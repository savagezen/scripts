#!/bin/sh

# File Substitution

LIST="1 2 3 a b c A B C"

cd /tmp
for i in $LIST
do
  touch on $LIST
done

echo -e "Use brackets [] to match when searching match characters:
  For example:  matching files with \"i\" and \"o\"
    ls [io]*"
  For example: match files wiht a range
    ls [0-9]* \n"
ls /tmp/[0-9]*
echo -e "Use \"!\" as an exclusion
  For example: exclude filenames with 0-9
    ls [!0-9]* \n"
ls /tmp/[!0-9]
echo "To seach for filenames with Captial letters only:
  \"ls [A-Z]*\"
To search for filenames with lowercase letters only:
  \"ls [a-z]*\"
To search for filenames with that start with captial and lowercase letters:
  \"ls [Aa]*\""