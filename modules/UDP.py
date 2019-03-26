#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

class UDP:
    def __init__(self, ip, port):
        """Class init method."""
        self.UDP_IP = ip
        self.UDP_PORT = port

        # self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, msg):
        """Send message through UPD."""

        # self.socket.sendto(msg, (UDP_IP, UDP_PORT))
        pass
