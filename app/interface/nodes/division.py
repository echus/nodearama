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

class Division(bpy.types.Node, BlenderNodeBase):
    bl_idname = "Division"
    bl_label = "Vector Division"

    def init(self, context):
        super(Division, self).init(context)

        # Initialise sockets
        self.inputs.new("XYZSocket", "Input 1")
        self.inputs.new("XYZSocket", "Input 2")
        self.outputs.new("XYZSocket", "Result")

    def update(self):
        super(Division, self).update()

    #def draw_buttons(self, context, layout):
        #col = layout.column()
        #col.label("Divide vectors")
