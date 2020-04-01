#! /bin/bash

# ############################################################################
#
#   This is a common way of commenting in Bash, where the comments are boxed
#   to give a quick clue of the beginning of a script.
#   
#   Author:     <Something goes here!>
#   Purpose:    <Something else goes here!>
#   Date:       <You got the point!>
#   ...
# ############################################################################

# ############################################################################
# man - The Bash Command Manual     (Press 'Q' to leave)
# ############################################################################
man ls

# Basic Shell Commands
# ####################

# cd - Change Directory
cd ~                        # Changes to the user home from anywhere.
cd Documents                # Changes to sub-folder Documents

# ls - List Directory Contents
ls                          # list files in current path 
ls Documents                # list files in "Documents"
ls *.sh                     # list all files ending in .sh
ls foo*                     # list all files starting with foo
ls -l                       # list files in formatted list (with more info such as date and permissions) 
ls -a                       # list list all files (including hidden files) in current path
ls  --sort=WORD             # sort by WORD instead of name. Options are: none, extension, size, time, version

# cp - Copy Files and Directories
cp fileA fileB              # copy fileA into fileB
cp *.c dirA                 # copy all files matching *.c into directory dirA 
cp -r dirA dirB             # copy dirA (recursively) into dirB

# mv - Move (Rename) Files
#WARNING:  mv  will  overwrite  any  files  it  gets  as  destination.  
#          -n  will  stop  it  from  overwriting
mv  fileA  fileB            # move (rename) fileA to fileB
mv *.c dirA                 # move all files matching *.c into dirA  
mv dirA dirB                # move dirA (recursively) into dirB

# echo - Display Text
echo "Hello World"          # displays Hello World in the console.
echo                        # displays an empty line.

# File Manipulation
# ####################

# cat - Concatenate and Print Files to stdout
cat languages1.txt          # print (display) fileA's contents in the console
cat -eT languages1.txt      # display fileA's contents, including invisible (tab/newline) characters
cat fileA fileB fileC       # display the contents of the files in order.
cat *.txt                   # display all files that end in .txt, in order.

# head and tail - Print the Start and End of Files
head -n 5 languages1.txt    # print the first 5 lines of fileA
head -c 5 languages1.txt    # print the first 5 characters of fileA
head -n -5 languages1.txt   # print all but the last 5 lines of fileA

tail -n 5 languages2.txt    # print the last 5 lines of fileA
tail -c 5 languages2.txt    # print the last 5 characters of fileA
tail -n +2 languages2.txt   # print all lines of fileA starting at line 2

# egrep - Regular Expression Text Search.
# search through the 'contents' of files and directories.
egrep "foo" languages2.txt  # display all lines that match "foo" in file to the console
egrep "^X" *.txt            # display all lines that match the regex "^H" in files.
egrep -lr "foo" dirA        # display all files in directory dirA that contain the word "foo"
                            # -l stands for list-files, and -r stands for recursive

# cut - Select Sections of a File: select entire columns of tabulated data files.
cut -f1,5 fileA             # select and print columns 1 and 5 of fileA

# select and print, where file is delimited by commas, not tabs
cut -f1,3 -d',' datafiles/AMZN.dat

# sort - Sort a File
sort fileA                  # print fileA with its lines sorted alphabetically.

# wc - Word Count

wc -w fileA                 # print the number of words in fileA 
wc -l fileA                 # print the number of lines in fileA
wc -c fileA                 # print the number of characters in fileA
wc fileA                    # print the number of lines, words, characters in fileA

# Variables:
# All variables and values are by default processed as text strings.
# ####################

# Assignment and Usage
myvar="Hello  World"        # myvar now contains the text "Hello World" (no quotes) 
mynum=5                     # mynum now contains the character '5' (no quotes) 
mylongnum=364               # mylongnum now contains the string "364" (no quotes)

# WARNING: Spaces matter.
# This WILL NOT WORK: No spaces before or after the "="
# brokenvar = Some text
correctvar="Some Text"      # If the text string value contains spaces.

# To use a variable's value, the variable name must be preceded by a '$' sign
echo $myvar                 # display Hello World in the console
echo "$mynum + $mylongnum"    # display the text: 5 + 364

mydir=~/Documents
ls $mydir                   # list all files in ~/Documents
myfile=$mydir"/Examples/Bash/Lecture09_F19/languages1.txt"
cat $myfile                 # display contents of ~/Documents/fileA

# Expression (subshell)
# ####################

