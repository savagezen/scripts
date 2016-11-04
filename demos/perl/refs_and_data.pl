#!/usr/bin/perl

use strict;
use warnings;

my $color = "Red";
my $scalarRef = \$color;	# references use \ w/o quotes

print $scalarRef, "\n";		# SCALR(0x....)
print $$scalarRef, "\n";	# Red
print ${ $scalarRef }, "\n";	# Red 

my %ages = (
  "James" => "29",
  "Jimmy" => "17",
  "John" => "34",
);

my $hashRef = \%ages;

print $ages{"James"}, "\n";		# 29, direct hash access
print ${ $hashRef }{"Jimmy"}, "\n";	# 17, use reference to get hash
print $hashRef->{"John"}, "\n";		# same as above

my %owner1 = (
	"name" => "Santa Claus",
	"DOB"  => "1882-12-25",
);

my %owner2 = (
	"name" => "Mickey Mouse",
	"DOB"  => "1928-11-18",
);

my @owners = ( \%owner1, \%owner2 );

print @owners, "\n";			# will return hash refs

# DATA STRUCTURE
# "should" use:
my %account = (				# start w/ ( )
  "number" => "21345879",
  "opened" => "01.23.12",
  "owners" => [				# note [ ]
    {					# note { }
	"name" => "Austin",
	"dob" => "05.12.88",
    },					# end.austin
    {
	"name" => "Hank",
	"dob" => "06.21.71",
    },					# end.hank
  ],					# end.owners
);					# end.acount

