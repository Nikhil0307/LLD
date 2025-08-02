import itertools
import threading
from concurrent.futures import ThreadPoolExecutor
from queue import PriorityQueue
from typing import Dict
from ..notification_model import Notification, Priority
from channel_factory import ChannelFactory

class Dispatcher:

    def __init__(self, worker_count: int = 10):
        self._queue = PriorityQueue()
        self._priority_map: Dict[Priority, int] = {
            Priority.high: 1,
            Priority.normal: 2,
            Priority.low: 3
        }
        self._counter = itertools.count()
        self._executor = ThreadPoolExecutor(max_workers=worker_count)

        self._dispatcher_thread = threading.Thread(target=self._worker_loop, daemon=True)
        self._dispatcher_thread.start()

    def queue_notification(self, notification: Notification) -> None:
        self._queue.put(
            (
                self._priority_map.get(notification.priority),
                next(self._counter), notification
            )
        )

    def _worker_loop(self):
        while True:
            _, _, notification = self._queue.get()
            self._executor.submit(self.dispatch, notification)

    def dispatch(self, notification):
        channel = ChannelFactory.get_channel(notification.channel)
        channel.send(notification)
