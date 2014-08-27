# =============================================================================
# (C) Copyright 2014
# Australian Centre for Microscopy & Microanalysis
# The University of Sydney
# =============================================================================
# File:   observe.py
# Date:   2014-08-25
# Author: Varvara Efremova
#
# Description:
# Simple implementation of the observer pattern
# Taken from http://en.wikipedia.org/wiki/Observer_pattern
# =============================================================================

import abc

class Observable:
    def __init__(self):
        self.__observers = []

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

class Observer:
    __metaclass__ = abc.ABCMeta

    def __init__(self, observable):
        observable.register_observer(self)

    @abc.abstractmethod
    def notify(self, observable, *args, **kwargs):
        return
