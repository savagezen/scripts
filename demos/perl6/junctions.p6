#!/usr/bin/perl
# perl6mavven tutorial 2.18

say "Select an option:";
say "(1) One";
say "(2) Two";
say "(3) Three";
$c = prompt '';

if $c == 1 || $c == 2 || $c == 3 {
  say "Valid Choice";
} else {
  say "Invalid Choice";
}

if $c == 1|2|3 {
  say "Valid Choice";
} else {
  say "Invalid choice";
}