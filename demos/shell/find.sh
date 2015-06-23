#!/bin/sh

# using "find"

echo -e "Syntax = \"find SearchStart SearchMethod "SearchEntry" -options\" \n"
echo -e "SearchStart = where you want \"find\" to start looking.
	. = current directory \n"
echo  -e "SearchMethod = method of finding
	-name = find files by filename
	-perm = find files by permissions
	-user = find file by user owner
	-group = find file by group membership
  	-type = find files that are a certain type, like
    		b - a block flie
    		d - a directory file
    		c - a character file
    		p - a pipe file
    		l - a symbolic linked file
    		f - an ordinary file
  	-fstype = find files on a certain file system type
  	-mount = find only files on mounted file systems
  	-foll0w = follow symbollic links \n"
echo -e "SearchEntry = what you're looking for inside quotations \n"
echo -e "Options = what you want to do if what you're looking for is found
  	-print
  	-exec
  	-ok \n"
echo "Enter a file to be created and then searched for (ex: my.file):"
read -s NAME
cd /tmp && touch $NAME

echo "Enter where to start looking (ex: / [root], ~ [home], . [current dir]):"
read -s START

echo "Enter how to search (ex: name):"
read -s METHOD

echo "Enter query inside quotation marks and wildcards if needed (ex: \"my*\"):"
read -s QUERY

echo -e "Enter what to do if query is found (ex: print): \n"
read -s OPTION

SEARCH="find $START -$METHOD $QUERY -$OPTION"
echo "Command Entered: $SEARCH"
echo "Searching...."
exec $SEARCH