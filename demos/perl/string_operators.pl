#!/usr/bin/perl

use strict;
use warnings;

print "First number: ";
my $x = <STDIN>;            # get user input
chomp $x;                   # remove trailing new line

print "Second number: ";
my $y = <STDIN>;
chomp $y;

if ($y == 0) {                          # (condition) is true, do...
    print "Cannod divide by zero\n";
#} elsif {
#   second condition....;}
} else {                                # (condition) is false, do...
    my $z = $x / $y;
    print "The result is $z\n";
}