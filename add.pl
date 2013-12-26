#!/usr/bin/perl -w
use strict;

open FILE,"<my.txt" or die "$!";
my %hash;
while (<FILE>) {
	my @mass=split;
	$hash{$mass[0]}=$_;
}

while (<>) {
	my @mass=split;
	if (exists $hash{$mass[0]}) {
		my @mass2=split(' ',$hash{$mass[0]});
		print "$mass[0]	$mass[1]	$mass[2]	$mass2[1]	$mass2[2]\n";
	}
}
