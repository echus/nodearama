# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   tree.py
# Date:   2014-08-14
# Author: Varvara Efremova
#
# Description:
# Blender NodeTree implementation (UI)
# =============================================================================

# Blender API
import bpy

# For generating NodeTree IDs
from uuid import uuid4

# Base class for ID tagging
from .base import IDable
# Event classes for communication with Observer
from ..communication.events import UpdateNodeTree

class NodearamaTree(bpy.types.NodeTree, IDable):
    bl_description = "Atom probe analysis nodes"
    bl_icon = "MESH_CYLINDER"
    bl_idname = "Nodearama"
    bl_label = "Nodearama"

    def init(self):
        # Generate unique ID
        self.generate_id()

        # Communicate creation to observers
        #obs = bpy.context.scene.observable
        #event = CreateNodeTree(self.uuid)
        #obs.notify_observers(event)

    def update(self):
        # Initialise node if not initialised yet
        if not self.initialised():
            self.init()

        # Event information
        uuid = self.uuid
        nodes = self.gen_node_dict()
        links = self.gen_link_dict()

        # Communicate update
        obs = bpy.context.scene.observable
        event = UpdateNodeTree(uuid, nodes, links)
        obs.notify_observers(event)

    def gen_node_dict(self):
        bl_nodes = self.nodes # List of blender nodes currently in NodeTree
        nodes = {}            # Dict of node information

        for bl_node in bl_nodes:
            uuid = bl_node.uuid                       # Unique node ID
            nodes[uuid] = {}                          # New dict for each node
            nodes[uuid]['bl_idname'] = bl_node.bl_idname # Node type
            #for prop in bl_node.props:
            #     nodes[uuid][prop.name] = prop.value
        return nodes

    def gen_link_dict(self):
        links = self.links
        return links

