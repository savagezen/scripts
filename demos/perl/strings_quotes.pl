#!/usr/bin/perl

use strict;
use warnings;

# Double Quoted
print "noral string\n";     # normal string
print "two\nlines\n";       # two
                            # lines
print "Enter your name: ";
my $n = <>;
print "Hello, $n how are you?";       # Hello Foo, how are you?

print "another 'string'\n";           # another 'string', '' is literal

# print "His "real" name is Foo";     # ERROR
print "His \"real\" name is Foo\n";   # His "real" name is Foo

print "His \"real\" name is \"Foo\"\n"; # ugly! but works
print qq(His "real" name is "$n"\n);    # That looks better!
                                        # parins act like double quotes
                                        
print qq(His "real" name is ("$n")\n);  # multiple parins are okay as long as they match
print qq{His "real" name is $n\n};      # qq is NOT a function, so any parin types will work
print qq{His "real" name is ($n)\n};    # can include parins inside this way

# BUT, those above three will line-break BEFORE the closing parin

# Single Quotes
## single quotes are literal, they don't interpret
print 'one string', "\n";     # one string
print 'a\n', "\n";            # a\n
print 'a $name', "\n";        # a $name
print 'another "string"';     # another "string"

# print 'a'b';                # ERROR
print 'a\'b', "\n";           # a'b
print q(His "variable" name '$namme"\n);  # single q act like single quote as above for qq