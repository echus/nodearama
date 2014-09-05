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
from ..communication.events import CreateNodeTree

class NodearamaTree(bpy.types.NodeTree, IDable):
    bl_description = "Atom probe analysis nodes"
    bl_icon = "MESH_CYLINDER"
    bl_idname = "Nodearama"
    bl_label = "Nodearama"

    def init(self):
        # Generate unique ID
        self.generate_id()

        # Communicate creation to observers
        obs = bpy.context.scene.observable
        event = CreateNodeTree(self.uuid)
        obs.notify_observers(event)

    def update(self):
        # Check nodetree is initialised, if not call init
        print("NT update called")

        if not self.initialised():
            self.init()
            return

        # Communicate update
        #obs = bpy.context.scene.observable
        #event = UpdateNodeTree(self.uuid)
        #obs.notify_observers(event)
