#!/bin/bash

regex="([[:digit:]]+)-([[:digit:]]+),([[:digit:]]+)-([[:digit:]]+)"

part1=0
part2=0

while read p; do
  if [[ $p =~ $regex ]]
  then

    A="${BASH_REMATCH[1]}"
    B="${BASH_REMATCH[2]}"
    C="${BASH_REMATCH[3]}"
    D="${BASH_REMATCH[4]}"

    if [[ $A -le $C ]] && [[ $B -ge $D ]]
    then
      ((part1=part1+1))
      ((part2=part2+1))
    elif [[ $A -ge $C ]] && [[ $B -le $D ]]
    then
      ((part1=part1+1))
      ((part2=part2+1))
    elif ( [[ $A -le $C ]] && [[ $B -ge $C ]] ) || ( [[ $A -le $D ]] && [[ $B -ge $D ]] )
    then
      ((part2=part2+1))
    fi
  else
    echo "No match"
  fi
done <input4.txt

echo "Part 1: $part1"
echo "Part 2: $part2"
