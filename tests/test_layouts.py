from algorithm_visualizer import Commander
from algorithm_visualizer import Layout

from tests import CommanderTestCase


class LayoutsTests(CommanderTestCase):
    def setUp(self):
        self.child = Commander()
        self.layout = Layout([self.child])

    def test_layout_create(self):
        layout = Layout([self.child])

        self.assertCommandEqual("Layout", [self.child.key], key=layout.key)

    def test_layout_setRoot(self):
        self.layout.setRoot(self.child)

        self.assertCommandEqual("setRoot", self.child.key)

    def test_layout_add(self):
        index = 1
        self.layout.add(self.child, index)

        self.assertCommandEqual("add", self.child.key, index, key=self.layout.key)

    def test_layout_remove(self):
        self.layout.remove(self.child)

        self.assertCommandEqual("remove", self.child.key, key=self.layout.key)

    def test_layout_removeAll(self):
        self.layout.removeAll()

        self.assertCommandEqual("removeAll", key=self.layout.key)
