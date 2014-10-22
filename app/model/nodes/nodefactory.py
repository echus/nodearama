# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   nodebase.py
# Date:   2014-09-08
# Author: Varvara Efremova
#
# Description:
# Node factory for dynamic node creation
# =============================================================================

from .posread import POSReadNode
from .posview import POSViewNode

class NodeFactory:
    __nodefact = {
            'POSReadNode': POSReadNode(),
            'POSViewNode': POSViewNode(),
            }

    @classmethod
    def make(cls, nodetype):
        """Node factory: Returns a node of type nodetype"""
        # TODO raise error if nodetype doesn't exist
        return cls.__nodefact[nodetype]


