#!/bin/sh
# sort, uniq, paste, join, split

########
# sort #
########
# sort <filename>		sorts lines in specified file
# sort -r <filename>	sorts line in reverse order
echo "Enter the names of three friends (separated by a space):"
read name1 name2 name3
touch /tmp/friends.list
echo $name1 > /tmp/friends.list
echo $name2 >> /tmp/friends.list
echo $name3 >> /tmp/friends.list
echo "The list you entered was..."
cat /tmp/friends.list
echo "Sorting list..."
sort /tmp/friends.list

########
# uniq #
########
# used to remvoe duplicate lines in text file
# $ sort file1 file2 | uniq > file3
#	sorts file1 and file2
#	removes duplicates
#	sends output to file3
# $ sort -u file1 file2 > file3
#	does the same thing

##########
# paste  #
##########
# append contents of one file to another
# -s option	appends via row rather than adding columns

touch /tmp/phone.list
echo "Enter $name1's phone number:"
read number1
echo $number1 > /tmp/phone.list
echo "Enter $name2's phone number:"
read number2
echo $number2 >> /tmp/phone.list
echo "Enter $name3's phone number:"
read number 3
echo $number3 >> /tmp/phone.list
echo "This is what you enetered..."
cat /tmp/phone.list
echo "Combining name.list and phone.list..."
paste /tmp/friends.list /tmp/phone.list > /tmp/phone.book
# -d option can be used to select a separating character instead of tabbed
# example:  name:pho-nen-umber
cat /tmp/phone.book

########
# join #
########
# essentially an enhanced version of paste

#########
# split #
#########
# breaks up unequal sized segments of text file
# by default breaks file into 1,000-line segments
# original file remains unchanged
# NOT part of Arch

#####################################
# regular expressions and wildcards #
#####################################
# .	match any single character
# a|z	match "a" or "z"
# $	match end of string
# *	match preceding item 0 or more times
