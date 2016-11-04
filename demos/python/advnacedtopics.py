#!/bin/python2.7
# codecademy - Python 2.7
# Advanced Topics


# Dictionary review
dictionary = {
	"Key1" : 1,
	"Key2" : 1.5,
	"Key3" : "A"
	}
print dictionary.items()		# prints pairs [ ("key", "value"), ("key", "value"), ("key", "value") ]
print dictionary.keys()		# prints only keys
print dictionary.values()		# prints only values

# Print each followed by a space, then its value
for key in dictionary:
	print key, dictionary[key]

# Range of numbers from 0 - 50 inclusive
list1 = range(51)
# Range of even numbers from 0 - 51 inclusive
evens_to_50 = [i for i in range(1) if i % 2 == 0]
print evens_to_50

# List Comprehension -> what just happened above in evens_to_50's definition
# print even squares between 1 and 11
even_squares = [x**2 for x in range(1,11) if (x**2)%2 == 0]
print even_squares
	# cubes of numbers 1 through 10 if cube is evenly divisible by 4
cubes_by_four = [x**3 for x in range (1,11) if (x**3)%4 == 0]
print cubes_by_four

# List Slicing
# [start:end:stride]
# start = inclusive; default = 0
# end = exclusive; default = end of list
# stride = space between items; 2 = every other; default = 1

# Example
l = [i ** 2 for i in range(1, 11)]
print l[2:9:2]
# you can also omit certain indices
print l[3:]			# starts at 4th entry and goes to end in intervals of 1
print l[:2]			# prints only the first two entries; index of 0 and 1
print l[::2]			# starts at beginning, goes to finish, intervals of 2
print l[::-1]			# prints list backwards in intervals of 1; pos = L -> R, neg = R -> L
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]	# exactly what it says, backwards by 10
print backwards_by_tens
to_21 = range(1,22)			# numbers from 1 - 21 inclusive
odds = to_21[::2]			# odd numbers from 1 - 21, via slicing
middle_third = to_21[7:14:]		# middle third, 8 - 14 inclusive

# lambda creates an anonymous function
## don't need to give it a name have a value returned
lambda x: x % 2 == 0
# is the same as
def by_three(x):
	return x % 3 == 0
# filter(lambda ... my_list)
# <filter> uses <lambda> to determine what to filter
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]	# Filter only "Python" from the list
print filter(lambda x: x == languages[2], languages)

squares = [x**2 for x in range(1,11)]				# Print squares rom 1-11 in 30-70
print filter(lambda x: 30<= x <= 70, squares)
# or 
print filter(lambda x: x in range(30,71), squares)

# list numbers divisible by 3 or 5 between 1 and 15
threes_and_fives = [x for x in range(1,16) if x%3 == 0 or x%5 == 0]

# Filter out all Xs from the garbled message
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X" ,garbled )
print message