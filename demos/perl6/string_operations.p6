#!/usr/bin/perl6
# perl6maven tutorial 2.6 - 2.8

my $x = "Shoulder Bone";
my $y = "Neck Bone";

my $z = $x ~" connected to the "~ $y;   # same as "$x connected to $y"
say $z;                                 # Sholder Bone connected to Neck Bone

my $w = "Take " ~ (2 + 3);
say $w;                               # Take 5
say "Take 2 + 3";                     # Take 2 + 3
say "Take {2 + 3}";                   # Take 5

my $z ~= "! ";                        # $z = $z connected to exclamation point and space
say $z;

my $a = prompt "Enter a string:  ";
my $b = prompt "Enter another string: ";
my $c = $a ~ $b;				# $a$b
my $d = $a ~" "~ $b;				# $a $b
say $c;
say $d;

my $n = prompt "Enter a number: ";
my $q = $d x $n;
say $q;
