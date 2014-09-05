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
            'CreateNodeTree': self.onCreateNodeTree,
            'UpdateNodeTree': self.onUpdateNodeTree,
            }

        self.graphs = [] # NodeGraph storage list

    def notify(self, observable, event):
        """Invoke correct handler whenever an event is received"""
        # Get name of event class
        event_name = event.__class__.__name__
        # Call appropriate handler
        self.handler[event_name](event)

    def onCreateNodeTree(self, event):
        print("Create nodetree with id:", event.uuid)

    def onUpdateNodeTree(self, event):
        print("Update nodetree with id:", event.uuid)
        print("    Nodes:", event.nodes)
        print("    Links:", event.links)
