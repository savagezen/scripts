#!/usr/bln/perl6

my $filename = 'examples/numbers.txt';

my $total;
my $count;
my $min;
my $max;

if (my $fh = open $filename, :r) {
    for $fh.lines -> $line {
        if (not $count) {
            $min = $max = $line;
        }
        $total += $line;
        if ($min > $line) {
            $min = $line;
        }
        if ($max < $line) {
            $max = $line;
        }
        $count++;
    }
    my $average = $total / $count;
    say "Total: $total, Count: $count Average: $average Min: $min Max: $max";
} else {
    say "Could not open '$filename'";
}

# There is a minor issue in this solution, what if there are no values at all in the 
file?
