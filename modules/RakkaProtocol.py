#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

"""A module that contains a class for converting a dict to Rakkatec protocol."""

from collections import OrderedDict

# TODO: This struct does not hold any information about the type of data in each byte. This is
# something that should be added. Otherwise signed values will not make any sense.
_RECEIVE_STRUCT= OrderedDict([
        ("RPM", [0,1]),
        ("oil_pressure", [2]),
        ("eng_temp", [3]),
        ("hydro_oil_temp", [4]),
        ("hydre_oil_level", [5]),
        ("fuel", [6]),
        ("battary_voltage", [7]),
        ("main_boom_h_ang", [8]),
        ("main_boom_v_ang", [9]),
        ("excavation_boom_ang", [10]),
        ("scoop_ang", [11]),
        ("main_boom_ang", [12]),
        ("zoom_pos", [13]),
        ("locks_open", [14]),
        ("locks_closed", [15]),
        ("fork_tilt", [16]),
        ("body_roll", [17]),
        ("body_pitch", [18]),
        ("steer_ang", [19]),
        ("traveled_distance", [20,21]),
        ("speed", [22,23]),
])

def _int_to_bytes(x):
    """Covert an integer to byte."""
    if abs(x) > 127:
        raise "Value '%s' exceeds signed int range. The range is -127 to 127." % x
    num = x if x >= 0 else (256 + x)
    return bytes([num])

def _bool_to_bytes(x):
    """Covert a bool to byte."""

    return bytes([True if x else False])

class RakkaProtocol:

    @staticmethod
    def to_bytes(control_dict):
        """
        A method that converts a dictionary with control intructions/values to a bytes object to
        control Rakka 3000 vehicle.
        """
        msg = []
        msg.append(_int_to_bytes(control_dict.get("speed", 0)))
        msg.append(_int_to_bytes(control_dict.get("steer", 0)))
        msg.append(_int_to_bytes(control_dict.get("wheel-raise", 0)))
        msg.append(_int_to_bytes(control_dict.get("chasis-turn", 0)))
        msg.append(_int_to_bytes(control_dict.get("chasis-bend", 0)))
        msg.append(_int_to_bytes(control_dict.get("lfw-raise", 0)))
        msg.append(_int_to_bytes(control_dict.get("rfw-raise", 0)))
        msg.append(_int_to_bytes(control_dict.get("lrw-raise", 0)))
        msg.append(_int_to_bytes(control_dict.get("rrw-raise", 0)))
        msg.append(bytes([control_dict.get("gear", 0)]))
        msg.append(bytes([control_dict.get("floatation", 0)]))
        msg.append(_bool_to_bytes(control_dict.get("engine-pwr", 0)))
        msg.append(bytes([0, 0])) # RPM control, documentation is not clear.
        msg.append(_bool_to_bytes(control_dict.get("engine-pre-heat", 0)))
        msg.append(_int_to_bytes(control_dict.get("boom-hor", 0)))
        msg.append(_int_to_bytes(control_dict.get("boom-vert", 0)))
        msg.append(_int_to_bytes(control_dict.get("exc", 0)))
        msg.append(_int_to_bytes(control_dict.get("scoop", 0)))
        msg.append(_int_to_bytes(control_dict.get("claw", 0)))
        msg.append(_int_to_bytes(control_dict.get("hook-lift", 0)))
        msg.append(_int_to_bytes(control_dict.get("hook-extnd", 0)))
        msg.append(bytes([control_dict.get("hook-lock", 0)]))
        msg.append(_int_to_bytes(control_dict.get("fork-lift", 0)))
        msg.append(_int_to_bytes(control_dict.get("fork-claw", 0)))
        msg.append(bytes([control_dict.get("lights", 0)]))

        return b''.join(msg)

    @staticmethod
    def decipher(msg):
        """Decipher a message sent by Rakka vehicle. Return a dict with '{parameter: value}'."""
        content = {}

        for key, idx in _RECEIVE_STRUCT.items():
            content[key] = int.from_bytes([msg[i] for i in idx], byteorder='big')

        return content
