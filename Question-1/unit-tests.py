import unittest
import os
from datetime import datetime
from async_logger import AsyncLogger 
import time

class TestAsyncLogger(unittest.TestCase):
    def test_log_written(self):
        logger = AsyncLogger()
        logger.log("Test log entry")
        logger.stop(wait=True)
        today = datetime.now().strftime("%Y-%m-%d")
        log_file = f'logs/log_{today}.txt'
        self.assertTrue(os.path.exists(log_file))
        with open(log_file, 'r') as file:
            content = file.read()
        self.assertIn("Test log entry", content)

    def test_create_file_at_midnight(self):
        logger = AsyncLogger()
        # Simulate crossing midnight; for real test, mock datetime to return different dates
        logger.current_date = "2999-12-31"  # Pretend it's an old date
        logger.log("Test log entry")
        logger.stop(wait=True)
        log_file = 'logs/log_2999-12-31.txt'
        self.assertTrue(os.path.exists(log_file))

    def test_stop_immediate(self):
        logger = AsyncLogger()
        logger.log("First entry")
        logger.stop(wait=False)
        time.sleep(0.1)  # Give some time for the thread to process
        logger.log("Second entry")
        logger.stop(wait=True)
        today = datetime.now().strftime("%Y-%m-%d")
        log_file = f'logs/log_{today}.txt'
        with open(log_file, 'r') as file:
            content = file.read()
        self.assertNotIn("Second entry", content)

if __name__ == '__main__':
    unittest.main()