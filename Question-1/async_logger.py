import threading
import queue
from datetime import datetime
import time
import os

class AsyncLogger:
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, log_directory='logs'):
        self.log_directory = log_directory
        self.log_queue = queue.Queue()
        self.active = True
        self.thread = threading.Thread(target=self._process_logs)
        self.current_date = datetime.now().strftime(self.DATE_FORMAT)
        self._ensure_directory_exists()
        self.thread.start()

    def _ensure_directory_exists(self):
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

    def _get_log_file_path(self):
        """Generate the path of the log file based on the current date."""
        return os.path.join(self.log_directory, f'log_{self.current_date}.txt')

    def log(self, message):
        """Enqueue a message for logging."""
        self.log_queue.put((message, datetime.now().strftime(self.DATE_FORMAT)))

    def _process_logs(self):
        file = None
        current_file_date = None
        try:
            while self.active or not self.log_queue.empty():
                try:
                    message, log_date = self.log_queue.get(timeout=0.1)
                    if log_date != current_file_date:
                        current_file_date = log_date
                        if file:
                            file.close()
                        file = open(self._get_log_file_path(), 'a')
                    file.write(f'{message}\n')
                except queue.Empty:
                    continue
        finally:
            if file:
                file.close()

    def stop(self, wait=True):
        self.active = False
        self.thread.join()

# Example usage
if __name__ == '__main__':
    logger = AsyncLogger()
    logger.log('Log entry 1')
    time.sleep(1)
    logger.log('Log entry 2')
    time.sleep(1)
    logger.log('Log entry 3')
    logger.stop()