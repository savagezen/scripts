#!/usr/bin/perl6

# perl6maven tutorial 3.12 - 3.13

my $filename = prompt 'Enter /path/to/raw_data.file: ';
my $fh = open $filename, :r;		# open $filename as read only

my $sum;
my $count;
my $low;
my $high;

for $fh.lines -> $line {
  if (not $count) {			# this keeps $count from interfereing with $low
    $low = $high = $line;
  }
  # low
  if ($low > $line) {
    $low = $line;
  }
  # high
  if ($high < $line) {
    $high = $line;
  }
  # count
  $count++;
  #sum
  $sum += $line;
}

# count (alternate)
# my @rows = lines $filename.IO;
# $count = $rows.elems;

# mean
my $mean = $sum / $count;

# results
say "Count:		$count";
say "Low:		$low";
say "High:		$high";
say "Sum:		$sum";
say "Mean:		$mean";
