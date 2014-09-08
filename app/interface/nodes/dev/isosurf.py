# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   isosurf.py
# Date:   2014-08-14
# Author: Varvara Efremova
#
# Description:
# Blender isosurface node interface definition
# =============================================================================

# Blender API
import bpy
from bpy.props import FloatProperty

# Base node class
from .node import BlenderNodeBase

class Isosurf(bpy.types.Node, BlenderNodeBase):
    bl_idname = "Isosurf"
    bl_label = "Isosurface"

    value = FloatProperty(default=1.0)

    def init(self, context):
        super(Isosurf, self).init(context)

        # Initialise sockets
        self.inputs.new("XYZSocket", "Density")
        self.outputs.new("XYZSocket", "Isosurface")

    def update(self):
        super(Isosurf, self).update()

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "value", text="Value")
