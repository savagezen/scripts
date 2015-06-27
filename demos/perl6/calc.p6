#!/usr/binn/perl6
# perl6maven tutorial 2.14 - 2.15

my $a = prompt "Number: ";
my $o = prompt "Operator: ";
my $b = prompt "Number: ";

if $o eq "+" {say $a + $b;}
 elsif $o eq "-" {say $a - $b;}
 elsif $o eq "*" {say $a * $b;}
 elsif $o eq "/" {say $a / $b;}
 else {say "Invalid operator: $o";}

given $o {                                # $o is referred to as "the topic"
  when "+" { say $a + $b; }
  when "-" { say $a - $b; }
  when "*" { say $a * $b; }
  when "/" { say $a / $b; }
  default  { say "Invalid operator $o"; }
}