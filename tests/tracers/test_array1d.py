from algorithm_visualizer import Array1DTracer
from algorithm_visualizer import ChartTracer

from tests import CommanderTestCase


class Array1DTests(CommanderTestCase):
    def setUp(self):
        self.tracer = Array1DTracer()

    def test_array1d_set(self):
        args = [[1, 2, 3]]
        self.tracer.set(*args)

        self.assertCommandEqual("set", *args, key=self.tracer.key)

    def test_array1d_patch(self):
        args = [1, "foo"]
        self.tracer.patch(*args)

        self.assertCommandEqual("patch", *args, key=self.tracer.key)

    def test_array1d_depatch(self):
        args = [1]
        self.tracer.depatch(*args)

        self.assertCommandEqual("depatch", *args, key=self.tracer.key)

    def test_array1d_select(self):
        args = [1, 2]
        self.tracer.select(*args)

        self.assertCommandEqual("select", *args, key=self.tracer.key)

    def test_array1d_deselect(self):
        args = [1, 2]
        self.tracer.deselect(*args)

        self.assertCommandEqual("deselect", *args, key=self.tracer.key)

    def test_array1d_chart(self):
        chart = ChartTracer()
        self.tracer.chart(chart)

        self.assertCommandEqual("chart", chart.key, key=self.tracer.key)
