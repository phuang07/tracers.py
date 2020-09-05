from algorithm_visualizer import LogTracer

from tests import CommanderTestCase


class LogTests(CommanderTestCase):
    def setUp(self):
        self.logger = LogTracer()

    def test_log_set(self):
        args = [1]
        self.logger.set(*args)

        self.assertCommandEqual("set", *args, key=self.logger.key)

    def test_log_print(self):
        args = ["hello"]
        self.logger.print(*args)

        self.assertCommandEqual("print", *args, key=self.logger.key)

    def test_log_println(self):
        args = ["hello"]
        self.logger.println(*args)

        self.assertCommandEqual("println", *args, key=self.logger.key)

    def test_log_printf(self):
        args = ["%s", "hello"]
        self.logger.printf(*args)

        self.assertCommandEqual("printf", *args, key=self.logger.key)
