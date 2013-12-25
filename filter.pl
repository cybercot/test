#!/usr/bin/perl -w
use strict;

while (<>) {
	my @mass=split;
	if ($mass[3]>5 and $mass[4]>5) {
		print "$mass[0]	$mass[1]	$mass[2]	$mass[3]	$mass[4]\n"
	}
}
