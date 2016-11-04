#!/bin/sh
# Reference - http://tldp.org/LDP/abs/html/varsubn.html
# Reference - http://www.freeos.com/guides/lsst/ch02sec02.html
# Reference - http://www.cyberciti.biz/faq/bash-for-loop/

VariableName=Value		# VariableName=Value; no space is permitted on either side of "="
NoWhiteSpace="A B C   D"
WhiteSpace="A B C    D"
letters="one two three"		# Quotes needed if whitespaces in value
numbers="1 2 3"
mixed_bag=2\ ---\ Whatever	# Can use "\" to escape whitespaces in value
a=879

echo "VariableName"		# Print quoted text
echo $NoWhiteSpace		# Print value of Variable1 without white spaces preserved
echo "$WhiteSpace"		# Print value of Variable1 with white spaces preserved
echo "$numbers = $letters"
echo $mixed_bag

echo "The value of \"a\" is $a"	# Simple reading variable with quoted expression "a"

let a=16+5			# Reassign value of variable "a"
echo "The value of \"a\" is now $a"

echo "Enter value:"		# Allow user to input value and assign it to "a"
read a
echo "The value of \"a\" is now $a"

for i in 1 2 3 4 5		# Specify literal range
do
   echo "Welcome $i"		# Execute command for the specificed range
done

for i in {1..5}			# Specify range with squigly braces
do
   echo "Test $i"
done

for i in {0..110..20}		# {START..END..INCREMENT}
do
   echo "Block $i"
done

exit 0