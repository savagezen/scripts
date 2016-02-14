#!/usr/bin/perl6
# perl6maven tutorial 3.4

  #`{{

  Regular, user defined, variable have sigils:  @ $ %

  }}

say "System variables have an addition character betwen sigil and variable name";
say ".... see comments";


  #`{{
  $*PROGRAM_NAME	relative path to the currently running perl6 script
  $*PROGRAM		full path to the currently running program
  $*CWD			contains a path to the crruent working directory
  $*IN			is standard input (STDIN); read inline with $*IN.get
  $*PID			process ID
  $EXECUTABLE_NAME	realtive path to the current binary (most likely perl6)
  $EXECUTABLE		full path to perl6
  $*TMPDIR		??
  }}

my $in = $*IN.get;
say $in;
