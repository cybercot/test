#!/usr/bin/perl -w
use strict;

my %hash_1;
my %hash_2;

open FILE,"<potapov_ref.txt" or die "$!";
while (<FILE>) {
	my @mass=split;
	$hash_1{$mass[1]}+=$mass[3];
	$hash_2{$mass[1]}+=1;	
}
open FILE2,"<potapov_ref.txt" or die "$!";
open RESULTS,">ref_final.txt" or die "$!";
while (<FILE2>) {
	my @mass=split;
	if (exists $hash_1{$mass[1]}) {my $ratio=$hash_1{$mass[1]}/$hash_2{$mass[1]};
		print RESULTS "$mass[1] $mass[3] $ratio\n"}
}

open FILE3,"<potapov_alt.txt" or die "$!";
open RESULTS2,">alt_final.txt" or die "$!";
while (<FILE3>) {
        my @mass=split;
        if (exists $hash_1{$mass[1]}) {my $ratio=$hash_1{$mass[1]}/$hash_2{$mass[1]};
                print RESULTS2 "$mass[1] $mass[3] $ratio\n"}
}
