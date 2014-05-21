#!/bin/sh
# Unix and Linux Shell Programming (Tansley)
# Chapter 7:  Introducing Regular Expressions

echo "Metacharacters for [grep], [awk], and [sed]:
  ^ 			Will match the beeginning of line only
  $ 			Will match end of line only
  * 			Match zero or more occurances
  []			Characters enclosed in [] will be matched
  \ 			Escape spcial meaning of metacharacter
  .			Matching any single character
  pattern \{n \}	Match specific numbe rof occurences (n) that contain (pattern)
  pattern \{n,\}m	Match at least (n) occurences of preceeding (pattern)
  pattern \n,m\}	Match any number of occurences between (n) and (m) of (pattern)"
echo -e "Example 1:  Search for executables in ~/ \n
cd ~/ && ls -l ..x..x..x"
cd ~/ && ls| grep ..x..x..x
echo -e "Example 2: search files in ~/ owned by $user \n
Enter Username:" read user
echo -e "12 periods(.) follwoed by $user \n
Really, this is searching for files where the 13th letter of the stdout from \"ls -l ~/\" is the first letter of the $user \n
Command:  ls -l|grep ...........$user"
ls -l| grep ............$user
echo "Enter folder name:"
read folder
echo -e "Example 3: search for directories in $folder \n
Command:  ls -l $folder| grep ^d"
ls -l $folder| grep ^d
echo  -e "Example 4:  search for specific file type inside $folder \n
Enter file extension (.txt):" read ext
echo "Command:  ls -l $folder| grep $ext$"
ls -l $folder| grep $ext$
echo  "Use \"[]\" for specifying ranges
  [0-9]		Match any number
  [a-z]		Match any lower case letter
  [A-Z]		Match any upper case letter
  [A-Za-z]	Match any letter
  [A-Za-z0-9]	Match any letter or number"

