from algorithm_visualizer import Tracer

from tests import CommanderTestCase


class TracerTests(CommanderTestCase):
    def setUp(self):
        self.tracer = Tracer()

    def test_tracer_create(self):
        args = ["foo"]
        tracer = Tracer(*args)

        self.assertCommandEqual("Tracer", *args, key=tracer.key)

    def test_tracer_delay(self):
        args = [5]
        self.tracer.delay(*args)

        self.assertCommandEqual("delay", *args)

    def test_tracer_set(self):
        self.tracer.set()

        self.assertCommandEqual("set", key=self.tracer.key)

    def test_tracer_reset(self):
        self.tracer.reset()

        self.assertCommandEqual("reset", key=self.tracer.key)
