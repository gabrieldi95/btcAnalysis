#!/usr/bin/perl -w
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
