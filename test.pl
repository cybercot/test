#!/usr/bin/perl -w
use strict;


while (<>) {
	my @mass=split;
	if ($mass[3]==0 or $mass[4]==0) {print "$mass[1]\n"}
}

