#!/usr/bin/perl

use strict;
use warnings;

my $random_number = rand();
my $random_10 = int(rand(10));
my $range = 57;

print "Random Number: ", $random_number, "\n";
print "Random Number (0-10): ", $random_10, "\n";
print "Random Number (with assinged range of $range): ", int(rand($range)), "\n";
