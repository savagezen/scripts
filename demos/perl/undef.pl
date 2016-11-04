#!/usr/bin/perl

use strict;
use warnings;

=begin commemt

Every scalar variable has a default value called undef.

In case you start to use the variable without giving it a value before

Perl will use this value that will be trnaslated to the value 0 in the

numerical context and to the empty string in string context.

=cut

my $x = $x + 1;        # $x as if it were 0; warning
my $y = $y . "xxx";    # $y = "xxx" because empty string added; warning
my $z++;               # $z becomes 0, no warning, but doesn't do anything

if (not defined $x) {
    $x = 0;
}