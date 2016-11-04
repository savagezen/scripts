#!/bin/python2.7
# codecademy - Python
# Loops 2

################
# "while" loops
################
count = 0

if count < 5:				# if count is < 5 - this will be done
	print "Hello, I am an if statemtne and count is ", count

while count < 5:			# as long as count is < 5 - this will be done
	print "Hello, I am a while and coutn it ", count
	count = count + 1

loop_condition = True		# loop_condition set to True
while loop_condition:		# checks to see if loop_condition equals True
	print "I am a loop"		# print this as long as loop_condition is True
	loop_condition = False	# loop_condition set to False

num = 1
while num < 11:				# can also use "<= 10"
	print num**2			# print evern number from 1 - 10 squared
	num = num + 1			# increment "num"

choice = raw_input("Enjoying the course? (y/n): ")
while choice != "y" and choice != "n":
	choice = raw_input("Sorry, I didn't catch that.  Enter again: ")

print "Random Number Game:"
from random import randint
print "	- A random number between 1 and 10 will be generated"
random_number = randint(1, 10)
print "	- You will have 3 guesses"
guesses_left = 3
while guesses_left > 0:
	guess = int(raw_input("Your Guess: "))
	if guess == random_number:
		print "You Win!"
		break				# will stop loop if above condition is true
	guesses_left = guesses_left -1
	print "Guesses Left: %g" % guesses_left
else:
	print "You Lose."

##############
# "for" loops
##############
print "Counting..."
for i in range(20):
	print i					# print 1 - 19

hobbies = []
for x in range(3):			# will ask a question 3 times
	hobby = raw_input("Enter a hobby: ")
	hobbies.append(hobby)	# add input hobby to "hobbies" list"

word = raw_input("Enter a random word: ")
for x in word:
	print x					# print each letter in the input word

# String Manipulation
phrase = "A bird in the hand..."	# print each letter in the string, but replace some of them
for char in phrase:
	if char == "A" or char == "a":
		print "X",					# replace "A" and "a" with "X".  Without the "," chars will be printed on new line
	else:
		print char,
print								# this is needed to print the entire stirng together
									# For Example:
numbers = [7, 9, 12, 54, 99]
for num in numbers:
	print num**2					# prints each number squared on a new line

# print keys and values in dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
	print key, d[key]				# prints key[word] followed by associated value (separated by a space)
# lists
choices = ['pizza', 'pasta', 'salad', 'nachos']
print "Your chocies are:"
for index, item in enumerate(choices):
	print index+1, item				# start printed index = 1 (rather than 0) at first entry

print "The \"zip\" function is used to compare the length of lists."
print "	Example:"
print "	list_a = []"
list_a = [3, 6, 9, 17, 15, 19]
print "	list_b = []"
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
print "for a, b in zip(list_a, list_b):"
print "	if a > b:"
print "		print a"
print "	else:"
print "		print b"
for a, b in zip(list_a, list_b):		# compare "a"s in "list_a" to "b"s in "list_b"
	if a > b:							# if there are more a's than b's
		print a
	else:
		print b

print "You can also use \"else\" statements in \"while\" loops"
f1 = raw_input("Enter a fruit: ")
f2 = raw_input("Enter another fruit: ")
f3 = raw_input("Enter one more: ")
fruits = [f1, f2, f3]
print "fruits = %s" % (fruits)
for f in fruits:
	if f == "tomato":
		print "Are you sure a tomato is a fruit?"	# it is
		break
	else:
		print f

print "A final sample....."
tests = ["test1", "test2", "test3", "failed"]
print "tests = %s" % (tests)
for x in tests:
	if x != "failed":
		print "testing in progress..."
	else: # x == "failed"
		print "test failed."