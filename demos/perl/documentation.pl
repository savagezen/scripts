#!/usr/bin/perl -w
use strict;

print "Regular text.....\n";

=pod

=head1 Title

=head2 Subtitle

  regular text like a brief description
  more text on another line

new parragraph.  the comment witll continue until  it is specified by =cut at the beginning of line.

Some examples of documentation tags:

=over 4

=item *

First Item

=item *

Second Item

=item *

Third Item

=back

=cut

print "Documentation hiding in comments!\n";
print "Run this file with 'perldoc' instead of 'perl'\n";