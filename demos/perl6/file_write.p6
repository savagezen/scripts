#!/usr/bin/perl
# perl6maven tutorial 3.8 - 3.9

  #`{{
  
  Open File Modules:
  :r	read
  :w	write
  :a	append

  }}

my $filename = "/tmp/temp.txt";		# name file to write to

my $fh = open $filename, :w;		# write mode specified
$fh.say("hello world");			# text to write, other output methods: print() printf()
$fh.close;
