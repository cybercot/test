#!/usr/bin/perl -w
use strict;

while (<>) {
	my @mass=split;
	if ($mass[1]>5 and $mass[2]>5) {
		print "$mass[0]	$mass[1]	$mass[2]\n"
	}
}
