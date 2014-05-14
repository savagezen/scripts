#!/bin/python2.7
# codecademy - Python
# Conditionals & Control Flow

print "There are six comparators that can result in a Boolean (T/F) variable"
print "	(==)	Equal to"
3 == 3
2**2 == 2 + 2
False = not True
print "	(!=)	Not equal to"
True != False
True != (not True)
27 / 6 != 5
print "	(<)	Less than"
3 < 5
print "	(>)	Greater than"
5 > 3
print "	(<=)	Less than or equal to"
5 <= 5
print "	(>=)	Greater than or equal to"
print "True Example:"
print "	bool_true = True"
print "	bool_true = 2 + 2 == 4"
print "False Example:"
print "	bool_false = False"
print "	bool_false = -1 >= 25"
print "Boolean Oerators:"
print "Evaluation_Order = \"not and or\" == True"
print "	(and) Checks if both statements are True"
True and (not False)
(2 + 2 == 4) and (5 >= 5)
print "		True and True is True"
print "		True and False is False"
print "		False and True is False"
print "		False and False is False"
print "	(or) Checks if at least one statement is True"
True or False
print "		True or True is True"
print "		True or False is True"
print "		False or True is True"
print "		False or False is False"
print " (not) Gives opposite of the statement"
print "		Not True is False"
print "		Not False is True"
print "	Expressions in () are read as own unit"
bool_1 = False or not True
bool_2 = False and not True or True
bool_3 = True and not (False or False)
bool_4 = not not True or False and not True
bool_5 = False or not (True and True)
print "Putting it all together:"
def the_true_function(True):
	if True and (5 == 5):
		print "True"
	elif False and (not True):
		print "False"
	else:
		print "Unknown"
print "def the_function():"
print "	if condition1:"
print "		do something"
print "	elif condition2:"
print "		do something else"
print "	else:"
print "		otherwise do this"