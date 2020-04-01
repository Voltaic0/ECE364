#! /bin/bash
# ######################################################
# Author : Mark Dunn
# email : dunn60@purdue.edu
# ID : ee364a12
# Date : 10/22/19
# ######################################################
# Write your sequence of statements here .
name=${1}
dir=$( pwd )
studfile=$dir"/maps/students.dat"
id=$(egrep "$name" $studfile | egrep -o "[0-9]{5}-[0-9]{5}")
circlist=""
for circ in $(ls $dir"/circuits/")
do
    if [[ $(egrep "$id" $dir"/circuits/"$circ) ]]; then circlist=${circ:8:7}" "$circlist; fi
done
complist=""

for circ in $circlist
do
  compids=$(egrep -o "[A-Z]{3}-[0-9]{3}" $dir"/circuits/circuit_"$circ".dat")
  complist=$compids" "$complist
done
file="compsort.txt"

if [ -f $file ] ; then
    rm $file
fi
singlist=""
for comp in $complist
do
  if [[ $singlist =~ .$comp ]]
  then
    singlist=$singlist
  else
    singlist=$singlist" "$comp
    echo $comp >> compsort.txt
  fi
done

sort compsort.txt | cat
rm compsort.txt



exit 0