#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

def accelarate(val):

    return {"speed": int((val/1024)*127)}

def breaking(val):

    return {"speed": 0}

def turn(val):

    return {"steer": int(-(val/32768)*127)}

def nothing(val):
    """Default function. Does nothing."""

    return {}

def lights_on(val):

    if val:
        return{"lights": 1}
    return {}

def hello_world(val):
    """Hellow world function."""

    if val:
        print("hello world!")
    return {}
