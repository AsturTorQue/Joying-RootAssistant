# -*- coding: utf-8 -*-

# py - This python "helper" script contains general help files

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

###################################################
###################################################
def is_executable(fpath):
	return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

def check_for_program(program):
	exists = False
	for path in os.environ["PATH"].split(os.pathsep):
		path_plus_program = os.path.join(path, program)
		if is_executable(path_plus_program):
			#print "program " + program + " found"
			exists = True
	return exists


def clr_scr():
	OSplatform = platform.system()
	if (OSplatform == "Windows") | (OSplatform == "nt"):
		os.system('cls')
	else:
		os.system('clear')


def adb_cmd(glob_vars, cmd):
	cmd = glob_vars['adb'] + ' ' + cmd

	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	(output, err) = process.communicate()
	process.wait()
	print(output)
	# real connection errors
	conn_errors = ["unable to connect to ", "device offline"] 
	if any(conn_error in output for conn_error in conn_errors):
		clr_scr()
		#adb_cmd(glob_vars['adb'] + ' kill-server ')
		print("\n\n          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		print("          !!!!!                                                         !!!!!")
		print("          !!!!!      I CAN NOT CONNECT TO YOUR JOYING HEAD UNIT         !!!!!")
		print("          !!!!!                                                         !!!!!")
		print("          !!!!!       - Do you have the correct ip-address?             !!!!!")
		print("          !!!!!       - Are you on the same network?                    !!!!!")
		print("          !!!!!       - Can you ping your unit?                         !!!!!")
		print("          !!!!!       - After sleep mode WiFi can be unstable.          !!!!!")
		print("          !!!!!         Reboot your unit in that case!                  !!!!!")
		print("          !!!!!                                                         !!!!!")
		print("          !!!!!                                                         !!!!!")
		print("          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
		sys.exit()

	#if (err != "") | (err != "None") | (err != None):
	#	print(err)

def input_cmd(Message):
	# raw_input has been changed to input in python > 3
	if sys.version_info<(3,0,0):
		choice = raw_input(Message)
	else:
		choice = input(Message)

	return choice


# download function
def resource_download( glob_vars, local_path, file_url ):
	print("\nDownloading " + file_url.rsplit('/', 1)[-1])
	loc_file = urlopen( map_url )
	with open(os.path.join(glob_vars['BASE_DIR'], "resources", local_path),'wb') as output:
		output.write(loc_file.read())



###################################################
###################################################


def push_BUSYBOX(glob_vars):
	clr_scr() 
	print("\n\n    Updating your busybox.\n\n")
	#time.sleep(5)
	adb_cmd(glob_vars, ' push ' + os.path.join(glob_vars['BASE_DIR'], "busybox-X86", "busybox") + ' /sdcard/')
	adb_cmd(glob_vars, ' shell "su -c mount -o remount,rw /system"')
	adb_cmd(glob_vars, ' shell "su -c cp /system/bin/busybox /system/bin/busybox.org"')
	adb_cmd(glob_vars, ' shell "su -c cp /sdcard/busybox /system/bin/busybox"')
	adb_cmd(glob_vars, ' shell "su -c chmod 0755 /system/bin/busybox"')
	adb_cmd(glob_vars, ' shell "su -c mount -o remount,ro /system"')
	adb_cmd(glob_vars, ' shell "su -c ls -l /system/bin/busy*"')
	input_cmd("\n\nPress enter to return to main menu\n\n")
		
