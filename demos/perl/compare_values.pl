#!/usr/bin/perl

use strict;
use warnings;

# "12.0" == 12      true, 12.0 automatically interpreted as integer
# 2 < 3             true, obvious
# 2 lt 3            true, 2 comes before 3
# "12.0" eq 12      FALSE, no period or '0' in second value
# 12 < 3            true, obvious
# 12 gt 3           FALSE, '1...' is before '3...' + warning
# "foo" == ""       true, comparing strings w/ == ; gives warning
# "foo" eq ""       FALSE, obvious
# "foo" == "bar"    true + warning, both non-integers
# "foo" eq "bar"    FALSE, obvious

print "What is your name: ";
my $input = <STDIN>;
chomp $input;
if ($input eq "") {
# if ($input == "")             WRONG!  will actually return as true, both non-numbers, use eq
    print "Empty String\n";
}