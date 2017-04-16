# -*- coding: utf-8 -*-

# sysoptions.py - This python "helper" script deals with the several Sofiaserver.apk options

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

import os, platform, sys, subprocess
import jrfunctions

#glob_vars['PROGRAM_NAME']

SCRIPT_VERSION="v0.1 16 April 2017"
SCRIPT_NAME="Joying rooting subscript, version " + SCRIPT_VERSION

def init(glob_vars):
	jrfunctions.clr_scr()
	if glob_vars['MAINSCRIPT'] == "YES":
		MENU(glob_vars)
	else:
		jrfunctions.clr_scr()
		print("\n\nThis script can only be called from the main jrassist.bat or jrassist.sh script\n\n")
		jrfunctions.input_cmd("Press enter to exit this script\n\n")
		sys.exit()


def MENU(glob_vars):
	jrfunctions.clr_scr()
	print(87 * "=")
	print("  " + glob_vars['PROGRAM_NAME'])
	print("  " + SCRIPT_NAME)
	print(87 * "=")
	print("\n   This script will root your unit in a better way and add the SuperSU superuser apk\n\n")
	print("  Select an Option :")
	print("\n   1 . Root my unit with SuperSU 2.79 SR3")
	print("\n   2 . Do nothing and exit this subscript.")
	print(87 * "=")
	choice = jrfunctions.input_cmd("")
	### Convert string to int type ##
	choice = int(choice)
	if choice == 1:
		ROOT_IT(glob_vars)
	elif choice == 2:
		return
	else:
		MENU(glob_vars)


def ROOT_IT(glob_vars):
	# Make the partitions read-writable
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell mount -o rw,remount /system')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell mount -o rw,remount /system /system')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell mount -o rw,remount /')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell mount -o rw,remount / /')

	# Make some temporary folders
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell "mkdir /tmp"')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell "mkdir /tmp/supersu"')

	# Do the copying
	#print("\n$FILEPATH\n\n"
	jrfunctions.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/chattr.pie /tmp/supersu/')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/install.sh /tmp/supersu/')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/install-recovery.sh /tmp/supersu/')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/libsupol.so /tmp/supersu/')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/su.pie /tmp/supersu/')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/Superuser.apk /tmp/supersu/')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/supolicy /tmp/supersu/')

	# Do the actual installation
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell chmod 0755 /tmp/supersu/install.sh')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell "cd /tmp/supersu/ && sh install.sh"')

	# Clean up
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell rm -rf /tmp/supersu')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell mount -o ro,remount /system')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell mount -o ro,remount /')
	#read -n 1 -s -p "Press any key to exit this script and return to the main script"
	jrfunctions.input_cmd("\n\nPress enter to exit this script and return to the main script\n\n")



