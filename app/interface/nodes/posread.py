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
from bpy.props import StringProperty

# Base node class
#from .nodebase import BlenderNodeBase
from . import BlenderNodeBase

COLOR = (0.93, 0.47, 0.26)

class POSReadNode(bpy.types.Node, BlenderNodeBase):
    bl_idname = "POSReadNode"
    bl_label = "POS Read"

    pos_filename = StringProperty(subtype='FILE_PATH', default="//")
    #rng_filename = StringProperty(subtype='FILE_PATH', default="//")

    def init(self, context):
        super(POSReadNode, self).init(context, color=COLOR)

        # Initialise sockets
        self.outputs.new("XYZSocket", "POS XYZ")

    def update(self):
        super(POSReadNode, self).update()

    def draw_buttons(self, context, layout):
        col = layout.column()
        col.prop(self, "pos_filename", text="POS")
        #col.prop(self, "rng_filename", text="RNG")
