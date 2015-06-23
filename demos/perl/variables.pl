#!/usr/bin/perl

use warnings;
use strict;

print "Variable Types:\n";
print "Scalar:	(\$) strings, floats, and integers\n";
print "Array:	(\@) list of variables with index starting at 0\n";
print "Hash:	(\%) key / values with corresponding index\n\n";

my $name = "Austin";          # variable names can't start w/ number, e.g. $1
my $age = 27;
my $salary = 20.675;
my $number = 1_345_652;       # 1,345,652
my $temp = undef;

print "$name\n";
print "$age\n";
print "$salary\n\n";

my @ages = (55, 55, 27, 26);
my @names = (
  "Larry",
  "Rita",
  "Austin",
  "Travis"
);
my $names = @ages;			# Returns number of entries
					# NOT explicit content
print "\$names[0] = $names[0]\n";
print "\$names[1] = $names[1]\n";
print "\$names[2] = $names[2]\n";
print "\$names[3] = $names[3]\n";
print "\$ages[0] = $ages[0]\n";
print "\$ages[1] = $ages[1]\n";
print "\$ages[2] = $ages[2]\n";
print "\$ages[3] = $ages[3]\n";
print "There are $names names\n";
print "Number of Names: ", scalar @ages, "\n\n";

my @abc = ("a".."z");			# range from a - z
my @num = ("1".."10");			# range from 1 - 10

print "@abc\n";
print "@num\n";
#foreach $number (@num) {		# print on separate lines
#  print "$number\n"};			# 'strict' wills top this, saying
					# $number needs defined
print "$_\n" for @num;
print "Boolean variables (T/F), doesn't care about content\n";
print "Void variables = doesn't care what vale or even return value\n";

my %family = (				# hash / dictionary
  "Larry" => "Dad",
  "Rita" => "Mom",
  "Travis" => "Brother",
  "Austin" => "Me",
);

print $family{"Larry\n"};		# Dad

my @bones   = ("humerus", ("jaw", "skull"), "tibia");
my @fingers = ("thumb", "index", "middle", "ring", "little");
my @parts   = (@bones, @fingers, ("foot", "toes"), "eyeball", "knuckle");
print "$_\n" for @parts;

my $boolean = 1;			# perl can use any
print "My Boolean: ", $boolean, "\n";	# variable as boolean
					# True >= 1, False =< 0

{
  my $inside_block = "variable defined inside block";
  # $inside_block can't be read outside of containing curly braces
  print "$name\n";      # can still print outside-defined variable inside
  my $name = "Foo";
  print "$name\n";      # only redifines while INSIDE block
}