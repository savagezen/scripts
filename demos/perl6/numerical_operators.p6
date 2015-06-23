#!/usr/bin/perl6
# perl6maven tutorial 2.4 - 2.5

my $x = prompt "Enter a number: ";            # strings are automatically converted to integers
my $y = prompt "Enter another number: ";      # when needed

my $add = $x + $y;
say "$x + $y = $add";

my $sub = $x - $y;
say "$x - $y = $sub";

my $multip = $x * $y;
say "$x * $y = $multip";

my $div = $x / $y;
say "$x / $y = $div";

my $mod = $x % $y;
say "The remainder of $x / $y is $mod";

my $x += 14;                                  # same as $x = $x + 14
say "New X = $x";

my $y++;                                      # same as $y = $y + 1
my $y--;                                      # same as $y = $y - 1

my $exp = $x ** $y;
say "$x to the power of $y = $exp";