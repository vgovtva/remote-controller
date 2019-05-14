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

class Operator:

    def _get_action(self, code, mode, default=None):
        """
        Get the name of function from layout based on button 'code' and current 'mode' the layout is in.
        """

        binds = self._layout.get(code, None)
        return binds.get(mode, None) if binds else default

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
            func_name = self._get_action(code, mode, default="action_not_found")
            func = getattr(self.actions, func_name, actionset.nothing)
            ret = func(value)
            self._connection.send(self._protocol.to_bytes(self.actions.state))

    def __init__(self, connection, device, protocol, layout):

        self._connection = connection
        self._device = device
        self._protocol = protocol
        self._layout = self._load_layout(layout)
        self._state = _create_null_state()
        self.actions = actionset.Basic()
