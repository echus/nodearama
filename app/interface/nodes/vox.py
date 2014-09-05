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
from bpy.props import FloatProperty

# Base node class
from .node import BlenderNodeBase

class Vox(bpy.types.Node, BlenderNodeBase):
    bl_idname = "Vox"
    bl_label = "Voxelisation"

    size = FloatProperty(default=1.0)

    def init(self, context):
        super(Vox, self).init(context)

        # Initialise sockets
        self.inputs.new("XYZSocket", "XYZ")
        self.outputs.new("XYZSocket", "Vox")

    def update(self):
        super(Vox, self).update()

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "size", text="Voxel size")
