#!/usr/bin/perl6
# perl6maven tutorial 2.9 - 2.12

my $age = prompt "What is your age:  ";
if $age > 18 {
  say "You can vote in most countries.";
}

if $age > 18 {
    say "Above 18";
} else {
    say "Below 18";
}

say $age > 18 ?? "Above 18" !! "Below 18";

say $age == any(20..29)                     # if $age in given range
  ?? "You are in your 20's"                 # if it IS, do this (??)
  !! "You are not in your 20's";            # if it is NOT, do this (!!)

# Can also be written as:  CONDITION ?? DO_THIS_IF_TRUE !! DO_THIS_IF_FALSE;

my $comp_num = "==  !=  < > <=  >=";
my $comp_abc = "eq  ne  lt  gt  le  ge";
say "Compare Numbers: $comp_num";
say "Compare Strings: $comp_abc";

my $q1 = prompt "3 == 4 (t/f) ";
say $q1 eq "f" ?? "Correct!" !! "Wrong, the integer 3 does not equal the integer 4";

my $q2 = prompt "'35' eq 35.0 (t/f) ";
say $q2 eq "f" ?? "Correct!" !! "Wrong, using string comparrison with non-string";

my $q3 = prompt "'25' == 25.0 (t/f) ";
say $q3 eq "t" ?? "Correct!" !! "Wrong, in this case string numbers get automatically converted";

my $q4 = prompt "13 > 2 (t/f) ";
say $q4 eq "t" ?? "Correct!" !! "Wrong, the digit 13 IS greater than the digit 2";

my $q5 = prompt "14 gt 2 (t/f) ";
say $q5 eq "f" ?? "Correct!" !! "Wrong, the '1' in '13' will be read as a string coming before 2";

my $q6 = prompt "'hello' == 'world' (t/f) ";
say $q6 eq "t" ?? "Correct, but with an exception.  They're definded and thus both true" !! "Wrong, but it's a trick question.";

my $q7 = prompt "'hello' eq 'world' (t/f) ";
say $q7 eq "f" ?? "Correct!" !! "Wrong, the strings are certainly not equal to eachother";

my $q8 = prompt "'hello' == '' (t/f) ";
say $q8 eq "t" ?? "Wrong, but it's a trick question." !! "Correct, but with an exception.  One element is defined and the other is not, they they're not equal";

my $q9 = prompt "'hello' eq '' (t/f) ";
say $q9 eq "f" ?? "Correct!" !! "Wrong, the strings are not equal.";

# and     &&
# or      ||
# orelse  //
# xor     ^^
# not     !

say "-----";
say (2 && 1);     # 1 - && prints the second variable
say (2 or 1);     # 2 - || prints the first
say (0 && 1);     # 0 - a leading zero reverses that rule
say (0 or 3);     # 3

say "-----";      # XOR is where neither condition is true
say (1 ^^ 0);     # 1 - defaults to true condition?
                  #     - 0 can't budge but there are inifinite numbers between 0 and 1
say (0 ^^ 1);     # 1 - defaults to true condition?
say (0 ^^ 0);     # 1 - neither variables meet this condition
say (1 ^^ 1);     # NIL - impossible

say "-----";
say (1 // 0);     # 1 - true or else false = true
say (0 // 1);     # 0 - false or else ture = fale
say (1 // 1);     # 1 - true or esle true = true
say (0 // 0);     # 0 - false or else fale = false

say "-----";
say (not 1);      # false
say (not 0);      # true