# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   slot.py
# Date:   2014-08-14
# Author: Varvara Efremova
#
# Description:
# Abstract base class defining slot structure
# =============================================================================

import abc

class SlotBase:
    __metaclass__ = abc.ABCMeta

    def value_getter(self):
        return

    def value_setter(self, value):
        return

    value = abc.abstractproperty(value_getter, value_setter)
