#!/bin/bash

# ipaddress given?
if [ "$1" = "" ]
then
	echo -e '\n\nno argument given. I need the ip-address. Restart the script with "./jrassist.sh ip-address"\n\n'
	exit
fi
cd py-scripts
./jrassist.py $1

