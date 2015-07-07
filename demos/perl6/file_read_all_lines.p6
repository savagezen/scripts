#!/usr/bin/perl6
# perl6maven tutorial 3.6

my $filename = $*PROGRAM-NAME;

my $fh = open $filename;
while (defined my $line = $fh.get) {	# while getting lines
  say $line:				# say the line
}
