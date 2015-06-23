#!/bin/sh
# Prompt for user age and sort by decade

echo "Enter your age in years:"				# prompt
read AGE						# input

if [ "$AGE" -lt 13 ] ; then				# if AGE < 13
echo "You're not even a teenager..."

elif [ "$AGE" -ge 13 ] && [ "$AGE" -lt 20 ] ; then	# && used for "AND" conditions
echo "You're a teenager"

elif [ "$AGE" -ge 20 ] && [ "$AGE" -lt 30 ] ; then
echo "You're a young adult"

elif [ "$AGE" -ge 30 ] && [ "$AGE" -lt 40 ] ; then
echo "You're an adult"

elif [ "$AGE" -ge 40] && [ "$AGE" -lt 60 ] ; then
echo "You're middle-aged"

elif [ "$AGE" -ge 60 ] && [ "$AGE" -lt 70 ] ; then
echo "You're getting close to Social Security and senior discounts"

elif [ "$AGE" -ge 70 ] && [ "$AGE" -lt 100 ] ; then
echo "You're getting up there...."

elif [ "$AGE" -ge 100 ] ; then
echo "You've passed the century mark... what's next?"

elif [ "$AGE" -lt 1 ] || [ "$AGE" -gt 120 ] ; then	# || used for "OR" condition
echo "Sorry, you're age is out of range"

fi
