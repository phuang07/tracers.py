from algorithm_visualizer import GraphTracer
from algorithm_visualizer import LogTracer

from tests import CommanderTestCase


class GraphTests(CommanderTestCase):
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

        self.assertCommandEqual("set", *args, key=self.tracer.key)

    def test_graph_directed(self):
        args = [True]
        ret = self.tracer.directed(*args)

        self.assertIs(ret, self.tracer)
        self.assertCommandEqual("directed", *args, key=self.tracer.key)

    def test_graph_weighted(self):
        args = [True]
        ret = self.tracer.weighted(*args)

        self.assertIs(ret, self.tracer)
        self.assertCommandEqual("weighted", *args, key=self.tracer.key)

    def test_graph_layoutCircle(self):
        ret = self.tracer.layoutCircle()

        self.assertIs(ret, self.tracer)
        self.assertCommandEqual("layoutCircle", key=self.tracer.key)

    def test_graph_layoutTree(self):
        args = [True]
        ret = self.tracer.layoutTree(*args)

        self.assertIs(ret, self.tracer)
        self.assertCommandEqual("layoutTree", *args, key=self.tracer.key)

    def test_graph_layoutRandom(self):
        ret = self.tracer.layoutRandom()

        self.assertIs(ret, self.tracer)
        self.assertCommandEqual("layoutRandom", key=self.tracer.key)

    def test_graph_addNode(self):
        args = ["foo", 12.34, 1, 2, 3, 4]
        self.tracer.addNode(*args)

        self.assertCommandEqual("addNode", *args, key=self.tracer.key)

    def test_graph_updateNode(self):
        args = ["foo", 12.34, 1, 2, 3, 4]
        self.tracer.updateNode(*args)

        self.assertCommandEqual("updateNode", *args, key=self.tracer.key)

    def test_graph_removeNode(self):
        args = ["foo"]
        self.tracer.removeNode(*args)

        self.assertCommandEqual("removeNode", *args, key=self.tracer.key)

    def test_graph_addEdge(self):
        args = ["source", "target", 12.34, 1, 2]
        self.tracer.addEdge(*args)

        self.assertCommandEqual("addEdge", *args, key=self.tracer.key)

    def test_graph_updateEdge(self):
        args = ["source", "target", 12.34, 1, 2]
        self.tracer.updateEdge(*args)

        self.assertCommandEqual("updateEdge", *args, key=self.tracer.key)

    def test_graph_removeEdge(self):
        args = ["source", "target"]
        self.tracer.removeEdge(*args)

        self.assertCommandEqual("removeEdge", *args, key=self.tracer.key)

    def test_graph_visit(self):
        args = ["foo", "bar", 12.34]
        self.tracer.visit(*args)

        self.assertCommandEqual("visit", *args, key=self.tracer.key)

    def test_graph_leave(self):
        args = ["foo", "bar", 12.34]
        self.tracer.leave(*args)

        self.assertCommandEqual("leave", *args, key=self.tracer.key)

    def test_graph_select(self):
        args = ["foo", "bar"]
        self.tracer.select(*args)

        self.assertCommandEqual("select", *args, key=self.tracer.key)

    def test_graph_deselect(self):
        args = ["foo", "bar"]
        self.tracer.deselect(*args)

        self.assertCommandEqual("deselect", *args, key=self.tracer.key)

    def test_graph_log(self):
        log = LogTracer()
        self.tracer.log(log)

        self.assertCommandEqual("log", log.key, key=self.tracer.key)
