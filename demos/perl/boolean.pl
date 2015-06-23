#!/usr/bin/perl

use strict;
use warnings;

# boolean a.k.a. logical operators

# and   &&
# or    ||
# not   !
# xor

print "DO NOT mix numbers or words when comparing in same expressin!\n";
# see also perldoc / perl loop

if ($z) {
    # if $z is true
}

=begin comment

FALSE values:

undef

""

0 0.0 000000 0e+10

"0"

ALL OTHER VALUES ARE TRUE!

=cut

if ($my_salary > 1_000_000 or $mmy_salary > 10_000) {       # if condition 1 is true, cond 2 is never checked
                                                            # if both are true, cond1 has precidence
}

if ($my_salary > 1_000_000 or $my_salary++ > 10_000) {      # adds 1 every time checked
}