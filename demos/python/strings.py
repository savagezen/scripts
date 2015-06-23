#!/bin/python2.7
# codeacademy.com - Python
# Strings and Console Output

print "There are three ways to define a string"
print "  my_string = \"string\""
my_string = "string1"
print my_string
print "	my_string = \'string\'"
my_string = 'string2'
print my_string
print "	str(my_string) - which is also used to make a string out of a non-string"
notstring = 1.2345
print str(notstring)

print "Of course strings can have more than one word"
print "	my_string = \"Hello World\""
print "Some characters like \" and \' will break the code because Python thinks its the end of the string"
my_string = "Hello World"
print my_string

print "Indexes can be used to define parts of strings also"
print " If you wante c = c ..."
print "   c = \"cats\"[0]"
print " The index is a reference to the [N]th letter if you were to start counting at \"0\" rather than \"1\""
c = "cats"[0]
# Quotes not needed since index is what's printed
print c

print "To get the number of  in a scharacters in a string you need to use ()len.  Where the variable is inside ()."
lendemo = raw_input("Enter a combination of upper and lowercase letters:")
print len(lendemo)
print "There are two other string methods"
print "	your_variable.upper() - converts all chacater to uppe case letters"
upperdemo = lendemo
print upperdemo.upper()
print "	your_variable.lower() - converts all chacaters to lower casae letters"
lowerdemo = upperdemo
print lowerdemo.lower()

print "You can use str() to combine string and no-string variables"
color = raw_input("What is your favorite color?")
color_string = "Your favorite color is "
print color_string + str(color)

print "%s is used to substitute for string variables."
name = raw_input("What is your name?")
print "Hello %s" % (name)
print "Of course mulitple variables can be defined if quoted and seaparated by commas within ()"
print "Your name is %s and your favorite color is %s" % (name, color)