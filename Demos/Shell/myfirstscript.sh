#!/bin/zsh

$ vi How to Write a Simple Shell Script
#
#
# Add Notes Here....
#
clear
echo "**********Writing a Simple Shell Script**********

This is a guide I wrote as my first shell script.  It is a simple guide to show how to write a shell script that will display a quoted text on the command prompt screen.

!!!DISCLAIMER!!! - This script was tested on Linux Mint 14 and is my frist script.  YOU assume all responsibility of your system when following any instructions herein**

1 - Open a file editor, such as gedit, and save a file with a name like -- MyShellScript.sh (The .sh suffix is to easily identify the file as a shell script but is not required)

2 - Save, exit, and go back to the command prompt.  Give permissions to [file name] by typing --

chmod ugo+x [file name] | chmod ug+r [file name] | chmod u+w [file name] [enter]

-- The first part will allow (add [+])the file owner/user (u), groups the owner is in (g), and other system users (o) to execute the script.  The | symbol is used to connect commands and is usally found above the return key on American keyboards.  The second part allows the owner and groups to read/view (r) the file.  The second part allows only the user to write/edit (w) the file.  Feel free to adjust accordingly.

3 - Now enter these commands --

bash [file name] [enter]
sh [file name] [enter]
./[file name] [enter]
. [file name] [enter]

-- you can also pipe (|) the commands together if you'd like.  I separated them for clarity.

4 - Reopen [file name] with gedit or other text editor and type the following into the text file contents --

$ vi [file name]
#
# [any notes you want to add to yourself]
#
clear
echo [quotation] [text you want to be displayed] [quotation]

F.Y.I. ONLY - don't type this in the file!
-- $ vi [file name] starts vi file editor
-- # followed by any text is not read
-- clear - clears the screen
-- echo - prints the quoted message

5 - Save, exit, and enter the following command to run the script --

./[file name]

-- If you have saved the file to a directory other than ROOT (/) you will need to adjust the command and filepath accordingly.  i.e. /home/username/Documents/filename

** This information can also be found at www.java-samples.com/showtutorial.php?tutorialid=1326 ** I am not affiliated with the website in any way.  ENJOY!"
