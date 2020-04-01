#! /bin/bash

#----------------------------------
# $Author: ee364a12 $
# $Date: 2019-10-29 11:18:57 -0400 (Tue, 29 Oct 2019) $
#----------------------------------

function part_1 
{
    line =""
    echo $line >> sim.txt
    for lin in $(cat file.txt)
    do
      if [[  $(egrep $lin file.txt | wc -w) -gt 1 ]]
      then
          if [[ $(egrep $lin sim.txt) ]]
          then
              line=$lin
          else
              echo $lin >> sim.txt
          fi
      fi
    done
    sort sim.txt | cat
    rm sim.txt
    # Fill out your answer here. Do not include exit 0 in your code.
    return                      
}                               

function part_2
{              
    # Fill out your answer here. Do not include exit 0 in your code.
    return                     
}                              

function part_3
{
    # Fill out your answer here. Do not include exit 0 in your code.
    return
}


# To test your function, you can call it below like this:
#
part_1
# part_2
# part_3
