#! /bin/bash
# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 10/22/19
# ######################################################
# Write your sequence of statements here .

dir=$( pwd )
circlist=""
for circ in $(ls $dir"/circuits/")
do
  size=$(wc -c $dir"/circuits/"$circ | egrep -o "^[0-9]+")
  if [[ $size -gt 200 ]]
  then
    circlist=${circ:8:7}" "$circlist
  fi
done
echo $circlist | egrep -o "[0-9]{2}-[0-9]{1}-[0-9]{2}" | sort

exit 0