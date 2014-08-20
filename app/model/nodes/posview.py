# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   posview.py
# Date:   2014-08-19
# Author: Varvara Efremova
#
# Description:
# POSView display node definition
# =============================================================================

# Node base and slots
from . import NodeBase

N_IN = 1
N_OUT = 0

class POSViewNode(NodeBase):
    def __init__(self):
        # Initialise input and output slots
        super(POSViewNode, self).__init__(N_IN, N_OUT)

    def evaluate(self):
        print("POS input received:")
        slot = self._get_input(0)
        print(slot)
        print(slot.value)
        return "FINISHED"
