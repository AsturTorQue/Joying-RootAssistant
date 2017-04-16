# -*- coding: utf-8 -*-

# py - This python "helper" script deals with the several Sofiaserver.apk options

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

def ext_cmd(cmd):
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	(output, err) = process.communicate()
	process.wait()
	print output
	#if (err != "") | (err != "None") | (err != None):
	#	print err

def input_cmd(Message):
	# raw_input has been changed to input in python > 3
	if sys.version_info<(3,0,0):
		choice = raw_input(Message)
	else:
		choice = input(Message)

	return choice

def push_BUSYBOX(glob_vars):
	print(chr(27) + "[2J") 
	print("\n\n    Updating your busybox.\n\n")
	#time.sleep(5)
	ext_cmd(glob_vars['adb'] + ' push WORKINGDIR/resources/busybox /sdcard/')
	ext_cmd(glob_vars['adb'] + ' shell "su -c mount -o remount,rw /system"')
	ext_cmd(glob_vars['adb'] + ' shell "su -c cp /system/bin/busybox /system/bin/busybox.org"')
	ext_cmd(glob_vars['adb'] + ' shell "su -c cp /sdcard/busybox /system/bin/busybox"')
	ext_cmd(glob_vars['adb'] + ' shell "su -c chmod 0755 /system/bin/busybox"')
	ext_cmd(glob_vars['adb'] + ' shell "su -c mount -o remount,ro /system"')
	ext_cmd(glob_vars['adb'] + ' shell "su -c ls -l /system/bin/busy*"')
	input_cmd("\n\nPress any key to return to main menu\n\n")
		
