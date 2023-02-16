import numpy as np
import typing


class AdjacencyList(object):

    @staticmethod
    def count_vertices_undirected_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        """
        Counts the number of vertices in an undirected graph

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: int, the number of vertices
        """
        
        return len(adj_list)

    @staticmethod
    def count_edges_undirected_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        """
        Counts the number of edges in an undirected graph

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: int, the number of edges
        """

        return sum(len(val) for val in adj_list.values()) // 2

    @staticmethod
    def count_vertices_directed_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        """
        Counts the number of vertices in a directed graph

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: int, the number of vertices
        """
        
        return len(adj_list)

    @staticmethod
    def count_edges_directed_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        """
        Counts the number of edges in an undirected graph

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: int, the number of nodes/vertices
        """

        return sum(len(val) for val in adj_list.values())

    @staticmethod
    def count_odd_neighbours_undirected_graph(
            adj_list: typing.Dict[int, typing.List[int]]) -> int:
        """
        Counts the number of vertices that have an odd number of neighbours

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: int, the number of edges
        """
        
        return sum(len(val) % 2 != 0 for val in adj_list.values())

    @staticmethod
    def list_to_matrix(
            adj_list: typing.Dict[int, typing.List[int]]) -> np.array:
        """
        Accepts a graph in the adjacency list format, and returns it in the
        adjacency matrix format.

        :param adj_list: The graph in adjacency list format, where
        adj_list[i] consists of a list, where each element of that list
        indicates an edge to a specific vertex
        :return: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        """
        
        n_edges = AdjacencyList.count_vertices_directed_graph(adj_list)
        matrix = np.empty((n_edges, n_edges))
        for k, lst in adj_list.items():
            for v in lst:
                matrix[k][v] = 1

        return matrix
