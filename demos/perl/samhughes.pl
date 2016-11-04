#!/bin/perl
# perl in 2.5 hours - http://qntm.org/files/perl/perl.html
# Times: 17:45 : 18:30

use strict;
use warnings;

print "Arch is the best!\n";

# Variables - scalar ($)
my $undef = undef;    # undefined
print $undef;         # prints "" & raises warning

my $undef2;
print $undef2;        # prints "" and raises same warning

my $num = 178.5;
print $num, "\n";

my $string = "foo";
print $string, ".bar \n";

# Variables - Boolean
# There are no T/Fs in Perl
# Scalars in "if" are false ONLY if they = undef, number 0, string "", string "0"

my $str1 = "4G";
my $str2 = "4H";

print $str1 .  $str2;
print $str1 +  $str2; # "8" with two warnings
print $str1 eq $str2; # "" empty string / false
print $str1 == $str2; # "1" with two warnings

# "classic error"
print "yes" == "no"; # "1" with two warnings; both values evaluate to 0 when used as numbers

# numerical operators: < > <= >= == != <=> + *
# string operators:   lt gt le ge eq ne cmp . x

# Variables - array
# NOTE:  @ , $
my @array = (
  "print\n",
  "these\n",
  "words\n",
  "out\n",
  "for\n",
  "me\n", # trailing comma is okay
);
print $array[0];  # "print"
print $array[1];
print $array[2];
print $array[3];
print $array[4];
print $array[5];  # "me" + warning
print $array[-1]; # "me"
print $array[-6]; # "print"
print $array[-7]; # undef, prints "", raises warning

print "This array has ".(scalar @array).." elements\n";     # no. of scalars in array
print "The last populated index is ".$#array, "\n";         # last index is 5

print "\$string bar\n";
print "string = \$string \n";
print "\@array \n";           # "@array"
print '@array', "\n";         # "@array"
print "@array \n";            # prints array contents
print @array, "\n";           # prints array contenst

# Variables - Has (%) - like python dictionary
# NOTE: % => $
my %states = (
  "Illinois"    =>  "IL",   # => called 'fat comma'
  "Georgia"     =>  "GA",
  "New York"    =>  "NY",
  "California"  =>  "CA",   # tariling comma still okay
);

print $states{"Illinois"};
print $states{"California"};
print $states{"CA"};              # returns below error
print $states{"China"}, "\n";     # returns undef, prints "" and raises warning

my @states = %states;             # can set array = to hash
print @states;                    # order not necessarily preserved, whichever is most efficient

######################
# Review #############
######################
my $data = "string";
my @data = (
  "a",
  "r",
  "r",
  "a",
  "y",
);
my %data = (
  "hash" => "variable",
);
print $data;
print $data[0];           # [] used to call array entry
print $data{hash};        # {} used to call hash key

