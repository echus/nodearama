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
from . import BlenderNodeBase

class POSViewNode(bpy.types.Node, BlenderNodeBase):
    bl_idname = "POSViewNode"
    bl_label = "POS View"

    def init(self, context):
        super(POSViewNode, self).init(context)

        # Initialise sockets
        self.inputs.new("XYZSocket", "XYZ")

    def update(self):
        super(POSViewNode, self).update()

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.label("See 3D View")
