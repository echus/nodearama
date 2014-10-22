# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   adapter.py
# Date:   2014-08-14
# Author: Varvara Efremova
#
# Description:
# MVA Adapter
# =============================================================================

from .model import NodeGraph
from .model.nodes import NodeFactory

from .communication.observe import Observer

class Adapter(Observer):
    def __init__(self, observable):
        # Register observer for notifications from observable view
        super(Adapter, self).__init__(observable)

        # Initialise event handler dict
        self.handler = {
            'CreateNodeTree': self.on_create_node_tree,
            'UpdateNodeTree': self.on_update_node_tree,
            }

        self.graphs = {} # NodeGraph storage dict

    def notify(self, observable, event):
        """Invoke correct handler whenever an event is received"""
        # Get name of event class
        event_name = event.__class__.__name__
        # Call appropriate handler
        self.handler[event_name](event)

    # === Handlers ===
    def on_create_node_tree(self, event):
        pass
        #print("Create nodetree with id:", event.uuid)

    def on_update_node_tree(self, event):
        print("Update nodetree with id:", event.uuid)
        print("    Nodes:", event.nodes)
        print("    Links:", event.links)
        print()

        # Create new Graph if this is a new NodeTree
        if event.uuid not in self.graphs.keys():
            print("Creating new NodeGraph")
            self.graphs[event.uuid] = NodeGraph()
            print("    ", self.graphs)
            print()

        g = self.graphs[event.uuid] # Convenience
        # Loop over all nodes, comparing, if one not found create it etc
        # TODO a way to return nodes in NodeGraph in the same format as event sends them?
        # OR FIRST create Node from each Blender Node
        # Then write a compare function in NodeBase
        # And use this to compare nodes
        """if self.uuid not in self.graphs.keys():
            self.graphs[event.uuid] = NodeGraph()
            return

        g = self.graphs[event.uuid]

        # Do diffing here, find nodes to be created and deleted

        mk_nodes = []
        rm_nodes = []
        mk_links = []
        rm_links = []

        # Make graph nodes from blender node information
        nodes_to_add = [self.make_graph_node(b_node) for b_node in mk_nodes]
        # Add new nodes to graph
        for node in nodes_to_add:
            g.add_node(node)

        # Make links
        for b_link in mk_links:
            pass

        # Delete nodes
        for b_node in rm_nodes:
            pass

        # Delete links
        for b_link in rm_links:
            pass"""

    # === Maker functions ===
    def make_graph_node(b_node):
        """Returns a graph node given blender node instance"""
        uuid = b_node.uuid

        # Properties generated here

        # TODO make node factory to do this based on node bl_id!!!
        g_node = POSReadNode()
