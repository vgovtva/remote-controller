#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

"""This module contains a class that implements the logic of the main loop of remote cotrol."""

import yaml
from modules import actionset

def _create_null_state():
    """A helper function of creating the inital state of the machine, with everything set to 0."""

    state = {}

    return state

def _is_action(func_name):
    """Helper function to check action is out of 'actionset'."""

    func = getattr(actionset, func_name, None)
    if not func:
        return False
    return callable(func) and func.__module__ == actionset.__name__

class Operator:

    def _get_action(self, code, mode):
        """
        Get the name of function from layout based on button 'code' and current 'mode' the layout is in.
        """

        binds = self._layout.get(code, None)
        return binds.get(mode, None) if binds else None

    def _load_layout(self, path):
        """load the layout configuration for the controller."""

        with open(path, 'r') as fobj:
            try:
                layout = yaml.safe_load(fobj)
            except Exception as err:
                raise Exception("\nissue loading the layout file at '%s':\n%s" % (path, err))

        return layout

    def run(self):
        """Read device input and send it."""
        mode = 1
        for code, value in self._device.read():
            func_name = self._get_action(code, mode)
            func = self.actions.get(func_name, actionset.nothing) if func_name else actionset.nothing
            ret = func(value)
            self._connection.send(self._protocol.to_bytes(ret))

    def __init__(self, connection, device, protocol, layout):

        self._connection = connection
        self._device = device
        self._protocol = protocol
        self._layout = self._load_layout(layout)
        self._state = _create_null_state()
        self.actions = {func:getattr(actionset, func) for func in dir(actionset) if _is_action(func)}
