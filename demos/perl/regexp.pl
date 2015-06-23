#!/usr/bin/perl

use strict;
use warnings;

# match operators:  =~ m//
# in scalar context, returns true on success and false on failure

my $string = "Hello world";
if($string =~ m/(\w+)\s+(\w+)/) {
	print "success\n";
	# string exists / is defined
}

# paraenthesses perform submatches
# on success sub-matches stuffed into $1 $2 $3

print $1;           # hello
print $2;           # world

#####################################
# NOT FINISHED
###################################