#!/usr/bin/perl -w
use strict;

while (<>) {
	my @mass=split;
	my $class='';
	if ($mass[2]==1) {$class='a'}
	else{$class='b'}
	print "$mass[0]	$mass[1]	$class\n"
}
