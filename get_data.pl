#!/usr/bin/perl -w

#This script is used only to take the data from the csv table and format it for the real script to use it

use warnings;
use strict;

my @values = ();

while(my $linha = <>){
    chomp($linha);
    my @col = split(",", $linha);
    my $date = $col[0];
    my $value = $col[1];
    push @values, $value;
}


print "@values";
