#!/bin/sh
# edX Intro to Linux - Bash Shell Scripting
# Exit Status Code Usage

# - "ls" a non existent file
# - display exit status code
# - create file
# - display new exit status code

echo "Enter a file name:"
read file

cd /tmp
if [ -f $file ] ; then
echo "File exists, doing nothing..."

else
ls $file
echo $?					# echo exit status; 0 = success
touch $file
echo $?

fi


