import unittest

from algorithm_visualizer import Commander
from algorithm_visualizer import LogTracer


class LogTests(unittest.TestCase):
    def setUp(self):
        self.logger = LogTracer()

    def test_log_set(self):
        args = [1]
        self.logger.set(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.logger.key,
            "method": "set",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_log_print(self):
        args = ["hello"]
        self.logger.print(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.logger.key,
            "method": "print",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_log_println(self):
        args = ["hello"]
        self.logger.println(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.logger.key,
            "method": "println",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_log_printf(self):
        args = ["%s", "hello"]
        self.logger.printf(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.logger.key,
            "method": "printf",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)
