# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   posread.py
# Date:   2014-08-14
# Author: Varvara Efremova
#
# Description:
# POSRead analysis node definition
# =============================================================================

from node import NodeBase

N_IN = 0
N_OUT = 2

class POSReadNode(NodeBase):
    def __init__(self):
        super(POSReadNode, self).__init__(N_IN, N_OUT)

    def evaluate(self):
        print("number in, out:", N_IN, N_OUT)
        return "Done"
