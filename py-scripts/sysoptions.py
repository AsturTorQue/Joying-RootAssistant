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
		DOWNLOAD_IT(glob_vars, "SuperSU")
		ROOT_IT(glob_vars, "SuperSU")
	elif choice == 2:
		return
	else:
		MENU(glob_vars)

def DOWNLOAD_IT(glob_vars, resourcesPath):
	base_url = "https://github.com/hvdwolf/Joying-RootAssistant/raw/master/SuperSU_for_Joying_Intel/resources/"
	SU_DIR = os.path.join(glob_vars['TMP_DIR'], resourcesPath)
	# Make resourcesPath folder if it doesn't exist
	if not os.path.isdir(SU_DIR):
		os.makedirs(SU_DIR)

	jrfunctions.clr_scr()
	print("\n\n          Downloading the latest files\n")
	jrfunctions.resource_download( glob_vars, SU_DIR, (base_url + "chattr.pie") )
	jrfunctions.resource_download( glob_vars, SU_DIR, (base_url + "install.sh") )
	jrfunctions.resource_download( glob_vars, SU_DIR, (base_url + "install-recovery.sh") )
	jrfunctions.resource_download( glob_vars, SU_DIR, (base_url + "libsupol.so") )
	jrfunctions.resource_download( glob_vars, SU_DIR, (base_url + "su.pie") )
	jrfunctions.resource_download( glob_vars, SU_DIR, (base_url + "Superuser.apk") )
	jrfunctions.resource_download( glob_vars, SU_DIR, (base_url + "supolicy") )
	print("\n\n          Finished downloading the latest files")
	print("          Continuing with the installation")



def ROOT_IT(glob_vars, resourcesPath):
	SU_DIR = os.path.join(glob_vars['TMP_DIR'], resourcesPath)
	# Make the partitions read-writable
	jrfunctions.adb_cmd(glob_vars, ' shell mount -o rw,remount /system')

	# Make some temporary folders
	jrfunctions.adb_cmd(glob_vars, ' shell "mkdir /sdcard/supersu"')

	# Do the copying
	#print("\n' + SU_DIR + '\n\n"
	jrfunctions.adb_cmd(glob_vars, ' push ' + os.path.join(SU_DIR, "chattr.pie") + ' /sdcard/supersu/')
	jrfunctions.adb_cmd(glob_vars, ' push ' + os.path.join(SU_DIR, "install.sh") + ' /sdcard/supersu/')
	jrfunctions.adb_cmd(glob_vars, ' push ' + os.path.join(SU_DIR, "install-recovery.sh") + ' /sdcard/supersu/')
	jrfunctions.adb_cmd(glob_vars, ' push ' + os.path.join(SU_DIR, "libsupol.so") + ' /sdcard/supersu/')
	jrfunctions.adb_cmd(glob_vars, ' push ' + os.path.join(SU_DIR, "su.pie") + ' /sdcard/supersu/')
	jrfunctions.adb_cmd(glob_vars, ' push ' + os.path.join(SU_DIR, "Superuser.apk") + ' /sdcard/supersu/')
	jrfunctions.adb_cmd(glob_vars, ' push ' + os.path.join(SU_DIR, "supolicy") + ' /sdcard/supersu/')

	# internal copy
	jrfunctions.adb_cmd(glob_vars, 'shell "su -c mkdir -p /data/supersu"')
	jrfunctions.adb_cmd(glob_vars, 'shell "su -c cp /sdcard/supersu/* /data/supersu/"')

	# Do the actual installation
	jrfunctions.adb_cmd(glob_vars, ' shell chmod 0755 /data/supersu/install.sh')
	jrfunctions.adb_cmd(glob_vars, ' shell "cd /data/supersu/ && sh install.sh"')

	# Clean up
	jrfunctions.adb_cmd(glob_vars, ' shell rm -rf /sdcard/supersu')
	jrfunctions.adb_cmd(glob_vars, ' shell rm -rf /data/supersu')
	jrfunctions.adb_cmd(glob_vars, ' shell sync')
	#read -n 1 -s -p "Press any key to exit this script and return to the main script"
	jrfunctions.input_cmd("\n\nPress enter to exit this script and return to the main script\n\n")



