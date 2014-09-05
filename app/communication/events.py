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

# === Event bases ===
class NodeEventBase:
    def __init__(self, uuid, nodetree_uuid):
        self.uuid = uuid # Unique reference to object event is acting on
        self.nodetree_uuid = nodetree_uuid # Unique ref to parent NodeTree

class NodeTreeEventBase:
    def __init__(self, uuid):
        self.uuid = uuid # Unique reference to NodeTree event is acting on

# === Event definitions ===
# === Nodes ===
class CreateNode(NodeEventBase):
    def __init__(self, uuid, nodetree_uuid):
        super(CreateNode, self).__init__(uuid, nodetree_uuid)

class DeleteNode(NodeEventBase):
    def __init__(self, uuid, nodetree_uuid):
        super(DeleteNode, self).__init__(uuid, nodetree_uuid)

class UpdateNode(NodeEventBase):
    def __init__(self, uuid, nodetree_uuid, properties=None, links=None):
        super(UpdateNode, self).__init__(uuid, nodetree_uuid)
        self.properties = properties
        self.links = links

# === NodeTrees ===
class CreateNodeTree(NodeTreeEventBase):
    def __init__(self, uuid):
        super(CreateNodeTree, self).__init__(uuid)
