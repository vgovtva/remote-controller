#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

import sys

def nothing(val):
    """Default function. Does nothing."""
    pass

class Basic:
    """A basic action set of Rakka vehicle."""

    def accelarate(self, val):

        self.state["speed"] = int((val/1024)*127)

    def breaking(self, val):

        return {"speed": 0}

    def turn(self, val):

        self.state["steer"] = int(-(val/32768)*127)

    def nothing(self, val):
        """Default function. Does nothing."""

        pass

    def lights_on(self, val):

        if val:
            self.state["lights"] = 1

    def hello_world(self, val):
        """Hello world function."""

        if val:
            sys.stdout.write("hello world!\n")
            sys.stdout.flush()

    def __init__(self):
        """Init method for class."""

        # Initialize class default state.
        self.state = {"speed": 0,
                      "steer": 0,
                      "wheel-raise": 0,
                      "chasis-turn": 0,
                      "chasis-bend": 0,
                      "lfw-raise": 0,
                      "rfw-raise": 0,
                      "lrw-raise": 0,
                      "rrw-raise": 0,
                      "gear": 0,
                      "floatation": 0,
                      "engine-pwr": 0,
                      "rpm": 0,
                      "engine-pre-heat": 0,
                      "boom-hor": 0,
                      "boom-vert": 0,
                      "exc": 0,
                      "scoop": 0,
                      "claw": 0,
                      "hook-lift": 0,
                      "hook-extnd": 0,
                      "hook-lock": 0,
                      "fork-lift": 0,
                      "fork-claw": 0,
                      "lights": 0}
