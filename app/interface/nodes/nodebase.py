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
# Base classes used by all nodes
# BlenderNodeBase:
#     Blender base node class definition (all nodes inheret from this)
#     Initialises node ID and general node settings
# =============================================================================

# Blender API
import bpy

# Base class for ID tagging
from ..base import IDable

class BlenderNodeBase(IDable):
    def init(self, context, color=None):
        # Generate unique ID for this node
        self.generate_id()

        # Use custom color if specified
        if color is not None:
            self.use_custom_color = True
            self.color = color

    def update(self):
        pass
        # Check node is initialised
        #if not self.initialised():
        #    print("node not init'd yet")
        #    return
