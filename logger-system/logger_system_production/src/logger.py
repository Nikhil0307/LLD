import os
import datetime
import threading
import queue
import atexit
import json
import glob
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
            log_dir=Constants.LOG_FILE_PATH,
            current_log_level=Constants.INFO,
            log_format="[{time}] {level}: {message}",
            max_log_size=5 * 1024 * 1024,  # 5MB
            max_backup_files=5,
            queue_size=10000,
            drop_if_queue_full=True,  # backpressure vs drop strategy
            console_logging=False,
            structured_logging=False,
            retention_days=7,
            extra_fields=None
    ):
        if self._initialized:
            return

        os.makedirs(log_dir, exist_ok=True)
        self.log_dir = log_dir
        self.base_log_filename = f"Application-{datetime.datetime.today().strftime('%Y-%m-%d')}.log"
        self.log_file = os.path.join(self.log_dir, self.base_log_filename)

        self.current_log_level = current_log_level
        self.log_format = log_format
        self.max_log_size = max_log_size
        self.max_backup_files = max_backup_files

        self.drop_if_queue_full = drop_if_queue_full
        self.log_queue = queue.Queue(maxsize=queue_size)
        self.shutdown_flag = threading.Event()

        self.console_logging = console_logging
        self.structured_logging = structured_logging
        self.retention_days = retention_days
        self.extra_fields = extra_fields if extra_fields is not None else {}

        self.log_levels = {
            Constants.DEBUG: 0,
            Constants.INFO: 1,
            Constants.WARNING: 2,
            Constants.ERROR: 3,
        }

        # Apply retention policy at startup (optional; could be run periodically if needed)
        self._apply_retention_policy()

        self._start_worker_thread()
        atexit.register(self.shutdown)
        self._initialized = True

    def _start_worker_thread(self):
        self.worker = threading.Thread(target=self._process_logs, daemon=True)
        self.worker.start()

    def _process_logs(self):
        while not self.shutdown_flag.is_set() or not self.log_queue.empty():
            try:
                log_record = self.log_queue.get(timeout=1)
                self._write_log(log_record)
                self.log_queue.task_done()
            except queue.Empty:
                continue

    def _rotate_logs(self):
        # Rotate backup files first
        for i in range(self.max_backup_files - 1, 0, -1):
            src = os.path.join(self.log_dir, f"{self.base_log_filename}.{i}")
            dst = os.path.join(self.log_dir, f"{self.base_log_filename}.{i + 1}")
            if os.path.exists(src):
                os.rename(src, dst)

        if os.path.exists(self.log_file):
            os.rename(self.log_file, f"{self.log_file}.1")

        # Reapply retention after rotation
        self._apply_retention_policy()

    def _apply_retention_policy(self):
        """
        Deletes log files older than the retention policy (in days).
        You can modify this function to implement a max count policy if needed.
        """
        now = datetime.datetime.now()
        for filepath in glob.glob(os.path.join(self.log_dir, "*.log*")):
            try:
                file_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
                age = (now - file_time).days
                if age >= self.retention_days:
                    os.remove(filepath)
            except Exception as e:
                print(f"Error deleting old log file {filepath}: {e}")

    def _format_log(self, level, message, extra_fields):
        """
        Formats the log record either as a JSON string or as a plain text using the log_format.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Merge default extra fields with any additional fields passed to log()
        record = {
            "time": timestamp,
            "level": level,
            "message": message,
        }
        # Update the record with any default extra fields (like request_id, component_name)
        record.update(self.extra_fields)
        # Also update with any call-specific extra fields
        record.update(extra_fields or {})

        if self.structured_logging:
            return json.dumps(record)
        else:
            # For non-JSON, use the custom format
            formatted_message = self.log_format.format(time=timestamp, level=level, message=message)
            # Append key/value of the extra fields for visibility
            if extra_fields:
                extras = " ".join(f"{k}={v}" for k, v in extra_fields.items())
                formatted_message += f" {extras}"
            return formatted_message

    def _write_log(self, log_record):
        # Check if file rotation is needed
        if os.path.exists(self.log_file) and os.path.getsize(self.log_file) > self.max_log_size:
            self._rotate_logs()

        # Write to file
        with open(self.log_file, 'a') as f:
            f.write(log_record + '\n')

        # Optionally write to console if enabled
        if self.console_logging:
            print(log_record)

    def log(self, message: str, level=Constants.INFO, extra_fields=None):
        if level not in self.log_levels:
            raise ValueError(f"Invalid log level: {level}")

        if self.log_levels[level] < self.log_levels[self.current_log_level]:
            return

        # Format the log record with any extra fields passed to the call
        formatted = self._format_log(level, message, extra_fields)

        try:
            self.log_queue.put_nowait(formatted)
        except queue.Full:
            if self.drop_if_queue_full:
                # Drop silently
                pass
            else:
                # Backpressure: block until space is available
                self.log_queue.put(formatted)

    def shutdown(self):
        if not self.shutdown_flag.is_set():
            self.shutdown_flag.set()
            self.worker.join(timeout=5)
            # Flush remaining logs
            while not self.log_queue.empty():
                try:
                    self._write_log(self.log_queue.get_nowait())
                except queue.Empty:
                    break
