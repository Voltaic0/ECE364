#! /bin/bash
# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 10/22/19
# ######################################################
# Write your sequence of statements here .

dir=$( pwd )
highcount=0
for circ in $(ls $dir"/circuits/")
do
  curcount=$(wc -c $dir"/circuits/"$circ)
  curcount=${curcount:0:3}
  if [[ $curcount -ge $highcount ]]
  then
    highcount=$curcount
    highcirc=${circ:8:7}
  fi

done
egrep $highcirc $dir"/maps/projects.dat" | egrep -o "[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{8}" | sort
exit 0