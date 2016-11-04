#!/bin/sh

echo "Enter a name for temporary test file:  "
read FILE

echo "Enter a random sentence to work with:  "
read STRING

echo $STRING > /tmp/$FILE

echo "Enter a word for the sentence to search for:  "
read SEARCH

echo "Enter a word to replace the searched for word with:  "
read REPLACE

echo "File Contents:  " && cat /tmp/$FILE
echo "Running sed..."
sed s/$SEARCH/$REPLACE/g /tmp/$FILE
# s/search/replace/				substitute first string occurence in line
# s/search/replace/g				substitute all stirng occurences in line
# 1,3s/search/replace/g				substitute all string occurences in a reance of lines
# -i s/search/replace/g				save changes for string change (DANGEROUS)
# -i s/search/replace/g target.file > save.file
# with just s/.../ MUST inlcude trailing /

echo "Checking File Contents:"  && cat /tmp/$FILE
echo "No changes have been saved"

echo "Running sed again..."
sed s/$SEARCH/$REPLACE/g /tmp/$FILE > /tmp/sed.test2
echo "Changes saved in /tmp/sed.test2"
echo "New File Contents:"
cat /tmp/sed.test2

