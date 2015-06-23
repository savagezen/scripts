#!/bin/python2.7
# Codecademy - Python
# Introduction to Classes

print "Python is object oriented"
print "	- manipulates programming constructs called \"objects\""
print "	- objects are single data constructs"
print "		- containing data and functions"
print "	- functions of objects are called \"methods\"\n"

print "Basic classes need only the \"class\" keyword, but needs something to do"
print "	For example:"
print "		class NewClass(object):"
print "			pass\n"					# "pass" is a placeholder

class NewClass(object):					# New Class inhereit from "object"
	pass								# CONVENTION = name classes with Capital Letter

print "You can also define functions inside of a class"
print "	Example:"
print "		class Animal(object):"
print "			def __init__(self):"
print "				pass\n"
class Animal(object):
	def __init__(self):					# CONVENTION = "self" is first parameter in __init__()
		pass

print "Use dot.notation to access attributes of an object"
print "	Example:"
print "		class Square(object):"
print "			def __init__(self):"
print "				self.sides = 4\n"
print "		my_shape = Square()"		# a new instance MUST be created
print "		print my_shape.sides"		# prints "4"
print "	This can also be done outside of the class / function"
print "	>>> zebra = Animal(\"Jeffrey\")"
print "	>>> print zebra.name\n"			# prints the Zebra's name

print "__init__ can be thought of as \"initialize\" - boots up the class"
print "The first argument \"init\" gets refers to the instance object"
print "	Example:"
print "		class Animal(object):"
print "			def __init__(self, name, age, is_hungry):"
print "				self.name = name"
print "				self.age = age"
print "				self.is_hungry = is_hungry"

animal1 = raw_input("Enter a type of animal:  ")
animal2 = raw_input("Enter another type of animal:  ")
animal3 = raw_input("Enter a final type of animal:  ")
print "Name your %s" % (animal1)
name1 = raw_input("")
print "Name your %s" % (animal2)
name2 = raw_input("")
print "Name your %s" % (animal3)
name3 = raw_input("")
print "How old is %s" % (name1)
age1 = raw_input("")
print "How old is %s" % (name2)
age2 = raw_input("")
print "How old is %s" % (name3)
age3 = raw_input("")

class Animal(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

animal1 = Animal(name1, age1)			# Redefining new instances
animal2 = Animal(name2, age2)
animal3 = Animal(name3, age3)

print animal1.name, animal1.age
print animal2.name, animal2.age
print animal3.name, animal3.age

print "Not all variables are always available"
print "	- global variables (above) are always available"
print "	- member variables - available to members of  a class"
print "	- instance variables - available to a certiain instance"

class Animal(object):
	is_alive = True						# Member Variable applies to all members of class
	def __init__(self, name, age):
		self.name = name
		self.age = age
print animal1.name, is_alive
print animal2.name, is_alive
print animal3.name, is_alive

print "\n __init__ doesn't have to be your only funtion, you can make your own"
print "	Example:"
print "		class.....:"
print "			def your_function_name(self):"		# Don't forget the "self" parameter
print "				do_something"					# Do_something self.another_variable


