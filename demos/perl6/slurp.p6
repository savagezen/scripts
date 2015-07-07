#!/usr/bin/perl6
# perl6maven tutorial 3.10 - 3.11

my $filename = $*PROGRAM_NAME; # use quotes is specifying external file '/path/to/file'

# slurp into scalar variable
my $data = slurp $filename;
say $data;			# print entire file
# say $data.bytes;

# read / slurp lines into array
my @content = slurp $filename;
say @content.elems;		# say .elems of @content array
				# 1 - line / element

# read / slurp all content of file (every line) into array
my @rows = lines $filename.IO;
say @rows.elems;		# say .elems of 
				# 19 - lines / elements
