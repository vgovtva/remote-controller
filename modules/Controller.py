#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

"""A module that contains a class for handing input from controller."""

from evdev import InputDevice, categorize, ecodes

class Controller:
    def read(self):
        """Get input from the controlelr."""

        for event in self._device.read_loop():
            if event.type in (ecodes.EV_ABS, ecodes.EV_KEY):
                yield (event.code, event.value)


    def __init__(self, device):
        self._device = InputDevice(device)
