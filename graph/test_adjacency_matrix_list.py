import numpy as np
import numpy.testing
import typing
import unittest

from adjacency_matrix import AdjacencyMatrix
from adjacency_list import AdjacencyList


class GraphGenerator(object):

    @staticmethod
    def generate_undirected_graph(size):
        graph = np.random.randint(2, size=(size, size))
        num_edges = 0
        odd = 0
        for i in range(size):
            num_neighbours = 0
            for j in range(size):
                if j == i:
                    graph[i][j] = 0
                elif i < j:
                    graph[i][j] = graph[j][i]
                if graph[i][j]:
                    num_edges += 1
                    num_neighbours += 1
            if num_neighbours % 2 == 1:
                odd += 1
        return graph, int(num_edges / 2), odd

    @staticmethod
    def generate_directed_graph(size):
        graph = np.random.randint(2, size=(size, size))
        num_edges = 0
        odd = 0
        for i in range(size):
            num_neighbours = 0
            for j in range(size):
                if j == i:
                    graph[i][j] = 0
                if graph[i][j] > 0:
                    num_edges += 1
                    num_neighbours += 1
            if num_neighbours % 2 == 1:
                odd += 1
        return graph, num_edges, odd

    @staticmethod
    def matrix_to_list(adj_matrix: np.array) -> typing.Dict[int,
                                                            typing.List[int]]:
        adj_list = dict()
        n = len(adj_matrix)
        for i in range(n):
            current = []
            for j in range(n):
                if adj_matrix[i, j]:
                    current.append(j)
            adj_list[i] = current
        return adj_list


class TestAdjacencyMatrix(unittest.TestCase):

    def test_count_vertices_undirected_graph(self):
        n_cases = 5
        for i in range(n_cases):
            size = i + 5
            matrix, _, _ = GraphGenerator.generate_undirected_graph(size)
            student_answer = AdjacencyMatrix.count_vertices_undirected_graph(
                matrix)
            self.assertEqual(size, student_answer)

    def test_count_edges_undirected_graph(self):
        n_cases = 5
        for i in range(n_cases):
            size = i + 5
            matrix, n_edges, _ = GraphGenerator.generate_undirected_graph(size)
            student_answer = AdjacencyMatrix.count_edges_undirected_graph(
                matrix)
            self.assertEqual(n_edges, student_answer)

    def test_count_vertices_directed_graph(self):
        n_cases = 5
        for i in range(n_cases):
            size = i + 5
            matrix, _, _ = GraphGenerator.generate_directed_graph(size)
            student_answer = AdjacencyMatrix.count_vertices_directed_graph(
                matrix)
            self.assertEqual(size, student_answer)

    def test_count_edges_directed_graph(self):
        n_cases = 5
        for i in range(n_cases):
            size = i + 5
            matrix, n_edges, _ = GraphGenerator.generate_directed_graph(size)
            student_answer = AdjacencyMatrix.count_edges_directed_graph(matrix)
            self.assertEqual(n_edges, student_answer)

    def test_count_odd_neighbours_undirected_graph(self):
        n_cases = 10
        for i in range(n_cases):
            size = i + 5
            matrix, _, odd_neighbours = \
                GraphGenerator.generate_undirected_graph(size)
            student_answer = \
                AdjacencyMatrix.count_odd_neighbours_undirected_graph(matrix)
            self.assertEqual(odd_neighbours, student_answer)

    def test_invert_directed_graph(self):
        n_cases = 5
        for i in range(n_cases):
            size = i + 5
            matrix, _, _ = GraphGenerator.generate_directed_graph(size)
            student_answer = AdjacencyMatrix.invert_directed_graph(
                np.array(matrix))
            numpy.testing.assert_array_equal(matrix.T, student_answer)


class TestAdjacencyList(unittest.TestCase):

    def test_count_vertices_undirected_graph(self):
        n_cases = 5
        for i in range(n_cases):
            size = i + 5
            matrix, _, _ = GraphGenerator.generate_undirected_graph(size)
            adj_list = GraphGenerator.matrix_to_list(matrix)
            student_answer = AdjacencyList.count_vertices_undirected_graph(
                adj_list)
            self.assertEqual(size, student_answer)

    def test_count_edges_undirected_graph(self):
        n_cases = 5
        for i in range(n_cases):
            size = i + 5
            matrix, n_edges, _ = GraphGenerator.generate_undirected_graph(size)
            adj_list = GraphGenerator.matrix_to_list(matrix)
            student_answer = AdjacencyList.count_edges_undirected_graph(
                adj_list)
            self.assertEqual(n_edges, student_answer)

    def test_count_vertices_directed_graph(self):
        n_cases = 5
        for i in range(n_cases):
            size = i + 5
            matrix, _, _ = GraphGenerator.generate_undirected_graph(size)
            adj_list = GraphGenerator.matrix_to_list(matrix)
            student_answer = AdjacencyList.count_vertices_directed_graph(
                adj_list)
            self.assertEqual(size, student_answer)

    def test_count_edges_directed_graph(self):
        n_cases = 5
        for i in range(n_cases):
            size = i + 5
            matrix, n_edges, _ = GraphGenerator.generate_directed_graph(size)
            adj_list = GraphGenerator.matrix_to_list(matrix)
            student_answer = AdjacencyList.count_edges_directed_graph(adj_list)
            self.assertEqual(n_edges, student_answer)

    def test_count_odd_neighbours_undirected_graph(self):
        n_cases = 10
        for i in range(n_cases):
            size = i + 5
            matrix, _, odd_neighbours = \
                GraphGenerator.generate_undirected_graph(size)
            adj_list = GraphGenerator.matrix_to_list(matrix)
            student_answer = \
                AdjacencyList.count_odd_neighbours_undirected_graph(adj_list)
            self.assertEqual(odd_neighbours, student_answer)

    def test_list_to_matrix(self):
        n_cases = 5
        for i in range(n_cases):
            size = i + 5
            matrix, _, _ = GraphGenerator.generate_directed_graph(size)
            adj_list = GraphGenerator.matrix_to_list(matrix)
            student_answer = AdjacencyList.list_to_matrix(adj_list)
            numpy.testing.assert_array_equal(matrix, student_answer)
