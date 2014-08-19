# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   array3d.py
# Date:   2014-08-14
# Author: Varvara Efremova
#
# Description:
# Abstract base class defining slot structure
# =============================================================================
from .slot import SlotBase

import numpy as np

class Array3DSlot(SlotBase):
    def __init__(self, length):
        self.__value = np.zeros((length, 3))

    def value_getter(self):
        return self.__value

    def value_setter(self, value):
        self.__value = value

    value = property(value_getter, value_setter)
