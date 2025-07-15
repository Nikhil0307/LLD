import os
import datetime
import threading
import queue
import atexit
from conf.Constants import Constants


class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(
        self,
        log_dir='./logs',
        current_log_level=Constants.INFO,
        log_format="[{time}] {level}: {message}",
        max_log_size=5 * 1024 * 1024,  # 5MB
        max_backup_files=5,
        queue_size=10000,
        drop_if_queue_full=True,  # backpressure vs drop strategy
    ):
        if self._initialized:
            return

        os.makedirs(log_dir, exist_ok=True)
        self.log_dir = log_dir
        self.base_log_filename = f"{datetime.datetime.today().strftime('%Y-%m-%d')}.log"
        self.log_file = os.path.join(self.log_dir, self.base_log_filename)

        self.current_log_level = current_log_level
        self.log_format = log_format
        self.max_log_size = max_log_size
        self.max_backup_files = max_backup_files

        self.drop_if_queue_full = drop_if_queue_full
        self.log_queue = queue.Queue(maxsize=queue_size)
        self.shutdown_flag = threading.Event()

        self.log_levels = {
            Constants.DEBUG: 0,
            Constants.INFO: 1,
            Constants.WARNING: 2,
            Constants.ERROR: 3,
        }

        self._start_worker_thread()
        atexit.register(self.shutdown)
        self._initialized = True

    def _start_worker_thread(self):
        self.worker = threading.Thread(target=self._process_logs, daemon=True)
        self.worker.start()

    def _process_logs(self):
        while not self.shutdown_flag.is_set() or not self.log_queue.empty():
            try:
                log_message = self.log_queue.get(timeout=1)
                self._write_to_file(log_message)
                self.log_queue.task_done()
            except queue.Empty:
                continue

    def _rotate_logs(self):
        for i in range(self.max_backup_files - 1, 0, -1):
            src = os.path.join(self.log_dir, f"{self.base_log_filename}.{i}")
            dst = os.path.join(self.log_dir, f"{self.base_log_filename}.{i+1}")
            if os.path.exists(src):
                os.rename(src, dst)

        if os.path.exists(self.log_file):
            os.rename(self.log_file, f"{self.log_file}.1")

    def _write_to_file(self, log_message):
        if os.path.exists(self.log_file) and os.path.getsize(self.log_file) > self.max_log_size:
            self._rotate_logs()

        with open(self.log_file, 'a') as f:
            f.write(log_message + '\n')

    def log(self, message: str, level=Constants.INFO):
        if level not in self.log_levels:
            raise ValueError(f"Invalid log level: {level}")

        if self.log_levels[level] < self.log_levels[self.current_log_level]:
            return

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted = self.log_format.format(time=timestamp, level=level, message=message)

        try:
            self.log_queue.put_nowait(formatted)
        except queue.Full:
            if self.drop_if_queue_full:
                # Drop silently
                pass
            else:
                # Backpressure: block until space
                self.log_queue.put(formatted)

    def shutdown(self):
        if not self.shutdown_flag.is_set():
            self.shutdown_flag.set()
            self.worker.join(timeout=5)
            while not self.log_queue.empty():
                try:
                    self._write_to_file(self.log_queue.get_nowait())
                except queue.Empty:
                    break
