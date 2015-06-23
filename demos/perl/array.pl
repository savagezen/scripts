#!/usr/bin/perl

use warnings;
use strict;

my @stack = ("Josh", "Stephen", "Austin");
print @stack, "\n"; 					# JoshStephenAustin

# pop
print pop @stack, "\n";					# extract last element

# push
push @stack, "Kacy";					# insert at end
print @stack, "\n";

# shift
print shift @stack, "\n";				# prints first element

# unshift
print unshift @stack, "Mason", "\n";			# insert at beginning

# splice
print splice(@stack, 1, 4, "<<<", ">>>"), "\n";		# print indecies at 2 & 4

# join
my @elements = (
  "Iron",
  "Helium",
  "Nitrogen",
  "Oxygen",
);
print @elements, "\n";					# nospaces
print "@elements\n";					# has spaces
print join(", ", @elements), "\n";			# concatenate (interpret commas)

# reverse
print "Hello World\n";					# Hello World
print reverse("Hello", "World"), "\n";			# World Hello
print scalar reverse("HelloWorld"), "\n";		# dlroWolleH 
print scalar reverse("HelloWorld"), "\n";		# same ^

# map
my @capitals = ("Springfield", "Atlanta", "Birmingham", "Nashville");
print join ", ", map { uc $_ } @capitals, "\n";		# map applies caps (uc) to @states;

# grep
print join ", ", grep { length $_ == 6 } @capitals;	# grep filters input

# sort
print join ", ", sort @capitals, "\n";			# sort lexically (alpha)
