# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   pos_read.py
# Date:   2014-08-14
# Author: Varvara Efremova
#
# Description:
# Blender POSRead node definition
# =============================================================================

# Blender API
import bpy
from bpy.props import PointerProperty, StringProperty

# Base class for ID tagging
from ..base import IDable
# Events for communication with Observer (Adapter)
from ...communication.events import CreateNode, DeleteNode, UpdateNode

class POSRead(bpy.types.Node, IDable):
    bl_idname = "POSRead"
    bl_label = "POS Read"

    pos_filename = StringProperty(subtype='FILE_PATH', default="//")
    rng_filename = StringProperty(subtype='FILE_PATH', default="//")

    def init(self, context):
        # Initialise sockets
        self.outputs.new("XYZSocket", "XYZ")

        # Generate unique ID for this node
        self.generate_id()

        # Communicate creation to observers
        obs = bpy.context.scene.observable
        event = CreateNode(self.uuid)
        obs.notify_observers(event)

    def update(self):
        # Check node is initialised
        if not self.initialised():
            print("node not init'd yet")
            return

        # Communicate updated info to observers
        obs = bpy.context.scene.observable
        event = UpdateNode(self.uuid)
        obs.notify_observers(event)

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "pos_filename", text="POS")
        col.prop(self, "rng_filename", text="RNG")
