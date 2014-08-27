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

# === Event base: all events must reference the node they are acting on ===

class EventBase:
    def __init__(self, uuid):
        self.uuid = uuid # Unique reference to object event is acting on

class CreateNode(EventBase):
    def __init__(self, uuid):
        super(CreateNode, self).__init__(uuid)

class DeleteNode(EventBase):
    def __init__(self, uuid):
        super(DeleteNode, self).__init__(uuid)

class UpdateNode(EventBase):
    def __init__(self, uuid, properties=None, links=None):
        super(UpdateNode, self).__init__(uuid)
        self.properties = properties
        self.links = links

class CreateNodeTree(EventBase):
    def __init__(self, uuid):
        super(CreateNodeTree, self).__init__(uuid)
