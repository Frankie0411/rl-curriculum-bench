# File: metrics/graph_metrics.py

import networkx as nx
from typing import Dict, List, Tuple


class GraphMetrics:
    """Compute graph-based complexity metrics for multi-agent environments."""

    @staticmethod
    def compute_density(edges: List[Tuple[int, int]], num_nodes: int) -> float:
        """
        Compute graph density: ratio of actual edges to possible edges.

        Args:
            edges: List of edge tuples [(node1, node2), ...]
            num_nodes: Total number of nodes in graph

        Returns:
            Density value between 0 and 1
        """
        if num_nodes < 2:
            return 0.0

        G = nx.Graph()
        G.add_nodes_from(range(num_nodes))
        G.add_edges_from(edges)

        return nx.density(G)

    @staticmethod
    def compute_average_path_length(edges: List[Tuple[int, int]], num_nodes: int) -> float:
        """Compute average shortest path length in graph."""
        if num_nodes < 2:
            return 0.0

        G = nx.Graph()
        G.add_nodes_from(range(num_nodes))
        G.add_edges_from(edges)

        if not nx.is_connected(G):
            return float('inf')

        return nx.average_shortest_path_length(G)

    @staticmethod
    def compute_clustering_coefficient(edges: List[Tuple[int, int]], num_nodes: int) -> float:
        """Compute average clustering coefficient."""
        if num_nodes < 2:
            return 0.0

        G = nx.Graph()
        G.add_nodes_from(range(num_nodes))
        G.add_edges_from(edges)

        return nx.average_clustering(G)
