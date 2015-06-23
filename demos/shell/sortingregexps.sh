#!/bin/sh

# Sorting Expressions

echo "Sorting Regular Expressions:  for use with \"grep\", \"awk / gawk\", and \"sed\"
  Metacharacters and their meanings:
	^  ---------------- Match the beginning of a line
	$  ---------------- Match the end of a line
	*  ---------------- Match anything pending placement of wildcard
	[] ---------------- Characters inside brackets will be matched, can also be ranged
		              - Ex: [1-5] instead of [12345]
	\  ---------------- Used to escape special meaning of metacharacter
	.  ---------------- Match any single character
	pattern \{n\}   --- Match specified pattern that occurs \"n\" times
	pattern \{n\}m  --- Match specified pattern that occurs at least \"n\" times
	pattern \{n,m\} --- Match specified pattern occuring between \"n\" and \"m\" times"
echo "Test:  \"ls -l| grep ..x..x..x\" will match execute permissions for user, group, and other"
ls -l ~| grep ..x..x..x
echo "Test: 
