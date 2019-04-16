#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

import yaml

class Operator:

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
        pass

    def __init__(self, connection, device, layout):

        self._connection = connection
        self._device = device
        self._layout = self._load_layout(layout)
