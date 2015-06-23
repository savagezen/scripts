#!/usr/bin/perl6
# perl6maven tutorial 2.16 - 2.17

my $s = "The black cat jumped from the green tree";

say index $s, "e";          # 2, the index where 'e' is found in $s
say index $s, "e", 3;       # 3, index, after 3rd, where 'e' is found in $s
                            # first 3 still counted in output

say rindex $s, "e";         # 39, index, from the right, where 'e' is found in $s
say rindex $s, "e", 38;     # 38
say rindex $s, "e", 37;     # 33

say index "s", 4;           # (Int)
say index "s", 99;          # (Int)

my $a = "The black cat climbed the green tree";
my $z;
$z = substr $s, 14;         # $s starting at 14th index;
say $z;                     # think "going to the end, then coming back 14"

$z = substr $s, 4, 5;       # $z = black; 5 charcters from the 4th index of $s
say $z;
$z = substr $s, 4, *-11;    # $z = $s from 4th index to 12th character from end (chopped 11)
say $z;
$z = substr $s, *-4;        # 4 indexes from the right of $s
say $z;
$z = substr $s, *-4, 2;     # go to the end (*), then back 4 (-4), then print 2 chars (2)