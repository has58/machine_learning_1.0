#! /usr/bin/env perl

use warnings;
use strict;

my ($filename, $labels) = @ARGV or die "Command Argument is not present\n";

my $sum = 0;
open(my $data, '<:encoding(UTF-8)', $filename) or die "Could not able to open the '$filename'\n";

print "$data\n";
#while (my $line = <$data>)
#{	chomp $line;
#	my @fields = split "", $line;
#	$sum += $fields[2];
#}
#print "$sum\n";
