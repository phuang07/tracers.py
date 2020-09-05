from typing import TYPE_CHECKING

from .array2d import Array2DTracer
from algorithm_visualizer.types import Serializable, SerializableSequence, UNDEFINED

if TYPE_CHECKING:
    from .chart import ChartTracer


class Array1DTracer(Array2DTracer):
    def set(self, array1d: SerializableSequence[Serializable] = UNDEFINED):
        self.command("set", array1d)

    def patch(self, x: int, v: Serializable = UNDEFINED):
        self.command("patch", x, v)

    def depatch(self, x: int):
        self.command("depatch", x)

    def select(self, sx: int, ex: int = UNDEFINED):
        self.command("select", sx, ex)

    def deselect(self, sx: int, ex: int = UNDEFINED):
        self.command("deselect", sx, ex)

    def chart(self, chartTracer: "ChartTracer"):
        self.command("chart", chartTracer.key)
