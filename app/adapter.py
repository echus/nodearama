# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   adapter.py
# Date:   2014-08-14
# Author: Varvara Efremova
#
# Description:
# MVA Adapter
# =============================================================================

from .communication.observe import Observer

class Adapter(Observer):
    def __init__(self, observable):
        # Register observer
        super(Adapter, self).__init__(observable)

        # Initialise event handler dict
        self.handler = {
            'CreateNode': self.onCreateNode,
            'DeleteNode': self.onDeleteNode,
            'UpdateNode': self.onUpdateNode,
            'CreateNodeTree': self.onCreateNodeTree,
            }

        self.graphs = [] # NodeGraph storage list

    def notify(self, observable, event):
        # Get name of event class
        event_name = event.__class__.__name__
        # Call appropriate handler
        self.handler[event_name](event)

    def onCreateNode(self, event):
        print("Create node with id", event.uuid)

    def onDeleteNode(self, event):
        print("Delete node with id", event.uuid)

    def onUpdateNode(self, event):
        print("Update node with id", event.uuid)

    def onCreateNodeTree(self, event):
        print("Create nodetree with id", event.uuid)
