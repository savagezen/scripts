#!/usr/bin/perl6
# perl6maven tutorial 3.5

  #`{{
  
  open() function imports files from IO class. 
  two parameters are very important:  name and mode
  default mode is :r		read only
  
  $fh.get is used to read a line from the file
  }}

#my $file = $*PROGRAM_NAME;	# relative path to current script
				# $*PROGRAM_NAME deprecated v2015.6

my $filename = $*PROGRAM-NAME;

my $fh = open $filename;	# file handle

my $line = $fh.get;		# get first line of file
say $line;
