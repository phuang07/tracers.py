from algorithm_visualizer import Array2DTracer

from tests import CommanderTestCase


class Array2DTests(CommanderTestCase):
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

        self.assertCommandEqual("set", *args, key=self.tracer.key)

    def test_array2d_patch(self):
        args = [1, 2, "foo"]
        self.tracer.patch(*args)

        self.assertCommandEqual("patch", *args, key=self.tracer.key)

    def test_array2d_depatch(self):
        args = [1, 2]
        self.tracer.depatch(*args)

        self.assertCommandEqual("depatch", *args, key=self.tracer.key)

    def test_array2d_select(self):
        args = [1, 2, 3, 4]
        self.tracer.select(*args)

        self.assertCommandEqual("select", *args, key=self.tracer.key)

    def test_array2d_selectRow(self):
        args = [1, 2, 3]
        self.tracer.selectRow(*args)

        self.assertCommandEqual("selectRow", *args, key=self.tracer.key)

    def test_array2d_selectCol(self):
        args = [1, 2, 3]
        self.tracer.selectCol(*args)

        self.assertCommandEqual("selectCol", *args, key=self.tracer.key)

    def test_array2d_deselect(self):
        args = [1, 2, 3, 4]
        self.tracer.deselect(*args)

        self.assertCommandEqual("deselect", *args, key=self.tracer.key)

    def test_array2d_deselectRow(self):
        args = [1, 2, 3]
        self.tracer.deselectRow(*args)

        self.assertCommandEqual("deselectRow", *args, key=self.tracer.key)

    def test_array2d_deselectCol(self):
        args = [1, 2, 3]
        self.tracer.deselectCol(*args)

        self.assertCommandEqual("deselectCol", *args, key=self.tracer.key)
