# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   node.py
# Date:   2014-08-14
# Author: Varvara Efremova
#
# Description:
# Blender base node class definition (all nodes inheret from this)
# Defines methods for notifying Observers on init/update/delete
# And initialises node ID
# =============================================================================

# Blender API
import bpy

# Base class for ID tagging
from ..base import IDable
# Events for communication with Observer (Adapter)
from ...communication.events import CreateNode, DeleteNode, UpdateNode

class BlenderNodeBase(IDable):
    def init(self, context, color=None):
        # Generate unique ID for this node
        self.generate_id()

        # Communicate creation to observers
        obs = bpy.context.scene.observable
        event = CreateNode(self.uuid, "NODETREE") # TODO PARENT NODETREE ID
        obs.notify_observers(event)

        # Use custom color if specified
        if color is not None:
            self.use_custom_color = True
            self.color = color

    def update(self):
        # Check node is initialised
        if not self.initialised():
            print("node not init'd yet")
            return

        # Communicate updated info to observers
        obs = bpy.context.scene.observable
        # TODO PARENT NODETREE ID
        event = UpdateNode(self.uuid, "NODETREE")
        obs.notify_observers(event)
