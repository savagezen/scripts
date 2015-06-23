#!/usr/bin/perl -w
use strict;

=pod

=head1 Common Errors

=head2 and probable causes

"Global symbol %$ requires explicit package"

=item

forgot to declare variable, or typo'd or to put "my"

=back

"Use of uninitialized value $x in .. at .."

=item

happens when $x is undef, need one to print $x

=back

"name 'main::x' used only once:  possible typo at .."

=item

probably refers to $x, check typos

=back

"can't locate Module /NameX.pm in @INC (@INC contains: ...)

=item

you probably have 'use Module::NameX'.  check for typos, install location

=back

"scalar found where operater expected at ..."

=item

probably a missing or semicolon

=back

=cut