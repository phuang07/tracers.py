import unittest

from algorithm_visualizer import Commander
from algorithm_visualizer import Tracer


class TracerTests(unittest.TestCase):
    def setUp(self):
        self.tracer = Tracer()

    def test_tracer_create(self):
        title = "foo"
        tracer = Tracer(title)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": tracer.key,
            "method": "Tracer",
            "args": [title],
        }

        self.assertEqual(cmd, expected_cmd)

    def test_tracer_delay(self):
        delay = 5
        self.tracer.delay(delay)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": None,
            "method": "delay",
            "args": [delay],
        }

        self.assertEqual(cmd, expected_cmd)

    def test_tracer_set(self):
        self.tracer.set()
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "set",
            "args": [],
        }

        self.assertEqual(cmd, expected_cmd)

    def test_tracer_reset(self):
        self.tracer.reset()
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "reset",
            "args": [],
        }

        self.assertEqual(cmd, expected_cmd)
