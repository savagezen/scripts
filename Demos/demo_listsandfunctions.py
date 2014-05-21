#!/bin/python2.7
# codecademy - Python
# Lists and Functions

# List Review
n = [1, 2, 3]
print "Print specifc element of list:  list[index]"
print n[2] # indexes start at 0; 1st element = n[0]
print "Edit an element by redefining it:  list[index] = list[index] * 5"
n[2] = n[2] * 5
print n
print "Add item to end of list: list.append(new_item)"
n.append(4)
print n
print "Remove item and return value found at index: list.pop(index)"
n.pop(3)
print n
print "Remove actual item:  list.remove(item)"
n.remove(2)
print n
print "Remove item at index but do not return anything: del(list[index])"
del(n[1])
print n

# Function Review
number = 5
def my_function(x): # def function_name(argument)
  return x * 3 # Math: * + / -
print my_function(number)
print "Functions can take more than one argument / parameter:"
print " m = 5"
m = 5
print " n = 13"
n = 13
print "   def add_function(x, y):"
print " 	return x + y"
print "   print add_function(m, n)"
def add_function(x, y):
  return x + y
print add_function(m, n)
print "Strings and functions:"
n = raw_input("Enter a random word: ")
print " def string_function(s):" # function taking the argument "s"
print "   return s + \" pies\""
print " print string_fucntion(n)"
def string_function(s):
  return s + " pies"
print string_function(n)

# Using Functions With Lists
print "Using a list as an argument in a function is esentially the same as a string"
print "	def list_function(x):"
print "		return x"
print "	n = [3, 5, 7]"
print "	list_function(n)"
def list_function(x):
	return x
n = [3, 5, 7]
print list_function(n)

print "You can also select specific indexes of the list"
print "	return... x[index]" 
def list_function(x):
	return x[1]					# See "n" above
list_function(n)

print "And you can modify the lists similarly"
print "	def add_three(x):"
print "		x[1] = x[1] + 3"
print "		return x"
print "	n = [3, 5, 7]"
def add_three(x):
	x[1] = x[1] + 3				# See "n" above
print list_function(n)

print "And of course appending (adding to the end of) a list isn't differenent either"
print "	def list_extender(lst):"
print "		lst.append(9)"
print "		return lst"
print "	print list_extender(n)"
def list_extender(lst):
	lst.append(9)
	return lst
print list_extender(n)			# See "n" above

# Using an Entire List in the Function
print "You can use the entire list in a function"
print "	For example:  printing out each entry in a list"
print "	def print_list(x):"
print "		for index in range(0, len(x)):"
print "			print x[index]"
print "	print_list(n)"
def print_list(x):				# See "n" above
	for index in range(0, len(x)):
		return x[index]
print print_list(n)

print "	Or multiplying each item in a list by 2"
print "		def double_list(x):"
print "			for index in range(0, len(x)):"
print "				x[index] = x[index] * 2"
print "			return x"
print "		print double_list(n)"
def double_list(x):			# See "n" above
	for index in range(0, len(x)):
		x[index] = x[index] * 2
	return x
print double_list(n)

print "range() is used to allow ranges everywhere you can lists"
print "	Example:  range(6) => [0,1,2,3,4,5]"	# range(stop)
print "	Example:  range(1,6) => [1,2,3,4,5]"	# range(start, stop); start default = 1
print " Example:  range(1,6,3) => [1,4]"		# range(start, stop, step); step default = 1
print double_list(range(3))						# range starting at 0, ending not including 3, steps of 1

print "Ways if iterating through a list:"
print "	Method 1:  for item in list:"			# easier but causes problems when trying to edit list
print "					print item"
print "	Method 2:	for i in range(len(list)):"
print "					print list[i]"
print "	Adding the contents of a list:"
n1 = int(input("Pick a number between 0 and 9: "))
n2 = int(input("Pick a number between 0 and 9: "))
n3 = int(input("Pick a number between 0 and 9: "))
numbers = [n1, n2, n3]
print "		numbers = " + numbers
print "		def total(numbers):"
print "			result = 0"
print "			for x in numbers:"
print "				result = result + x"		# This can also be done with strings (words)
print "			return result"
print "		total(numbers)"
def total (numbers):
	result = 0
	for x in numbers:
		result = result +x
	return result
total(numbers)
print "Using lists in a funciton is no differnet from using multiple arguments"
print "	m = [1, 2, 3]"
print "	n = [4, 5, 6]"
print "	def join_lists(x, y):"
print "		result = x + y"
print "		return result"
print "	print join_list(m, n)"
m = [1, 2, 3]
n = [4, 5, 6]
def join_lists(x, y):
	result = x + y
	return result
print join_lists(m, n)
print "Perhaps we want to join lists..."
print "	list_of_lists = [[1, 2, 3], [4, 5, 6]]"
print "	def flatten(lists):"
print "		results = []"
print "		for numbers in lists:"
print "			for number in nujmbers:"
print "				results.append(number)"
print "		return results"
print "	print flatten(list_of_lists)"
list_of_lists = [[1, 2, 3], [4, 5, 6]]
def flatten(lists):
	results = []
	for numbers in lists:
		for number in numbers:
			results.append(number)
	return results
print flatten(list_of_lists)