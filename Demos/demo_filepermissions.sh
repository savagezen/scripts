#!/bin/sh

# File Permission Reference

echo -e "To create file, execute \"touch /path/to/my.file\"\n
Change file permissions with \"chmod\" command \n
Syntax = \"chmod parties permission /path/to/my.file\"\n"
echo -e "  Parties:
    u = user - user executing command
    g - group - groups that the executing user belongs to
    o = other - other users
    a = all \n"
echo -e "  Operator:
    + = add following permisison(s) for previous user(s)
    - = remove following permission(s) for previous user(s)\n"
echo -e "  Permissions:
    r = read / cat file
    w = write - edit / delete file
    x = execute file \n"
echo "Numerical Permissions Reference:
  Syntax = chmod #### /path/to/file
    0400 = allow OWNER to READ
    0200 = allow OWNER to WRITE
    0100 = allow OWNER to EXECUTE
    0040 = allow GROUP to READ
    0020 = allow GROUP to WRITE
    0010 = allow GROUP to EXECUTE
    0004 = allow OTHER to READ
    0002 = allow OTHER to WRITE
    0001 = allow OTHER to EXECUTE
  Digits:
    First Digit:  set setuid, setgid, or sticky
    Second Digit: set owner permisison
    Third Digit: set group permisison
    Fourth Digit: set other permission
  Values:
    4 = r (Read)
    2 = w (Write)
    1 = x (eXecute)
    7 = rwx (Read, Write, eXecute)
    6 = rw (Read, Write)
    5 = r-x (Read, eXecute)"