# It is often useful to store a command’s output in a variable for use later. 
# In such cases, we create a subshell, a child process of the calling terminal that act like a terminals itself. 
# You can add any code you want to a subshell and its output will be sent back out to the calling shell (bash process)
ls *.txt > list_of_files.txt   # See below for I/O Redirection.
myfiles=$(cat list_of_files.txt)
# * The file "list_of_files.txt" contains filenames that we may want to use later.
# * the $() notation creates a subshell, and runs any code given inside it.
# * its output is sent back out to our calling statement.
# * In this case, it will store it in a variable.

echo  $myfiles              
# $myfiles now includes the text from list_of_files.txt

mv $myfiles $someFolder     # that variable can then be used like any other in commands
ls $someFolder

somefiles=$(egrep lr "ee364[a-g][0-9]{2}") # list all files that contain ee364 IDs
echo $somefiles   
cat $somefiles

# String Manipulation
${#string}                  # String length
${string:idx}               # Substring starting at idx
${string:idx:len}           # Substring starting at idx of length len
${string//regex/repl}       # Replace all matches of regex with the string repl

s=0_2_4_6_8_A_C_E_
echo ${#s}
echo ${s:4}
echo ${s:4:20}
echo ${s//_/:-)}

# IO Redirection: redirect one command's output into a file or even another command's input
# ####################
# > - Write Output to File
echo "Hello World" > fileA    # Writes "Hello World" to fileA.
echo "foo bar" >> fileA       # Appends to fileA.
ls *.txt > list_of_files.txt  # You get the idea!

# |- Pipe Output to Another Command's Input.
# Return a list of all files matching the pattern in the regex
ls -l | egrep "file[A-Za-z][0-9].csv" 

cat regexlines.txt | egrep -f - fileToSearch.txt
echo "ee364[a-g][0-9]\{2\}" | egrep -f - fileToSearch.txt
# * The -f switch to use a file as its regex input
# * RegEx will search for the contents of that file in other files. 
# * The file which we will use to input is stdin (specified by the dash '-' character above).
# * This lets us input regex to egrep from the pipe. 
# * If regexlines.txt contains more than one line, egrep will run multiple times 
#   using each line of the file as a regex pattern.
# Play  around  with  the  above concepts to familiarize yourself with grep's more powerful features. 

# This can be combined with subshells and variables: 
pattern="file[A-Za-z][0-9].csv"
filesfound=$(ls -l | egrep $pattern)
cat $filesfound | cut -d=',' -f1,3 > allfiles_cols_1_3.csv

# Evaluation, Conditionals, and Loops
# ####################
# if []; then expr; else expr; fi

# If statements in Bash look like this:
if [[ $myvar = "some value" ]]
then
    echo "TRUE" 
else
    echo "FALSE" 
fi

# Notice that by default bash will compare string values only
# Partial matches can be done too using regex:
if [[ $myvar = "ee364.*" ]]
then
    echo "TRUE" 
fi

# multiline statements can be combined into a single line using semicolons 
if  [[ $myvar = "some value" ]]; then echo "TRUE"; fi

# the default comparison mode is for text. This will print FALSE
if  [[ 5 < 364 ]]; then echo "TRUE"; else echo "FALSE"; fi

# numerical comparison can be achieved using:
#  '-eq':  equal,  '-ne':  not-equal
#  '-lt':  less-than,  '-gt':  greater-than
#  '-le':  less-than-or-equal,  '-ge':  greater-than-or-equal 
if  [[ 5 -lt 364 ]]; then echo "TRUE"; else echo "FALSE"; fi

# while [[]]; do expr; done
# ####################
cond=$(somecommand)
while [[ $cond != "Done" ]] 
do
    cond=$(somecommand) 
done

# for var in $list; do expr; done
# ####################
# * for-loops in Bash work similarly to Python
# * loop over a list of values than over an index
cfiles=$(ls *.c) 
for f in $cfiles 
do
    gcc $f -o ${f//\.c/.o} 
done

# When put on one line, for-loops store their outputs in variable.
ofiles=$(for f in $cfiles; do echo ${f//\.c/.o}; done)
echo $cfiles
echo $ofiles

# you can iterate over ranges:
for i in {1..5}; do echo i=$i; done

# This will not work with variables. Instead, use the command 'seq' 
mynum=5
for i in $(seq 1 $mynum); do echo i=$i; done

# All Bash scripts should end with an exit statement with a return code.
exit 0