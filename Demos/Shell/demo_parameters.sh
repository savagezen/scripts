#!/bin/sh
# edX - Introduction to Linux
# Bash Scripting - Script Parameters

# - display the name of the scripts
# - display the value of the first argument / parameter passed from the terminal
# - display the value of the second and third arguments / parameters passed from the terminal

echo "The name of this script is :  " $0
echo "The first parameter is:  " $1
echo "The second parameter is:  " $2
echo "The third parameter is:  " $3
echo "Parameters passed:  " $*

