#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 1.0, 20170415, Harry van der Wolf

import os, sys, platform, subprocess, time

# python helper scripts
import jrfunctions # General functions and tweaks
import sysoptions # Script for the rooting and so on
import sofiaserver # Script for the SofiaServer mods
import radio_mods # Script for the radio_mods


if sys.version_info<(3,0,0):
	# Fall back to Python 2's urllib2
	from urllib2 import urlopen
else:
	# For Python 3.0 and later
	from urllib.request import urlopen

###################################################
# Some intital variables
# Use dictionary for our variables, makes it easier to structure this script into functions (if I feel it is necessary :) )
glob_vars = {}

VERSION ="v0.1 15 April 2017"
OSplatform = platform.system()
glob_vars['PROGRAM_NAME'] = "Joying Intel Root assistant version " + VERSION + " on " + OSplatform


# Initialize file paths
realfile_dir  = os.path.dirname(os.path.abspath(__file__))
#glob_vars['BASE_DIR'] = os.path.join(realfile_dir, "..")
glob_vars['BASE_DIR'] = os.path.abspath(os.path.join(__file__ ,"../.."))
glob_vars['RESOURCES'] = os.path.join(glob_vars['BASE_DIR'],"resources")
if (OSplatform == "Windows") | (OSplatform == "nt"):
	glob_vars['adb'] = os.path.join(glob_vars['BASE_DIR'],"win-adb", "adb.exe")
else:
	glob_vars['adb'] = "adb"
#print(glob_vars['RESOURCES']
#print(glob_vars['adb']
#import time
#time.sleep(5)

# Set variable that subscripts can check
glob_vars['MAINSCRIPT'] = "YES"
###################################################
###################################################
def JRASSIST_ACCEPT():
	# set window title specific to this section
	title = glob_vars['PROGRAM_NAME'] + " disclaimer"
	jrfunctions.clr_scr()
	#print(our default header
	print("  READ ME:")
#	print(40 * "=" , "MENU" , 40 * "="
	print(87 * "=")
	print("  " + glob_vars['PROGRAM_NAME'])
	print("\n  standard disclaimer:")
	print("               WITH GREAT POWER COMES GREAT RESPONSIBILITY.\n")
	print("                 by proceeding you accept that this")
	print("                 script is carried out at your own risk")
	print("                 and you will not hold anyone else")
	print("                 but yourself responsible.\n")
	print("               WITH GREAT POWER COMES GREAT RESPONSIBILITY.")
	print('\n\n  . type " accept " without quotes to continue . . .')
	print("\n  . any other input will cancel and close this window\n") 
	print(87 * "=")
	#choice = raw_input("\n\nWhat's it gonna be boy? What's it gonna be?\n                                (Meatloaf, Paradise by the dashboard light, 1977)\n\n")
	choice = jrfunctions.input_cmd("\n")
	# the only accepted answer to continue
	if choice == "accept":
		jrfunctions.ext_cmd(glob_vars['adb'] + ' kill-server ')
		jrfunctions.ext_cmd(glob_vars['adb'] + ' connect ' + IP_ADDRESS)
		jrfunctions.ext_cmd(glob_vars['adb'] + ' root')
		jrfunctions.ext_cmd(glob_vars['adb'] + ' connect ' + IP_ADDRESS)
		OPTION_SELECTION()
	else:
		# we always want to use our close tool to exit the toolKIT
		# so we remap commonly used commands for exiting
		#if (choice == "e" ) | ( choice == "q" ) | ( choice == "exit" ) | ( choice == quit ):
		#	CLOSE_TOOL()
		#else:
		#	JRASSIST_ACCEPT()
		CLOSE_TOOL()

def OPTION_SELECTION():
	#clear
	# set window title specific to this section
	title = glob_vars['PROGRAM_NAME']
	#print(our default header
	jrfunctions.clr_scr()
#	print(40 * "=" , "MENU" , 40 * "="
	print(87 * "=")
	print("  " + glob_vars['PROGRAM_NAME'])
	print(87 * "=")
	print("  Select an Option (1-7) :") 
	print("\n   1 . Root, add SElinux policies and the SuperSU apk (version 2.79 SR3)")
	print("\n\n   2 . Install one of the NoKill/Steering-wheel-mod Sofia-1-C9-Server-V1.0.apk")
	print("\n\n   3 . Install modified stock bluetooth app to allow connection to all devices")
	print("\n\n   4 . Install one of the modified Radio apps")
	print("\n\n   5 . Alter the screen density; fake other android device, etc.")
	print("\n\n   6 . Update buggy busybox v1.22 with correct busybox v1.26-2")
	print("\n\n   7 . Exit this script")
	print(87 * "=")

	choice = jrfunctions.input_cmd('Enter your choice [1-7] : ')
	### Convert string to int type ##
	choice = int(choice)
	if choice == 1:
		sysoptions.init(glob_vars)
		OPTION_SELECTION()
	elif choice == 2:
		sofiaserver.init(glob_vars)
		OPTION_SELECTION()
	elif choice == 3:
		bt_selection(glob_vars)
		OPTION_SELECTION()
	elif choice == 4:
		radio_mods.init(glob_vars)
		OPTION_SELECTION()
	elif choice == 5:
		tweaks.menu(glob_vars)
		OPTION_SELECTION()
	elif choice == 6:
		jrfunctions.push_BUSYBOX(glob_vars)
		OPTION_SELECTION()
	elif choice == 7:
		CLOSE_TOOL()
	else:
		OPTION_SELECTION()
###################################################
def  CLOSE_TOOL():
	jrfunctions.clr_scr()
#	print(40 * "=" , "MENU" , 40 * "="
	print(87 * "=")
	print("   " + glob_vars['PROGRAM_NAME'])
	print( 87 * "=")
	#adb kill-server
	print("\n\n             The adb server has been stopped.\n\n")
	print("     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("     !!!!!                                    !!!!!")
	print("     !!!!!    REBOOT YOUR JOYING HEAD UNIT    !!!!!")
	print("     !!!!!                                    !!!!!")
	print("     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
	sys.exit()
###################################################
###################################################
# Set terminal size
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=100))

#check for ip-address
if len(sys.argv) < 2:
	print('\n\n  No ip-address given. I need the ip-address. Restart the script with "./jrassist.sh ip-address".')
	print('\n  like ./jrassist.sh 192.168.178.50\n\n')
	sys.exit()
else:
	IP_ADDRESS = sys.argv[1]

JRASSIST_ACCEPT()