# -*- coding: utf-8 -*-

# radio_mods.py - This python "helper" script deals with the several Radio mods

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
SCRIPT_NAME="Joying Radio Mods subscript, version " + SCRIPT_VERSION

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
	print("\n   1 . Install the BLUE_WHITE version")
	print("\n\n   2 . Install the RED_WHITE version")
	print("\n\n   3 . Install the RED version")
	print("\n\n   4 . Install the ORANGE version")
	print("\n\n   5 . Exit this radio mods subscript")
	print(87 * "=")
	choice = jrfunctions.input_cmd("")
	### Convert string to int type ##
	choice = int(choice)
	if choice == 1:
		INSTALL_MOD(glob_vars, 'BLUE_WHITE')
	elif choice == 2:
		INSTALL_MOD(glob_vars, 'RED_WHITE')
	elif choice == 3:
		INSTALL_MOD(glob_vars, 'RED')
	elif choice == 4:
		INSTALL_MOD(glob_vars, 'ORANGE')
	elif choice == 5:
		return
	else:
		MENU(glob_vars)


def INSTALL_MOD(glob_vars, SELECTED_MOD):
	jrfunctions.clr_scr()
	RADIO_MOD = os.path.join(glob_vars['BASE_DIR'], "Radio-Mod", SELECTED_MOD, "JY-1-C9-Radio-V1.0.apk")
	#print(RADIO_MOD
	#time.sleep(5)
	print("\n\n    Pushing the " + SELECTED_MOD + " version to your head unit\n\n")
	jrfunctions.ext_cmd(glob_vars['adb'] + ' push ' + RADIO_MOD + ' /sdcard/')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell "su -c am force-stop com.syu.radio"')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell "su -c mount -o remount,rw /system"')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell "su -c cp /system/app/JY-1-C9-Radio-V1.0/JY-1-C9-Radio-V1.0.apk /system/app/JY-1-C9-Radio-V1.0/JY-1-C9-Radio-V1.0.apk.old"')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell "su -c cp /sdcard/JY-1-C9-Radio-V1.0.apk /system/app/JY-1-C9-Radio-V1.0"')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell "su -c chmod 644 /system/app/JY-1-C9-Radio-V1.0/JY-1-C9-Radio-V1.0.apk"')
	jrfunctions.ext_cmd(glob_vars['adb'] + ' shell "su -c ls -l /system/app/JY-1-C9-Radio-V1.0"')
	jrfunctions.input_cmd("\n\nPress enter to exit this script and return to the main script\n\n")

