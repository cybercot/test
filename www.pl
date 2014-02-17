#!/usr/bin/perl -w
use strict;

while (<>) {
	my @mass=split;
	if ($mass[5]==1) {print "$mass[0]	$mass[1]	$mass[2]	$mass[3]	$mass[4]	a\n"}
	else {print "$mass[0]       $mass[1]        $mass[2]        $mass[3]        $mass[4]        b\n"}
}
