# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   events.py
# Date:   2014-08-25
# Author: Varvara Efremova
#
# Description:
# Event objects for communication with adapter
# =============================================================================

# === NodeTrees ===
#class CreateNodeTree:
#    """Called on new NodeTree creation"""
#    def __init__(self, uuid):
#        self.uuid = uuid

class UpdateNodeTree:
    """Called on NodeTree update"""
    def __init__(self, uuid, nodes, links):
        self.uuid = uuid
        self.nodes = nodes
        self.links = links
