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

    def __init__(self, num_inputs, num_outputs):
        # Initialise input/output slots
        self.__input = [None] * num_inputs
        self.__output = [None] * num_outputs

    def set_input(self, i, value):
        """Set ith input slot value"""
        # TODO error handling
        # TODO check that value is of a slot type
        self.__input[i] = value

    def get_output(self, i):
        """Return ith output slot value"""
        return self.__output[i]

    @abc.abstractmethod
    def evaluate(self):
        """Evaluate node outputs using input slot values"""
        return

    # Private methods for subclass use
    def _get_input(self, i):
        return self.__input[i]

    def _set_output(self, i, value):
        self.__output[i] = value
