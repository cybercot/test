#!/usr/bin/perl -w
use strict;

while (<>) {
	my @mass=split;
	my $class='';
	if ($mass[2] eq 'True') {$class='a'}
	else{$class='b'}
	print "$mass[0]	$mass[1]	$class\n"
}
