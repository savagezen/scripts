#!/usr/bin/perl

use strict;
use warnings;

print "Types and Descriptions:\n";
print "scalar:	Preceeded by \$ sign, contain number, string, or reference\n";
print "array:	preceeded by \@ sign, contains list starting with index 0\n";
print "hash:	prefeeded by \% sign, contains key / value combinations\n\n";

print "See Comments for Escape Sequences\n";
=begin comment
\\	backslash
\'	single quote
\a	alert or bell
\b	backspace
\f	form feed
\n	new line
\r	carriage return
\t	horizontal tab
\v	vertical tab
\0nn	create octal formated numbers
\xnn	create hexidecimal numbers
\cX	controls characters, x may be any character
\u	forces next character to upeprcase
\l	forces next character to lowercas
\U	forces all following characters to uppercase
\L	forces all following characters to lowercase
\Q	Backslash all followign non-alphanumeric characters
\E	End \U, \L, or \Q
=cut
