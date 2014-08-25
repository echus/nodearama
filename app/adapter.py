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

from .modules.observe import Observer

class Adapter(Observer):
    def notify(self, observable, *args, **kwargs):
        for a in args:
            print("Got", a, "from", observable)
        return
