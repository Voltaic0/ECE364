#! /bin/bash

# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 10/18/19
# ######################################################
# Write your sequence of statements here .
circ=${1}
dir=$( pwd )
projfile=$dir"/maps/projects.dat"
info=$(sort $projfile | egrep $circ | egrep -o "[0-9]{2}-[0-9]-[0-9]{2}")

studfile=$dir"/maps/students.dat"

test=""
for circuit in $info
do
    circfile=$dir"/circuits/circuit_"$circuit".dat"
    ids=$(cat $circfile | egrep "[0-9]{5}-[0-9]{5}")
    for stud in $ids
    do
      if [[ $test =~ .$stud ]]; then test=$test; else test=$test" "$stud; fi
    done

done

file="alphasort.txt"

if [ -f $file ] ; then
    rm $file
fi

for id in $test
do
    egrep $id $dir"/maps/students.dat" | egrep -o "[A-Z][a-z]+, [A-Z][a-z]+" >> alphasort.txt

done
sort alphasort.txt | cat
rm $file
exit 0