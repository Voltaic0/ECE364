#! /bin/bash

# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 10/18/19
# ######################################################
# Write your sequence of statements here .
name=${1}
dir=$( pwd )

studfile=$dir"/maps/students.dat"

id=$(egrep "$name" $studfile | egrep -o "[0-9]{5}-[0-9]{5}")

for circ in $(ls $dir"/circuits/")
do
    if [[ $(egrep "$id" $dir"/circuits/"$circ) ]]; then echo ${circ:8:7}; fi
done

exit 0