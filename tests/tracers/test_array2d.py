import unittest

from algorithm_visualizer import Commander
from algorithm_visualizer import Array2DTracer


class Array2DTests(unittest.TestCase):
    def setUp(self):
        self.tracer = Array2DTracer()

    def test_array2d_set(self):
        args = [
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
        ]
        self.tracer.set(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "set",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array2d_patch(self):
        args = [1, 2, "foo"]
        self.tracer.patch(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "patch",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array2d_depatch(self):
        args = [1, 2]
        self.tracer.depatch(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "depatch",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array2d_select(self):
        args = [1, 2, 3, 4]
        self.tracer.select(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "select",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array2d_selectRow(self):
        args = [1, 2, 3]
        self.tracer.selectRow(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "selectRow",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array2d_selectCol(self):
        args = [1, 2, 3]
        self.tracer.selectCol(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "selectCol",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array2d_deselect(self):
        args = [1, 2, 3, 4]
        self.tracer.deselect(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "deselect",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array2d_deselectRow(self):
        args = [1, 2, 3]
        self.tracer.deselectRow(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "deselectRow",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_array2d_deselectCol(self):
        args = [1, 2, 3]
        self.tracer.deselectCol(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "deselectCol",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)
