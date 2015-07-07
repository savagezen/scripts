#$!/usr/bin/perl
# per6maven tutorial 3.7

my $filename = $*PROGRAM-NAME;	# use quotes if specifying file name; '/path/to/file'

my $fh = open $filename;
for $fh.lines -> $line {	# for linse in fh (using .lines function)
  say $line;
}
