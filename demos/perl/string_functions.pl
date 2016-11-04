#!/usr/bin/perl

use strict;
use warnings;

# length  STRING            number of characters
# lc      STRING            lower case
# uc      STRING            upper case
# lcfirst STRING            lower case first letter
# ucfirst STRING            upper case first letter
# index   STRING,SUBSTRING  looks for SUBSTRING in STRING
# rindex  STRING,SUBSTRING  same as above, starts from right

my $s = "The quick brown fox jumped over the lazy dog";

print index $s, "br";       # prints character index where FIRST found
print "\n";

print index $s, "e";        # 2
print "\n";
print index $s, "e", 3;     # looks for "e" starting at index 3, prints index from start
print "\n";

print index $s, "cat";      # returns -1 if not found
print "\n";

print rindex $s, "la";
print "\n";
print rindex $s, "la", "7";
print "\n";

# substr
#   STRING, OFFSET, LENGTH

my $s1 = "The black cat climbed the green tree";

my $z;

$z = substr $s1, 4, 5;      # start at index 4 and go for 5
print "$z\n";               # black

$z = substr $s1, 4, -11;    # starts at index for, ends at 11 from right
print "$z\n";               # black cat climbed the

$z = substr $s1, -4;        # starts counting from right
print "$z\n";               # tree

$z = substr $s1, -4, 2;     # starts 4 from right, goes 2 to right
print "$z\n";               # tr

$z = substr $s1, 14, 7, "jumped from";  # replace $s1 index 14-21 with 'jumped from'
print "$s1\n";              # The black cat JUMPED FROM the green tree