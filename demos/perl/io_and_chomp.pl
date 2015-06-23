#!/usr/bin/perl
use strict;
use warnings;

my $name = "Foo";
print "Hello ", $name, " - how are you ?\n";

print "Hello $name - how are you?\n";

my $usr_name = <STDIN>;
print "Hello $usr_name - how are you ?\n";    # <STDIN> includes trailing <Enter>
chomp $usr_name;
print "Hello $usr_name - how are you ?\n";