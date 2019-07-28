import unittest

from algorithm_visualizer import Commander
from algorithm_visualizer import GraphTracer
from algorithm_visualizer import LogTracer


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.tracer = GraphTracer()

    def test_graph_set(self):
        args = [
            [
                [0, 1, 0],
                [1, 0, 1],
                [0, 1, 0],
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

    def test_graph_directed(self):
        args = [True]
        ret = self.tracer.directed(*args)

        self.assertIs(ret, self.tracer)

        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "directed",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_weighted(self):
        args = [True]
        ret = self.tracer.weighted(*args)

        self.assertIs(ret, self.tracer)

        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "weighted",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_layoutCircle(self):
        ret = self.tracer.layoutCircle()

        self.assertIs(ret, self.tracer)

        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "layoutCircle",
            "args": [],
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_layoutTree(self):
        args = [True]
        ret = self.tracer.layoutTree(*args)

        self.assertIs(ret, self.tracer)

        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "layoutTree",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_layoutRandom(self):
        ret = self.tracer.layoutRandom()

        self.assertIs(ret, self.tracer)

        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "layoutRandom",
            "args": [],
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_addNode(self):
        args = ["foo", 12.34, 1, 2, 3, 4]
        self.tracer.addNode(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "addNode",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_updateNode(self):
        args = ["foo", 12.34, 1, 2, 3, 4]
        self.tracer.updateNode(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "updateNode",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_removeNode(self):
        args = ["foo"]
        self.tracer.removeNode(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "removeNode",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_visit(self):
        args = ["foo", "bar", 12.34]
        self.tracer.visit(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "visit",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_leave(self):
        args = ["foo", "bar", 12.34]
        self.tracer.leave(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "leave",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_select(self):
        args = ["foo", "bar"]
        self.tracer.select(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "select",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_deselect(self):
        args = ["foo", "bar"]
        self.tracer.deselect(*args)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "deselect",
            "args": args,
        }

        self.assertEqual(cmd, expected_cmd)

    def test_graph_log(self):
        log = LogTracer()
        self.tracer.log(log)
        cmd = Commander.commands[-1]

        expected_cmd = {
            "key": self.tracer.key,
            "method": "log",
            "args": [log.key],
        }

        self.assertEqual(cmd, expected_cmd)
