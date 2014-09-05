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

# NodeGraph is the observable model
from ..communication.observe import Observable

class NodeGraph(Observable):
    def __init__(self):
        super(NodeGraph, self).__init__()
        self.graph = nx.MultiDiGraph()

    def add_node(self, node):
        # TODO check that it's a NodeBase
        self.graph.add_node(node)

    def remove_node(self, node):
        self.graph.remove_node(node)

    def connect(self, from_node, to_node, from_slot, to_slot):
        self.graph.add_edge(from_node, to_node, fr=from_slot, to=to_slot)
        # Point input of to_node to Slot output of from_node
        output = from_node.get_output(from_slot)
        to_node.set_input(to_slot, output)

    def disconnect(self, from_node, to_node, from_slot, to_slot):
        self.graph.remove_edge(from_node, to_node, fr=from_slot, to=to_slot)
        to_node.set_input(to_slot, None)

    def evaluate(self):
        """Evaluate total graph from starting node and return final output value"""
        eval_list = nx.topological_sort(self.graph)
        for n in eval_list:
            n.evaluate()
            print("evaluating type", type(n))

        # Notify observers of finished calculation
        self.notify_observers("EVALUATION DONE")
        return "FINISHED"
