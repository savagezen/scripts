#!/usr/bin/perl

use strict;
use warnings;

print "Perl doesn't care if you write something as a number or string\n";

print 3 . " ", "\n";        # 3 with space and new line
print 3.1 . " ", "\n";      # 3.1 with space and new line, note '.' is part of integer

print "3" + 5, "\n";        # 8, "3" acts as appropriate integer
print "3.45" + 6.721, "\n"; # same thing

print "3x" + 0, "\n";       # 3, first part interpreted as integer and 'x' ignored
                            # will also get warning
print "3x7" + 2, "\n";      # same as above
                            
print "3\n" + 0, "\n";      # work fine, but lazy

print "" + 0, "\n";         # "" acts as 0 but raises warning

print "z" + 0, "\n";        # warning that 'z' isn't numeric

print "z7" + 0, "\n";       # same as above