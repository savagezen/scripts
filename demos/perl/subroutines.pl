#!/usr/bin/perl

use strict;
use warnings;

print "Subroutines are user defined functions\n";

my @words = (
  "this",
  "is",
  "an",
  "array"
);

sub len {
  print (length $_) for @_;
}

len(@words);
print "\n";

# in perl variable inside subroutines are NOT copies
# the ARE the originals

my $a = 7;
print "a = $a\n";
sub reassign {
  $_[0] = 42;
}
reassign($a);
print "a = $a\n";

# subroutine to add characters to left until desired length is reached
sub left_pad {
  my $oldstring = shift;			# if no arry is specified, @_ is implied
  my $width	= shift;
  my $padChar	= shift;
  my $newString = ($padChar x ($width - length $oldstring)) . $ oldstring;
  return $newString;
}

print left_pad("hello", "10", "+");
print "\n";

sub contextualSubroutine {
  # Caller wants a list. Return a list.
  return ("Everest", "K2", "Etna") if wantarray;

  # Caller wants a scalar. Return a scalar.
  return 3;
}

my @array = contextualSubroutine();
print @array, "\n";				# EverestK2Etna

my $scalar = contextualSubroutine();
print $scalar, "\n";				# 3
