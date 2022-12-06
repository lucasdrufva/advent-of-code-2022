#!/opt/homebrew/bin/perl
use strict;
use warnings;
use Storable qw(dclone);

# Hard coded puzzle input...
my @stacks = ( ['N', 'R', 'G', 'P'],
            ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C'],
            ['M', 'S', 'V'],
            ['L', 'S', 'R', 'C', 'Z', 'P'],
            ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q'],
            ['C', 'T', 'N', 'W', 'D', 'M', 'S'],
            ['H', 'D', 'G', 'W', 'P'],
            ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V'],
            ['R', 'P', 'F', 'L', 'W', 'G', 'Z']);

my @part1_stack = @{ dclone(\@stacks) };
my @part2_stack = @{ dclone(\@stacks) };

my $file = 'input5.txt';
open(FH, $file) or die("File $file not found");
      
while(my $String = <FH>)
{
  if($String =~ /^move (\d+) from (\d+) to (\d+)$/)
  {
    # Part 1
    my @count = (0...(int($1)-1));
    for(@count)
    {
      my $val = pop @{@part1_stack[int($2)-1]};
      push(@{@part1_stack[int($3)-1]}, $val);
    }

    # Part 2
    my @moving = splice(@{@part2_stack[int($2)-1]}, -(int($1)), int($1) );
    push(@{@part2_stack[int($3)-1]}, @moving);
  }
}
close(FH);

print "Part 1: ";
my @i = (0..8);
for my $j (@i)
{
  print $part1_stack[$j][-1];
}
print "\n";

print "Part 2: ";
@i = (0..8);
for my $j (@i)
{
  print $part2_stack[$j][-1];
}
print "\n";
