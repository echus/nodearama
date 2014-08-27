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
import abc

class EventBase:
    __metaclass__ = abc.ABCMeta

    def __init__(self, node_id):
        self.node_id = node_id # Unique reference to object event is acting on

class CreateNode(EventBase):
    def __init__(self, node_id):
        super(CreateNode, self).__init__(node_id)

class DeleteNode(EventBase):
    def __init__(self, node_id):
        super(CreateNode, self).__init__(node_id)

class UpdateNode(EventBase):
    def __init__(self, node_id, properties, links):
        super(CreateNode, self).__init__(node_id)
        self.properties = properties
        self.links = links
