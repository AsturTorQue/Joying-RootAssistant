# -*- coding: utf-8 -*-

# bluetooth.py - This python "helper" script deals with the several bluetooth mods and improvements

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
SCRIPT_NAME="Joying Bluetooth Mods subscript, version " + SCRIPT_VERSION

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

def MENU(glob_vars):
	jrfunctions.clr_scr()
	print(87 * "=")
	print("  " + glob_vars['PROGRAM_NAME'])
	print("  " + SCRIPT_NAME)
	print(87 * "=")
	print("  Select an Option :")
	print("\n   1 . Install BlueBalls.apk: enables bluetooth options in settings")
	print("\n\n   2 . Install BluetoothTetering: BT tetering between your unit and phone")
	print("\n\n   3 . Install modded Bluetooth apk: enables coupling to all BT devices")
	print("\n\n   4 . Exit this Bluetooth mods subscript")
	print(87 * "=")
	choice = jrfunctions.input_cmd("")
	### Convert string to int type ##
	choice = int(choice)
	if choice == 1:
		INSTALL_MOD(glob_vars, 'BlueBalls')
	elif choice == 2:
		INSTALL_MOD(glob_vars, 'BTTethering')
	elif choice == 3:
		INSTALL_MOD(glob_vars, 'modBT')
	elif choice == 4:
		return
	else:
		MENU(glob_vars)


def INSTALL_MOD(glob_vars, SELECTED_MOD):
	jrfunctions.clr_scr()

