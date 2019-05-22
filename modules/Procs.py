#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

import shlex
import subprocess as sp
from threading import Thread

def _reader(f,buffer):
    while True:
        line=f.read()
        if line:
            buffer.append(line)
        else:
            break


class Proc:
    """A wrapper class to manage subprocesses."""

    def _buffer_output(self):
        """Start a thread that collects output from stdout."""

        thread = Thread(target=_reader, args=(self.stdout, self._buffer))

        thread.daemon=True
        thread.start()

    def get_last_line(self, timeout=None):

        stdout = list(self._buffer)
        if stdout:
            self._buffer=[]
        else:
            return None

        return str(stdout[-1]) if stdout[-1] else None

    def __init__(self, cmd):
        """
        Init method for Proc object. This object is used to control asyncronous processes.
        cmd - a string which represents the command to run.
        """

        self.proc = None
        self.stdout = None
        self.stdin = None
        self.stderr = None
        self._buffer = []

        # Validate input arguments.
        if not isinstance(cmd, str):
            raise Exception("invalid input argument type")

        self.proc = sp.Popen(shlex.split(cmd), stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE)
        self.stdout = self.proc.stdout
        self.stdin = self.proc.stdin
        self.stderr = self.proc.stderr

        # This code is necessary for non-blocking read from other processes
        self._buffer_output()
