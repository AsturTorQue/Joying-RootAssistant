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

import os, sys, subprocess

#glob_vars['PROGRAM_NAME']

SCRIPT_VERSION="v0.1 16 April 2017"
SCRIPT_NAME="Joying root the unit subscript, version " + SCRIPT_VERSION

def init(glob_vars):
	print(chr(27) + "[2J")
	if glob_vars['MAINSCRIPT'] == "YES":
		MENU(glob_vars)
	else:
		print(chr(27) + "[2J")
		print "\n\nThis script can only be called from the main jrassist.sh script\n\n"
		pause_cmd
		print "\n\n"
		sys.exit()


def MENU(glob_vars):
	print(chr(27) + "[2J")
	print 87 * "="
	print "  " + glob_vars['PROGRAM_NAME']
	print "  " + SCRIPT_NAME
	print 87 * "="
	print "\n   This script will root your unit in a better way and add the SuperSU superuser apk\n\n"
	print "  Select an Option :" 
	print "\n   1 . Root my unit with SuperSU 2.79 SR3"
	print "\n   2 . Do nothing and exit this subscript."
	print 87 * "="
	choice = raw_input("")
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
	self.ext_cmd(glob_vars['adb'] + ' shell mount -o rw,remount /system')
	self.ext_cmd(glob_vars['adb'] + ' shell mount -o rw,remount /system /system')
	self.ext_cmd(glob_vars['adb'] + ' shell mount -o rw,remount /')
	self.ext_cmd(glob_vars['adb'] + ' shell mount -o rw,remount / /')

	# Make some temporary folders
	self.ext_cmd(glob_vars['adb'] + ' shell "mkdir /tmp"')
	self.ext_cmd(glob_vars['adb'] + ' shell "mkdir /tmp/supersu"')

	# Do the copying
	#print "\n$FILEPATH\n\n"
	self.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/chattr.pie /tmp/supersu/')
	self.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/install.sh /tmp/supersu/')
	self.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/install-recovery.sh /tmp/supersu/')
	self.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/libsupol.so /tmp/supersu/')
	self.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/su.pie /tmp/supersu/')
	self.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/Superuser.apk /tmp/supersu/')
	self.ext_cmd(glob_vars['adb'] + ' push $FILEPATH/supolicy /tmp/supersu/')

	# Do the actual installation
	self.ext_cmd(glob_vars['adb'] + ' shell chmod 0755 /tmp/supersu/install.sh')
	self.ext_cmd(glob_vars['adb'] + ' shell "cd /tmp/supersu/ && sh install.sh"')

	# Clean up
	self.ext_cmd(glob_vars['adb'] + ' shell rm -rf /tmp/supersu')
	self.ext_cmd(glob_vars['adb'] + ' shell mount -o ro,remount /system')
	self.ext_cmd(glob_vars['adb'] + ' shell mount -o ro,remount /')
	#read -n 1 -s -p "Press any key to exit this script and return to the main script"
	pause_cmd()



