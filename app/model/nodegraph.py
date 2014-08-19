# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   nodegraph.py
# Date:   2014-08-14
# Author: Varvara Efremova
#
# Description:
# NodeGraph class defining node operations and the node graph model
# =============================================================================

import networkx as nx

class NodeGraph:
    def __init__(self):
        graph = nx.MultiDiGraph()

    def add_node(self, node):
        # TODO check that it's a NodeBase
        self.graph.add_node(node)

    def remove_node(self, node):
        self.graph.remove_node(node)

    def add_edge(self, from_node, to_node):
        self.graph.add_edge(from_node, to_node)

    def remove_edge(self, from_node, to_node):
        # TODO how to deal with multiple edges here??
        self.graph.remove_edge(from_node, to_node)

    def evaluate_graph(self):
        """Evaluate total graph from starting node and return final output value"""
        # topological sort
        return
