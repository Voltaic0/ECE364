#! /bin/bash

# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 10/18/19
# ######################################################
# Write your sequence of statements here .
comp=${1}
comp2=${2}
dir=$( pwd )
list=0
list2=0

for circ in $(ls $dir"/circuits/")
do
    if [[ $(egrep "$comp" $dir"/circuits/"$circ) ]]; then list=$(($list + 1)); fi
    if [[ $(egrep "$comp2" $dir"/circuits/"$circ) ]]; then list2=$(($list2 + 1)); fi
done
echo $list
echo $list2

if  [[ $list -gt list2 ]]; then echo $comp; else echo $comp2; fi
exit 0