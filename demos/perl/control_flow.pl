#!/usr/bin/perl

use strict;
use warnings;

my $a = 5;
my $b = 7;

if ($a > $b) {				# if 5 > 7
  print "$a is more than $b\n"		# 5 is not > 7
} elsif ($a < $b) {
  print "$a is not more than $b\n"
} else {				# a = b
  print "$a = $b\n"
};

unless ($a > $b) {			# unless 5 > 7
  print "$a is not more than $b\n"	# this gets executed unless 5 > 7
};

my @array = ("1", "2", "3");
my $i = 0;

while($i < scalar @array) {		# while loop
  print $i, ": ", $array[$i];
  $i++;
};
print "\n";

# can also use "until" loops in same way

# could use "foreach" but may throw warning, so do:
print "$_\n" foreach @array;		# could also just use "for"

# also "do" + while, but will throw error if @array is empty


# LAST and NEXT (in loops)
