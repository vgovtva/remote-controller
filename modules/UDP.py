#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

import socket

class UDP:
    def __init__(self, ip, port):
        """Class init method."""

        self.UDP_IP = ip
        self.UDP_PORT = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((ip, port))

    def send(self, msg):
        """Send message through UDP."""

        self.sock.sendto(msg, (self.UDP_IP, self.UDP_PORT))

    def receive(self):
        """Receive a message through UDP."""

        return self.sock.recv(1024)
