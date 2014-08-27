# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   base.py
# Date:   2014-08-27
# Author: Varvara Efremova
#
# Description:
# Base mixin classes used for IDing Nodes/NodeTrees
# =============================================================================

from bpy.props import StringProperty

from uuid import uuid4

class IDable:
    """Mixin class with ID property"""
    uuid = StringProperty(default="")

    def initialised(self):
        """Is the ID initialised?"""
        if self.uuid == "":
            return False
        else:
            return True

    def generate_id(self):
        """Generate new UUID"""
        self.uuid = str(uuid4())
