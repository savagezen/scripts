#!/usr/bin/perl

use strict;
use warnings;

my $a = 5;
my $b = 7;

print $a + $b . "\n";	# add
print $a - $b . "\n";	# subtract
print $a * $b . "\n";	# multiply
print $a / $b . "\n";	# divide

print $a ** $b . "\n";	# a to b power
print $a % $b . "\n";	# remainder of a / b

$b++;                  # increase value by 1
$a--;                  # decrease value by 1

my $c = $a + $b;
print "C = $c\n";
$c += 12;              # $c = $c + 12
print "Now C = $c\n";

my $num = rand();     # random number 0 <= NUMBER < 1, because 1 is true, not not a number
print "Random number < 1: $num\n";

my $n = rand(100);    # random number between 0 and 100, but NOT 100
print "Random number < 100: $num\n";

my $i = int(3.12);    # returns whole number part (3)
print "Whole integer part of random number: $i\n";

my $number = int(rand(100));  # 0 <= whole number < 100
print "Whole random number < 100: $number\n";