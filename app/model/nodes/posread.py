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

# Node base and slots
from . import NodeBase
#from .slots import Array3DSlot

# Import APTRead module
from ...modules.aptread import ReadAPTData

N_IN = 0
N_OUT = 2

class POSReadNode(NodeBase):
    def __init__(self):
        # Initialise input and output slots
        super(POSReadNode, self).__init__(N_IN, N_OUT)
        # Node properties
        self.pos_path = ""
        self.rng_path = ""

    def evaluate(self):
        data = ReadAPTData(self.pos_path, self.rng_path)
        self._set_output(0, data.xyz)
        self._set_output(1, data.mc)
        return "FINISHED"
