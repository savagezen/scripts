#!/usr/bin/perl

print "Use 'open' to turn scalar variable into file handle\n";
my $f = "system_call.pl";
my $result = open my $f, "<", $f;               # oen must have a mode, < meanopen and read from

if (!$result) {
    die "Couldn't open'".$f."' for reading because: ".$!;   # build in variable where
}                                                           #   error will bestuffed

print "To read al ine of text from a file use 'readline' function.\n";
while(1) {
    my $line = readline $fh;
    last unless defined $line;
    # process the line
}

chomp $line;                                    # truncate trailing line (no line break)
# chomp acts on $line in place
# so don't: $line = chomp $line

print "Use 'eof' function to detect end of file has been reached\n";
while (!eof $fh) {                              # read $line as long as 'readline' finds a line
    my $line = readline $fh;
    # process $line
}

# 'open' modes:
## >    = open and read
## <<   = write to / append

open(my $fh2, ">", $f) || die "Couldn't open '".$f."' for writing because: ".$!;
print $fh2 "The eagles have left the nest";     # notice NO comma

# files normally close automatically when tehy drop out, otherwise
close $fh2;
close $fh;

my @g = (
  "STDIN",
  "STDOUT",
  "STDERR",
);
print "Filehandles exist as global constants: @g\n";

my $line = <STDIN>;                         # read single line of user input
<STDIN>;                                    # wait for user to hit <Enter>

print "The function '-e' tests whether filename esits\n";
print "what" unless -e "/usr/bin/perl";
print "The function '-d' tests whether the named file is a directory\n";
print "The function '-f' tests whether named file is a plain file\n";