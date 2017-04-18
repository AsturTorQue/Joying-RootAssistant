#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 1.0, 20170415, Harry van der Wolf

import os, sys, platform, subprocess, shutil, time

# python helper scripts
import jrfunctions # General functions and tweaks
import sysoptions # Script for the rooting and so on
import sofiaserver # Script for the SofiaServer mods
import radio_mods # Script for the radio_mods
import bluetooth # Script for the several bluetooth mods
import credits # Contains the credits for all the persons who contributed

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
glob_vars['TMP_DIR'] = os.path.join(glob_vars['BASE_DIR'],"tmp")
glob_vars['BASE_REPO_URL'] = "https://github.com/hvdwolf/Joying-RootAssistant/blob/python_branch/"

if (OSplatform == "Windows") | (OSplatform == "nt"):
	glob_vars['adb'] = os.path.join(glob_vars['BASE_DIR'],"win-adb", "adb.exe")
else:
	glob_vars['adb'] = "adb"


# Set variable that subscripts can check. We don't want users to start a subscript
glob_vars['MAINSCRIPT'] = "YES"
# Set variable for dry_run. This is for test purposes and the scripts
# will do everything except connecting to the head unit
glob_vars['DRY_RUN'] = "NO"

###################################################
###################################################
def JRASSIST_ACCEPT(glob_vars):
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
		if glob_vars['DRY_RUN'] == "NO":
			jrfunctions.adb_cmd(glob_vars, ' kill-server ')
			jrfunctions.adb_cmd(glob_vars, ' connect ' + IP_ADDRESS)
			jrfunctions.adb_cmd(glob_vars, ' root')
			jrfunctions.adb_cmd(glob_vars, ' connect ' + IP_ADDRESS)
		else:
			jrfunctions.clr_scr()
			print("\n\nDRY_RUN is set to YES. This is for testing\nNo connection will be made to the head unit!\n\n")
			choice = jrfunctions.input_cmd("Press enter to continue\n")
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
	print("\n\n   3 . Install Bluetooth mods and helper apps")
	print("\n\n   4 . Install one of the modified Radio apps")
	print("\n\n   5 . Alter the screen density; fake other android device, etc.")
	print("\n\n   6 . Update buggy busybox v1.22 with correct busybox v1.26-2")
	print("\n\n   7 . CREDITS: Who contributed all to these mods.")
	print("\n\n   8 . Exit this script")
	print(87 * "=")

	choice = jrfunctions.input_cmd('Enter your choice [1-8] : ')
	### Convert string to int type ##
	choice = int(choice)
	if choice == 1:
		sysoptions.init(glob_vars)
		OPTION_SELECTION()
	elif choice == 2:
		sofiaserver.init(glob_vars)
		#NOT_IMPLEMENTED_YET()
		OPTION_SELECTION()
	elif choice == 3:
		bluetooth.init(glob_vars)
		OPTION_SELECTION()
	elif choice == 4:
		radio_mods.init(glob_vars)
		OPTION_SELECTION()
	elif choice == 5:
		NOT_IMPLEMENTED_YET()
		#tweaks.menu(glob_vars)
		OPTION_SELECTION()
	elif choice == 6:
		jrfunctions.push_BUSYBOX(glob_vars)
		OPTION_SELECTION()
	elif choice == 7:
		jrfunctions.clr_scr()
		print(credits.CREDITS)
		jrfunctions.input_cmd("\n\nPress enter to return to the main menu\n\n")
		OPTION_SELECTION()
	elif choice == 8:
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
	print("\n\n                  The adb server has been stopped.\n\n")
	print("          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("          !!!!!                                    !!!!!")
	print("          !!!!!    REBOOT YOUR JOYING HEAD UNIT    !!!!!")
	print("          !!!!!                                    !!!!!")
	print("          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
	print(87 * "=")
	print("\n\n")
	# remove tmp folder recursively
	shutil.rmtree( glob_vars['TMP_DIR'] )
	sys.exit()

def NOT_IMPLEMENTED_YET():
	jrfunctions.clr_scr()
	print("\n\n          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("          !!!!!                                    !!!!!")
	print("          !!!!!        Not implemented yet         !!!!!")
	print("          !!!!!                                    !!!!!")
	print("          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
	jrfunctions.input_cmd("Press enter to return to the main menu\n\n")

def TOOL_MISSING(tool):
	jrfunctions.clr_scr()
	print("\n\n          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	print("\n\n             " + tool + " is missing! Please install first!")
	print("\n\n          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
	jrfunctions.input_cmd("Press enter to exit this script\n\n")
	sys.exit()

###################################################
###################################################
# This is the "main" part
if __name__ == '__main__' :
	# Set terminal size
	if (OSplatform == "Windows") | (OSplatform == "nt"):
		os.system("mode con:cols=100 lines=32")
	else:
		sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=100))

	#check for ip-address
	if len(sys.argv) < 2:
		print('\n\n  No ip-address given. I need the ip-address. Restart the script with "./jrassist.sh ip-address".')
		print('\n  like ./jrassist.sh 192.168.178.50\n\n')
		sys.exit()
	else:
		IP_ADDRESS = sys.argv[1]

	# check if DRY_RUN has been specified. Overrules script value
	if len(sys.argv) >= 2:
		if sys.argv[2] == "DRY_RUN":
			glob_vars['DRY_RUN'] = "YES"

	# Make tmp folder if it doesn't exist
	if not os.path.isdir(glob_vars['TMP_DIR']):
		os.makedirs(glob_vars['TMP_DIR'])

	# Check if adb is available on linux/*BSD/Mac OS/X
	if not jrfunctions.check_for_program('adb'):
		TOOL_MISSING('adb')

	JRASSIST_ACCEPT(glob_vars)