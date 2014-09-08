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

# Base node class
from .node import BlenderNodeBase

class POSSplit(bpy.types.Node, BlenderNodeBase):
    bl_idname = "POSSplit"
    bl_label = "POS Split"

    rng_filename = StringProperty(subtype='FILE_PATH', default="//")

    def init(self, context):
        super(POSSplit, self).init(context)

        # Initialise sockets
        self.inputs.new("XYZSocket", "POS XYZ")
        self.outputs.new("XYZSocket", "1")
        self.outputs.new("XYZSocket", "2")

    def update(self):
        super(POSSplit, self).update()

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "rng_filename", text="RNG")
