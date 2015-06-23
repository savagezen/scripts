#!/bin/zsh
# Unlog GPG encrypted file and untar it as well

LOCKED=$1
ZIPPED=$(echo $1 | head -c -5)

# Ungpg the file
gpg -o $ZIPPED -d $1

# Untar
tar -xvf $ZIPPED

# Clean Up
rm $LOCKED
rm $ZIPPED

