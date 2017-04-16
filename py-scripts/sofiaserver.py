# -*- coding: utf-8 -*-

# sofiaserver.py - This python "helper" script deals with the several Sofiaserver.apk options

# Copyright (c) 2017 Harry van der Wolf. All rights reserved.

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public Licence as published
# by the Free Software Foundation, either version 2 of the Licence, or
# version 3 of the Licence, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public Licence for more details.

# This file is part of jrassist.


import os, platform, sys, subprocess, time
import jrfunctions

###################################################
# Variables for this script
SCRIPT_VERSION="v0.1 16 April 2017"
SCRIPT_NAME="Joying SofiaServer Mods subscript, version " + SCRIPT_VERSION

###################################################
###################################################

def init(glob_vars):
	jrfunctions.clr_scr()
	if glob_vars['MAINSCRIPT'] == "YES":
		MENU(glob_vars)
	else:
		jrfunctions.clr_scr()
		print("\n\nThis script can only be called from the main jrassist.bat or jrassist.sh script\n\n")
		jrfunctions.input_cmd("Press enter to exit\n\n")
		sys.exit()


