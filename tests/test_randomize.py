import unittest

from algorithm_visualizer import Randomize

ITERATIONS = 100


class IntegerTests(unittest.TestCase):
    def test_integer_type(self):
        rand = Randomize.Integer()
        value = rand.create()

        self.assertIs(type(value), int)

    def test_integer_range(self):
        rand_range = (1, 2)
        rand = Randomize.Integer(*rand_range)

        for _ in range(ITERATIONS):
            value = rand.create()

            self.assertIn(value, rand_range)


class DoubleTests(unittest.TestCase):
    def test_double_type(self):
        rand = Randomize.Double()
        value = rand.create()

        self.assertIs(type(value), float)

    def test_double_range(self):
        rand_range = (1.0, 2.0)
        rand = Randomize.Double(*rand_range)

        for _ in range(ITERATIONS):
            value = rand.create()

            self.assertGreaterEqual(value, 1.0)
            self.assertLessEqual(value, 2.0)


class StringTests(unittest.TestCase):
    def test_string_type(self):
        rand = Randomize.String()
        value = rand.create()

        self.assertIs(type(value), str)

    def test_string_length(self):
        rand = Randomize.String(10)
        value = rand.create()

        self.assertEqual(len(value), 10)

    def test_string_letters(self):
        letters = ('a', 'b', 'c')
        rand = Randomize.String(letters=letters)

        for _ in range(ITERATIONS):
            for char in rand.create():
                self.assertIn(char, letters)


class Array1DTests(unittest.TestCase):
    def test_array1d_length(self):
        rand = Randomize.Array1D(5)
        array = rand.create()

        self.assertEqual(len(array), 5)

    def test_array1d_randomizer(self):
        rand = Randomize.Array1D(ITERATIONS, randomizer=Randomize.Double(2, 4))
        array = rand.create()

        for value in array:
            self.assertIs(type(value), float)
            self.assertGreaterEqual(value, 2)
            self.assertLessEqual(value, 4)

    def test_array1d_sorted(self):
        rand = Randomize.Array1D(ITERATIONS)

        sort_ret = rand.sorted(True)
        self.assertIs(sort_ret, rand)
        self.assertTrue(rand._sorted)

        array = rand.create()

        for i in range(len(array) - 1):
            self.assertLessEqual(array[i], array[i + 1])


class Array2DTests(unittest.TestCase):
    def test_array2d_length(self):
        rand = Randomize.Array2D(5, 3)
        arrays = rand.create()

        self.assertEqual(len(arrays), 5)

        for array in arrays:
            self.assertEqual(len(array), 3)

    def test_array2d_randomizer(self):
        rand = Randomize.Array2D(ITERATIONS, ITERATIONS, randomizer=Randomize.Double(2, 4))
        arrays = rand.create()

        for array in arrays:
            for value in array:
                self.assertIs(type(value), float)
                self.assertGreaterEqual(value, 2)
                self.assertLessEqual(value, 4)

    def test_array2d_sorted(self):
        rand = Randomize.Array2D(ITERATIONS, ITERATIONS)

        sort_ret = rand.sorted(True)
        self.assertIs(sort_ret, rand)
        self.assertTrue(rand._sorted)

        arrays = rand.create()

        for array in arrays:
            for i in range(len(array) - 1):
                self.assertLessEqual(array[i], array[i + 1])


class GraphTests(unittest.TestCase):
    def test_graph_length(self):
        rand = Randomize.Graph(3)
        graph = rand.create()

        self.assertEqual(len(graph), 3)

        for edges in graph:
            self.assertEqual(len(edges), 3)

    def test_graph_no_loops(self):
        rand = Randomize.Graph(ITERATIONS, ratio=1)
        graph = rand.create()

        for i, edges in enumerate(graph):
            for j, edge in enumerate(edges):
                if i == j:
                    self.assertEqual(edge, 0)

    def test_graph_ratio_1(self):
        rand = Randomize.Graph(ITERATIONS, ratio=1)
        graph = rand.create()

        for i, edges in enumerate(graph):
            for j, edge in enumerate(edges):
                if i != j:
                    self.assertEqual(edge, 1)

    def test_graph_ratio_0(self):
        rand = Randomize.Graph(ITERATIONS, ratio=0)
        graph = rand.create()

        for i, edges in enumerate(graph):
            for j, edge in enumerate(edges):
                if i != j:
                    self.assertEqual(edge, 0)

    def test_graph_undirected(self):
        rand = Randomize.Graph(ITERATIONS)

        directed_ret = rand.directed(False)
        self.assertIs(directed_ret, rand)
        self.assertFalse(rand._directed)

        graph = rand.create()

        for i, edges in enumerate(graph):
            for j, edge in enumerate(edges):
                if i != j:
                    self.assertEqual(edge, graph[j][i])

    def test_graph_weighted(self):
        rand = Randomize.Graph(ITERATIONS, ratio=1, randomizer=Randomize.Double(2, 4))

        weighted_ret = rand.weighted()
        self.assertIs(weighted_ret, rand)
        self.assertTrue(rand._weighted)

        graph = rand.create()

        for i, edges in enumerate(graph):
            for j, edge in enumerate(edges):
                if i != j:
                    self.assertIs(type(edge), float)
                    self.assertGreaterEqual(edge, 2)
                    self.assertLessEqual(edge, 4)
