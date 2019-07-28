import unittest

from algorithm_visualizer import Commander
from algorithm_visualizer import Array1DTracer
from algorithm_visualizer import ChartTracer


class Array1DTests(unittest.TestCase):
    def setUp(self):
        self.tracer = Array1DTracer()

    def test_array1d_set(self):
        args = [[1, 2, 3]]
        self.tracer.set(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "set",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array1d_patch(self):
        args = [1, "foo"]
        self.tracer.patch(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "patch",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array1d_depatch(self):
        args = [1]
        self.tracer.depatch(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "depatch",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array1d_select(self):
        args = [1, 2]
        self.tracer.select(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "select",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array1d_deselect(self):
        args = [1, 2]
        self.tracer.deselect(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "deselect",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array1d_chart(self):
        chart = ChartTracer()
        self.tracer.chart(chart)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "chart",
            "args": [chart.key],
        }

        self.assertEqual(cmd, expected_cmd)
