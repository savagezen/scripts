#!/bin/sh

# Pipes and Input / Output Redirection

echo  -e "A pipe, \"|\" take the output from the left side command and uses it as input for the right side command:
  ls ~/ | grep Documents
    *the output of \"ls\" is used as the input for the \"grep\" search \n"
echo "\"tee\" is used to redirect the output of a command to a file:
  who | tee /tmp/who.output"
  who | tee /tmp/who.output
  cat /tmp/who.output
echo -e "File Descripter Codes:
    Input file - standard input = 0
    Output file - standard output = 1
    Error out put file - standard error = 2
  Standard Input:
    Where input goes into command (default is keyboard)
  Standard Output:
    Where output from commands goes (default is screen but can be sent to file)
  Standard Error:
    Where errors from command go (default is screen but can be sent to file) \n"
echo "Rdirection:
  command > filename = send standard output to filename"
ls / > /tmp/ls.root && cat /tmp/ls.root
echo "  command >> filename = send standard output to end of file"
ls -la / >> /tmp/ls.root && cat /tmp/ls.root
echo "  command > filename 2>&1 = send standard out put, including errors, to filename
  command < filename > filename2 = command gets input from filename and sends output to filename2"
