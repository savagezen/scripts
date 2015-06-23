#!/bin/sh
# Search for file in current directory

file=$1		# Accept input (file name) from command line
dir=$(pwd)

if [ -f $file ]	# Check if file exists
then
	echo -e "$file found in $dir"
else
	echo -e "$file NOT found in $dir"
fi
