#! /bin/bash

# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 10/18/19
# ######################################################
# Write your sequence of statements here .
comp=${1}
dir=$( pwd )
list=0

for circ in $(ls $dir"/circuits/")
do
    if [[ $(egrep "$comp" $dir"/circuits/"$circ) ]]; then list=$(($list + 1)); fi
done
echo $list
exit 0