# -*- coding: utf-8 -*-

# credits.py - This python "script" only contains the credits text string.

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

import jrfunctions


#                    10        20        30        40        50        60        70        80        90
#           123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
CREDITS = ("                                  = CREDITS =\n\n"
           "Many people have contributed by providing patches to existing apks or completely\n"
           "building new apks to improve the functionality and/or stability of these units.\n\n"
           "= Rooting the unit => Credits got to Chainfire.eu\n\n"
           "= SofiaServer apk:\n"
           " - NoKill: prevents apps from being killed when going into sleep mode => gustden (XDA)\n"
           " - Steering Wheel mods: configuring your own actions for hard buttons => gustden (XDA)\n"
           " - Hardcoded SRC only: Only SRC button has been reprogrammed => gustden (XDA)\n"
           " - Hardcoded alarm channel muting disables: now voice feedback works => AssassinsLament (XDA)\n"
           " - Nav_app.txt: Add many additional apks that can suppress the radio => surfer63 (XDA)\n\n"
           "= Bluetooth mods and apps:\n"
           " - BlueBalls.apk: enables bluetooth options in settings (hidden by Joying) => doitright (XDA)\n"
           " - BluetoothTetering: BT tetering between your unit and phone => doitright (XDA)\n"
           " - modded Bluetooth apk: enables coupling to all BT devices => treel (XDA)\n\n"
           "= Modded Radio apps: other colors and layout => surfer63 (XDA) a.k.a. hvdwolf (carjoying)\n\n"
           "= Extra voice data files for Google app; only relevant for en-US => dpredster (XDA)\n\n"
)



def CREDITSSSSSSSS(glob_vars):
	jrfunctions.clr_scr()
	print(CREDITS)
	jrfunctions.input_cmd("\n\nPress enter to return to the main menu\n\n")
