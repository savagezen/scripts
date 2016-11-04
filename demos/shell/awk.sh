#!/bin/sh

# gawk = GNU version of awk

# awk is used to extract then print specific contents of a f ile
# - powerful utility and interpreted programming language
# - used to manipulate data files, retrieving, and processing text
# - works well with "fields" and "records" (programs)

# awk 'command' var=value file
#	specify a command directly at the command line
# awk -f scriptfile var=value file
#	specify a file that contains the script to be executed along with "f"

echo "Enter the path to a file to search with awk:"
read PATH

echo "Printing entire file..."
awk '{ print $0 }' $PATH	# print entire file

echo "Printing first column of every line..."
awk -F: '{print $1}' $PATH	# print first field (column) of every line

echo "Printing first and sixth column of every line..."
awk -F: '{print $1 $6}' $PATH	# print first and 6th field of every line
