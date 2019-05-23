#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

"""A module that contains a class for handing input from controller."""

from evdev import InputDevice, categorize, ecodes, util

_XBOX_BTNS = {
    304: 'BTN_A',
    305: 'BTN_B',
    307: 'BTN_X',
    308: 'BTN_Y',
    314: 'BTN_SELECT',
    315: 'BTN_START',
    316: 'BTN_MODE', # Home Button
    16: "DPAD_H", # DPAD vertical 1 for DOWN
    17: 'DPAD_V', # DPAD horizontal 1 for RIGHT
    5: 'TRG_RIGHT', # Right Trigger
    311: 'BTN_RB', # Right Bumper
    2: 'TRG_LEFT', # Left Trigger
    310: 'BTN_LB', # Left Bumper
    3: 'JOYS_RIGHT_H', # RIGHT is positive
    4: 'JOYS_RIGHT_V', # DOWN is positive
    0: 'JOYS_LEFT_H', # RIGHT is positive
    1: 'JOYS_LEFT_V' # DOWN is positive
    }

class Controller:
    def read(self):
        """Get input from the controlelr."""

        for event in self._device.read_loop():
            if event.type in (ecodes.EV_ABS, ecodes.EV_KEY):
                yield (util.resolve_ecodes(self._keys, [event.code])[0][0], event.value)

    def pressed(self):
        """Returns currently pressed down buttons."""

    def __init__(self, device):
        self._device = InputDevice(device)
        self._keys = _XBOX_BTNS
