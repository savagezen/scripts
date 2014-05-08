#!/bin/sh

# Command Execution Order

# Using "&&"
echo "Command1 && Command2
  - Command2 is executed after Command1 returns successful status
  - \"If this command works\" && \"Then execute this command\""
echo "Enter name of a test directory (TestDir):" && read TESTDIR
mkdir /tmp/$TESTDIR
echo "Enter the name of another test directory (TestDir2):" && read TESTDIR2
mkdir /tmp/$TESTDIR2
echo "Enter name of test file (test.file):" && read FILE
touch /tmp/$TESTDIR/$FILE
echo "Copying $FILE from $TESTDIR to $TESTDIR2"
cp /tmp/$TESTDIR/$FILE /tmp/$TESTDIR2/ && echo "If you're reading this then cp was successful. \n"
echo "Here's another test..."
ping -c 3 www.google.com > /tmp/google.ping && echo "Ping Results..."
cat /tmp/google.ping
sort /tmp/google.ping > /tmp/ping.sorted && echo "Testing Sort... "
cat /tmp/ping.sorted

# Using "||"
echo "\n Command1 || Command2
  - Command2 is executed if Command1 fails
  - \"If this command fails\" || \"Then execute this command\"
Test:  Trying to copy a non-existent file"
cp /tmp/fake.file /tmp/$TESTDIR/ || echo "If you're reading this then cp failed \n"

# Grouping COmmands with "{}" and "()"
echo "To run list of commads in current shell:
  - enclose in round brackets \"()\"
  - separate each command with \"; \"
  - Example:  (Command1; Command2; ..)
To run list of of commands in sub-shell:
  - same as above but enclose in curly brackets \"{}\"