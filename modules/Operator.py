#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

import yaml
from modules import actionset


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

        print(layout)
        return layout

    def run(self):
        """Read device input and send it."""
#        self._connection.send("hello there")
        mode = 1
        for code, value in self._device.read():
            func_name = self._get_action(code, mode)
            func = self.actions.get(func_name, actionset.nothing) if func_name else actionset.nothing
            ret = func(value)

    def __init__(self, connection, device, layout):

        self._connection = connection
        self._device = device
        self._layout = self._load_layout(layout)
        self.actions = {}

        self.actions = {func:getattr(actionset, func) for func in dir(actionset) if _is_action(func)}
