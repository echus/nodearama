# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   pos_read.py
# Date:   2014-08-27
# Author: Varvara Efremova
#
# Description:
# Blender POSView node definition
# =============================================================================

# Blender API
import bpy

# Base class for ID tagging
from ..base import IDable
# Events for communication with Observer (Adapter)
from ...communication.events import CreateNode, DeleteNode, UpdateNode

class POSView(bpy.types.Node, IDable):
    bl_idname = "POSView"
    bl_label = "POS View"

    def init(self, context):
        # Initialise sockets
        self.inputs.new("XYZSocket", "XYZ in")

        # Generate unique ID for this node
        self.generate_id()

        # Communicate creation to observers
        obs = bpy.context.scene.observable
        event = CreateNode(self.uuid)
        obs.notify_observers(event)

    def update(self):
        # Check node is initialised
        if not self.initialised():
            return

        # Communicate updated info to observers
        obs = bpy.context.scene.observable
        event = UpdateNode(self.uuid)
        obs.notify_observers(event)

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.label("Hello World!")
