import numpy as np


class AdjacencyMatrix(object):

    @staticmethod
    def count_vertices_undirected_graph(adj_matrix: np.array) -> int:
        """
        Counts the number of vertices in an undirected graph

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: int, the number of vertices
        """
        
        return len(adj_matrix)

    @staticmethod
    def count_edges_undirected_graph(adj_matrix: np.array) -> int:
        """
        Counts the number of edges in an undirected graph

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: int, the number of edges
        """
        
        return np.sum(adj_matrix) // 2

    @staticmethod
    def count_vertices_directed_graph(adj_matrix: np.array) -> int:
        """
        Counts the number of vertices in an directed graph

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: int, the number of vertices
        """
        
        return len(adj_matrix)

    @staticmethod
    def count_edges_directed_graph(adj_matrix: np.array) -> int:
        """
        Counts the number of edges in an directed graph

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: int, the number of edges
        """
        
        return np.sum(adj_matrix)

    @staticmethod
    def count_odd_neighbours_undirected_graph(adj_matrix: np.array) -> int:
        """
        Counts the number of vertices that have an odd number of neighbours

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: int, the number of vertices that have an odd number of
        neighbours
        """
        
        n = 0
        for i in adj_matrix:
            if np.sum(i) % 2 != 0:
                n += 1
        return n

    @staticmethod
    def invert_directed_graph(adj_matrix: np.array) -> np.array:
        """
        Inverts the graph represented in adj_matrix in such a way, that each
        edge is switched direction, i.e., if there was an edge from
        adj_matrix[i][j] it will be directed the other way around, and vice
        versa. Pay additional attention to vertices that are connected in both
        directions.

        :param adj_matrix: The graph in adjacency matrix format, where
        adj_matrix[i][j] indicates whether there is an edge between vertex i
        and j
        :return: numpy array, representing the inverted graph
        """

        # FIXME: Kan wss beter
        n_edges = AdjacencyMatrix.count_vertices_directed_graph(adj_matrix)
        coord = []
        for index, x in np.ndenumerate(adj_matrix):
            if x == 1:
                i = index[0]
                j = index[1]

                coord.append((j, i))
            
        adj_matrix = np.zeros((n_edges, n_edges))
        for c in coord:
            adj_matrix[c] = 1

        return adj_matrix
