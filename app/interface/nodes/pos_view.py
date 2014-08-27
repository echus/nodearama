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

# Base node class
from .node import BlenderNodeBase

class POSView(bpy.types.Node, BlenderNodeBase):
    bl_idname = "POSView"
    bl_label = "POS View"

    def init(self, context):
        super(POSView, self).init(context)

        # Initialise sockets
        self.inputs.new("XYZSocket", "XYZ in")

    def update(self):
        super(POSView, self).update()

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.label("Hello World!")
