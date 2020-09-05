import abc
import random
import string
from typing import List, NoReturn, Sequence

from algorithm_visualizer.types import Number


class _Randomizer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self) -> NoReturn:
        raise NotImplementedError  # pragma: no cover


class Integer(_Randomizer):
    def __init__(self, min: int = 1, max: int = 9):
        self._min = min
        self._max = max

    def create(self) -> int:
        return random.randint(self._min, self._max)


class Double(_Randomizer):
    def __init__(self, min: Number = 0, max: Number = 1):
        self._min = min
        self._max = max

    def create(self) -> float:
        return random.uniform(self._min, self._max)


class String(_Randomizer):
    def __init__(self, length: int = 16, letters: Sequence[str] = string.ascii_lowercase):
        self._length = length
        self._letters = letters

    def create(self) -> str:
        text = random.choices(self._letters, k=self._length)
        return "".join(text)


class Array1D(_Randomizer):
    def __init__(self, N: int = 10, randomizer: _Randomizer = Integer()):
        self._N = N
        self._randomizer = randomizer
        self._sorted = False

    def sorted(self, sorted: bool = True) -> "Array1D":
        self._sorted = sorted
        return self

    def create(self) -> List:
        array = [self._randomizer.create() for _ in range(self._N)]
        if self._sorted:
            array.sort()

        return array


class Array2D(Array1D):
    def __init__(self, N: int = 10, M: int = 10, randomizer: _Randomizer = Integer()):
        super().__init__(M, randomizer)
        self._M = N

    def sorted(self, sorted: bool = True) -> "Array2D":
        self._sorted = sorted
        return self

    def create(self) -> List[List]:
        # Explicitly pass args to super() to avoid a TypeError (BPO 26495).
        return [super(Array2D, self).create() for _ in range(self._M)]


class Graph(_Randomizer):
    def __init__(self, N: int = 5, ratio: Number = 0.3, randomizer: _Randomizer = Integer()):
        self._N = N
        self._ratio = ratio
        self._randomizer = randomizer
        self._directed = True
        self._weighted = False

    def directed(self, directed: bool = True) -> "Graph":
        self._directed = directed
        return self

    def weighted(self, weighted: bool = True) -> "Graph":
        self._weighted = weighted
        return self

    def create(self) -> List[List]:
        graph = [[None] * self._N for _ in range(self._N)]
        for i in range(self._N):
            for j in range(self._N):
                if i == j:
                    # Vertex can't have an edge to itself (no loops)
                    graph[i][j] = 0
                elif self._directed or i < j:
                    if random.random() >= self._ratio:
                        # Don't create an edge if the ratio is exceeded
                        graph[i][j] = 0
                    elif self._weighted:
                        graph[i][j] = self._randomizer.create()
                    else:
                        graph[i][j] = 1
                else:
                    # Edge is the same for both its vertices if it is not directed
                    # In such case the initial weight for the edge is set above when i < j
                    graph[i][j] = graph[j][i]

        return graph
