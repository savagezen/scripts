#!/usr/bin/perl6
# perl6maven tutorial 1.1 - 2.3


# single line comment

 #`{{
	Multi line comments use a pound,
	backquote (NOT apostrophe),
	and any brackets such as:
	() [] {} <>
  }}


 #`<<<
	However, there is a bug that
	multiline comments can't start
	on the first character of that line
 >>>

say #`< embedded comments > "Hello World!";

my $n = prompt "What is your name: ";
my $greeting = "Hello, $n!";

say $greeting;

my $x;
my $y;
my $z;                              # can declare variables without defining them
