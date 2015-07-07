#!/usr/bin/perl6
# perl6maven tutorial 3.3

say "Before calling die";

die "This will kill the script";	# prints STDERR and ends script

say "This will not show up";
