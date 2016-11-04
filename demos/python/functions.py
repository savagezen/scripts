#!/bin/python2.7
# codecademy - Python
# Functions

print "Headers"
print "	Syntax:"
print "		keyword function_name():"
def spam():							# (def)ine the function
	# Comments
	print "Spam!"					# Commmands to be executed
spam()								# Run the function

def square(n):						# (def)ine the function and its argume(n)t
	"""Returns the square of a number"""
	squared = n**2
	print "%d sqaured is %d." % (n, squared)
	return squared
square(10)							# Call the 'square' function with the argument '10'
square(7)
square(22)
square(3.7695)

def power(base,exponent):			# functions can take more than one argument
	result = base**exponent
	print " %d to the power of %d is %d" % (base, exponent, result)
power(4,23)						# run the function with both arguments

print "Python has its own set of modules it can import"
print "	One such module is \"math\""
print "	[Generic Imports] are called with \"import\""
import math
print "	the use syntax would be module.function(argument)"
print "		For Example:  \"print math.sqrt(25)\" produces \"5\""
print math.sqrt(25)
print "	[Function Imports] call a specific function rather than the entire module"
print "		Syntax:	from module import <function>"
print "		Example: from math import sqrt"
print "		This is done so you don't have to type \"math.sqrt()\" every time"
from math import sqrt
print "	Now you can just type \"sqrt()\""
print sqrt(25)
print " [Universal Imports] allow us to call all the functions of a module"
print "	and still not have to type out \"module.function()\""
print "		Example:  from module import *"
from math import *
print "	However, you can't have a variable named the same as one of the functions."
print "		And there are quite a few in \"math\":"
everything = dir(math)
print everything

def biggest_number(*args):					# max
	'''will print the largest number in the below arguments'''
	print max(args)
	return max(args)
biggest_number(-10, -5, 5, 10)
'''or'''
max(3,6,5,9,2)
print max
'''or'''
maximum = max(3,6,5,9,2)
print maximum
def smallest_number(*args):
	'''will print the largest number in the below arguments'''
	print min(args)							# min
	return min(args)
smallest_number(-10, -5, 5, 10)
'''or'''
min(4,7,8,5,1)
print min
'''or'''
minimum = min(4,7,8,5,1)
print minimum
def distance_from_zero(arg):
	'''will print the distance the argument is from zero'''
	print abs(arg)							# absolute value
	return abs(arg)
distance_from_zero(-10)
'''or'''
abs(-57)
print abs
'''or'''
absolute_value = abs(22)
print absolute_value
											# type (of data)
print type(42)							# integer ('int')
print type(4.2)							# float / decimal ('float')
print type('spam')						# string ('str')

def shut_down(s):						# function shut_down takes one argument; s
	if s == "yes":
		return "Shuttding Down"			# if "yes" then return "Shutting Down"
	elif s == "no":
		return "Shutdown Aborted"		# if "now" then return "Shutdown Aborted"
	else:
		return "Sorry"					# return "Sorry" if anything else
from math import sqrt
print sqrt(13689)
def distance_from_zero(x):				# function distance_from_zero take one argument; x
	if type(x) == init or type(x) == float:		# If (x) is an integer or float data
		return abs(x)							# Return absolute value
	else:
		return "No"