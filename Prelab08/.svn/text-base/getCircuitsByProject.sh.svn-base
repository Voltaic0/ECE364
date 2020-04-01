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

myfile=$dir"/maps/projects.dat"

info=$(sort $myfile | egrep $circ | egrep -o "[0-9]{2}-[0-9]-[0-9]{2}")

for circuit in $info
do
    echo $circuit
done

exit 0