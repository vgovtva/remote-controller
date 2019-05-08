# -*- coding: utf-8 -*-
# vim: ts=4 sw=4 tw=100 et ai si
#
# License: GPLv2
# Author: Vladislav Govtva<vlad.govtva@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""The standard python packaging script."""

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
    install_requires=["argcomplete", "evdev", "PyYAML"], # dependencies
    long_description="""This collection of tools is made for controlling an autonmous vehicle Rakka
                        3000. """)

