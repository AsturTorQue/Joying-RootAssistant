# -*- coding: utf-8 -*-

# jrfunctions.py - This python "helper" script deals with the several Sofiaserver.apk options

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

def ext_cmd(cmd):
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	(output, err) = process.communicate()
	process.wait()
	print output

def pause_cmd():
	# very dirty method, but works always
	try:
		os.system('pause')  #windows, doesn't require enter
	except whatever_it_is:
		os.system('read -n 1 -s -p "Press any key to continue"') #linux, *bsd, mac OS/X


