# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   node.py
# Date:   2014-08-14
# Author: Varvara Efremova
#
# Description:
# Abstract base class defining analysis node structure
# =============================================================================

import abc

class NodeBase:
    __metaclass__ = abc.ABCMeta

    # Input/output slots
    # These need to be initialised to correct sizes
    __input = []
    __output = []

    def set_input(self, i, value):
        """Set ith input slot value"""
        # TODO error handling
        # TODO check that value is of a slot type
        __input[i] = value

    def output(self, i):
        """Return ith output slot value"""
        return __output[i]

    @abc.abstractmethod
    def evaluate():
        """Evaluate node outputs using input slot values"""
        return
