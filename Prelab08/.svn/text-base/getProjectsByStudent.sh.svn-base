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
projfile=$dir"/maps/projects.dat"

id=$(egrep "$name" $studfile | egrep -o "[0-9]{5}-[0-9]{5}")

complist=""
file="projlist.txt"
if [ -f $file ] ; then
    rm $file
fi
touch projlist.txt

for circ in $(ls $dir"/circuits/")
do
    if [[ $(egrep "$id" $dir"/circuits/"$circ) ]]
    then
       circnam=${circ:8:7}
       projs=$(egrep "$circnam" $projfile | egrep -o "[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{8}")
       complist=$complist" "$projs
    fi
done
for id in $complist
do
  if grep -q $id $dir"/projlist.txt"
  then
    id=$id
  else
    echo $id >> projlist.txt
  fi
done
sort projlist.txt | cat
rm projlist.txt

exit 0