# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si
#
# Author: Vladislav Govtva<vlad.govtva@gmail.com>

"""The standard python packaging script. Not all of the requirement are listed here. Only those
which are possible to install via pip. There are many more packages which were installed via
'apt-get'. Unfortunatelly, which ones were not tracked."""

import re
from setuptools import setup, find_packages

setup(
    name="project-name",
    description="Tools to control server power lab resources",
    author="Vladislav Govtva",
    author_email="vlad.govtva@gmail.com",
    version="0.2",
    scripts=["remote-controller", "remote-receiver"],
    packages=find_packages(exclude=["test*"]),
    license="GPLv2",
    install_requires=["argcomplete", "evdev", "PyYAML", "opencv-python", "imutils",
                      "opencv-contrib-python"], # dependencies
    long_description="""This collection of tools is made for controlling an autonmous vehicle.""")

