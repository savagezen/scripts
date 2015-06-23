#!/usr/bin/perl
# perl6maven tutorial 2.13

my $a = prompt "Enter a number between 21 and 57: ";
if $a >= 21 && $a <= 57 {
# if 21 <= $a <= 57
  say "$a is in the range.  You can follow directions!";
} else {
  say "$a is not in the range.  Fail!";
}

my $small = prompt "Enter a number between 0 and $a: ";
my $big = prompt "Enter a number between $a and 100: ";
if 0 <= $a <= $big <= 100 {
  say "Good!";
} else {
  say "You messed up somewhere...";
}