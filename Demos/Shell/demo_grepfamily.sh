#!/bin/zsh
# Unix and Linux Shell Programming (Tansley)
# Chapter 8:  The Grep Family

echo -e "Example:  find number of lines lines containing XX in file AA
Command:  grep -c \"XX\" AA \n
Enter search term or characters:"
read query
echo "Enter (create) a filename to search:"
read path
touch /tmp/$path
echo "$query" > /tmp/$path
exec grep -c "$query" $path
echo -e "Example 2: find what line numbers match query
Command:  grep -n \"XX\" AA \n
Enter Example2 commands using the same query term and file/path:"
read example2
$example2
echo -e "Example 3: find all lines that do NOT match query
Command:  grep -v \"XX\" AA \n
Enter Example3 commands using the same query term and file/path:"
read example3
echo "non matching li.ne" >> /tmp/$path
$example3
echo -e "Example 4: query followed by <tab> and literal string
Command 1:  grep \"XX<tab>\" AA
Command 2:  grep \"XX\>\" AA \n
Lets try searching all files in $HOME that were accessed this month.
Enter username:" 
read user
date
echo "Enter the current month:"
read month
echo "Command To Be Executed:  ls -l /home/$user | grep \"$month\>\""
ls -l /home/$user | grep "$month\>"
echo "Grep is case sensitive by default, let's turn that off.
Enter the current month in all lower-case letters:"
read month2
echo "Command To Be Executed:  ls -la /home/$user | grep -i \"$month2\""
ls -la /home/$user | grep -i "$month2"
echo "Example 4.5:  The same can be done with regular expressions
Command:  ls -l /home/$user | grep \"[Ss]ept\"
  Regular Expression Reminder:
	^	Dont query start of line
	[]	Range
	.	Single character
	*	Any number of characters
Example 5:  list diles (and directories) in /home/$user that were accessed between May 10 and May 19
Command:  ls -l /home/$user | grep -i "$month.1[0-9]""
ls -l /home/$user | grep -i "$month.1[0-9]"
echo "The \"ps\" command is used for processes:
  \"ps -ax\" lists all processes running on the system
Example 6:  See if a gertain program / application is running.
Enter the name of an application:" read process
$process
echo "Command:  ps -ax | grep "$process""
ps -ax | grep "$process"