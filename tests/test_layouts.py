import unittest

from algorithm_visualizer import Commander
from algorithm_visualizer import Layout


class LayoutsTests(unittest.TestCase):
    def setUp(self):
        self.child = Commander()
        self.layout = Layout([self.child])
        self.create_cmd = Commander.commands[-1]

    def test_layout_create(self):
        expected_cmd = {
            "key": self.layout.key,
            "method": "Layout",
            "args": [[self.child.key]],
        }

        self.assertEqual(self.create_cmd, expected_cmd)

    def test_layout_setRoot(self):
        self.layout.setRoot(self.child)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": None,
            "method": "setRoot",
            "args": [self.child.key],
        }

        self.assertEqual(cmd, expected_cmd)

    def test_layout_add(self):
        self.layout.add(self.child, 1)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.layout.key,
            "method": "add",
            "args": [self.child.key, 1],
        }

        self.assertEqual(cmd, expected_cmd)

    def test_layout_remove(self):
        self.layout.remove(self.child)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.layout.key,
            "method": "remove",
            "args": [self.child.key],
        }

        self.assertEqual(cmd, expected_cmd)

    def test_layout_removeAll(self):
        self.layout.removeAll()
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.layout.key,
            "method": "removeAll",
            "args": [],
        }

        self.assertEqual(cmd, expected_cmd)
