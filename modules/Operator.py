#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

class Operator:

    def run(self):
        """Read device input and send it."""
        pass

    def __init__(self, connection, device):

        self._connection = connection
        self._device = device
