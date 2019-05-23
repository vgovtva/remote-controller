#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si

import shlex
import subprocess as sp
from threading import Thread

def _reader(f, b):
    """f - Stream to read. b - buffer to write values to."""
    while True:
        line = f.readline()
        if line:
            b.append(line)
        else:
            break


class Proc:
    """A wrapper class to manage subprocesses."""

    def _buffer_output(self):
        """Start a thread that collects output from stdout."""

        thread = Thread(target=_reader, args=(self.stdout, self._buffer))

        thread.daemon = True
        thread.start()

    def get_last_line(self):
        """Get last line written by 'self.proc' in stdout."""

        stdout = list(self._buffer)
        if stdout:
            self._buffer.clear()
        else:
            return None

        return str(stdout[-1]) if stdout[-1] else None

    def keep_alive(self, errout=False):
        """
        Check if the process is still alive if it is not, restart it. If 'errout' is 'True' do
        not restart the process and raise error instead.
        """

        if not self.alive():
            if errout:
                raise Exception("process running '%s' died with following error:\n%s" %
                                (self._cmd[0], str(self.stderr.read())))

            self.__init__(" ".join(self._cmd))

    def alive(self):
        """Check whether the process is still alive."""

        return True if not self.proc.poll() else False

    def __init__(self, cmd):
        """
        Init method for Proc object. This object is used to control asyncronous processes.
        cmd - a string which represents the command to run.
        """

        self.cmd = None
        self.proc = None
        self.stdout = None
        self.stdin = None
        self.stderr = None
        self._buffer = []

        # Validate input arguments.
        if not isinstance(cmd, str):
            raise Exception("invalid input argument type")

        self._cmd = shlex.split(cmd)
        self.proc = sp.Popen(self._cmd, stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
        self.stdout = self.proc.stdout
        self.stdin = self.proc.stdin
        self.stderr = self.proc.stderr
        self.kill = lambda: self.proc.kill()

        # This code is necessary for non-blocking read from other processes
        self._buffer_output()
