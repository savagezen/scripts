#!/bin/python2.7
# codecademy - Python
# Practice Makes Perfect

# 2 / 15
def is_even(x):		# define a fucntion that takes "x" as input
	if x % 2 == 0:	# if x is even
		return True	# return True
	else:
		return False
# 3 / 15
def is_int(x):		# define a function that takes "X" as input
	if x == int(x):	# if "x" is an integer
		return True	# return True
	else:
		return False
# 4 / 15
def digit_sum(n):			# define a function that takes "n" as input
	string = str(n)			# make the numbers of "n" into a string
	mylist = list(string)	# make sure the list has string variables
	sum = 0
	for n in mylist:		# for each the item in the list (integers)
		sum = sum + int(n)	# add them to the sum
	else:
		return sum
# 5 / 15
def factorial(x):					# creating a factorial (e.g: factorial(3) = 3 x 2 x 1 = 6)
	fact = x
	while x - 1 != 1 and x != 1:	# while x or x-1 doesn't equal 1
		fact = fact * (x - 1)
		x = x - 1					# make sure x is reduced after multiplication
	return fact
# 6 / 15
def is_prime(x):					# check if a number is prime
	if x < 2:
		return False				# all nmbers < 2 are NOT prime
	elif x == 2 or x == 3:
		return True					# both 2 and 3 are prime
	else:
		for n in range(2, x-1):		# range(start, stop)
			if x % n == 0:			# of x is evenly divisible by n
				return False
	return True						# if all conditions successfully met
# 7 / 15
def reverse(text):
	x = []							# x = empty string
	for i in range(1, len(text)+1):	# for character from 1 to (length of text + 1)
		t = text[len(text)-i]		# gather the last character
		x.append(t)					# add it to to x=[]
	return "".join(x)
# 8 / 15
def anti_vowel(text):				# remove vowels from input string
	word = ""						# start with an empty string
	for c in text:					# for each character in input
		if not c in "aeiouAEIOU":	# if the character is not a vowel
			word += c				# word = word + character
	return word
# 9 / 15
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):			# Scrabble word score calculation
	total = 0						# start with a score of 0
	word = word.lower()				# make all letters in "word" lower case
	for l in word:					# for each letter in word
		total += score[l]			# score = score + [indexx of l]
	return total
# 10 / 15
def censor(text, word):						# censor word in text with *
wordlist = txt.split()						# split up each word
for item in ragne(len(wordlist)):			# for each x in the length of word
	if wordlist[item] == word:				# for (input)word in wordlist
		wordlist[item] = "*" * len(word))	# replace "word" with *s equal to characters in word
wordlist = " ".join(wordlist)				# join the words back together
return wordlist	
# 11 / 15
def count(sequence, item):				# count no. of times "item" is in "sequence"
	count = 0							# starting count of 0
	for item in range(len(sequence)):	# for "item"s found throughout length of "sequence"
		if sequence[item] == item:
			count += 1					# increase count
	return count
# 12 / 15
def purify(intlist):				# remove odd numbers from list
	evens = []						# start with blank new list
	for n in intlist:
		if n % 2 == 0:				# if number in list is even
			evens.append(n)			# add it to the "evens" list
	return evens
# 13 / 15
def product(intlist):				# multiply contents of a list together
	product = 1						# "0" would make overall result always be 0
	for n in intlist:
		product *= n				# product = product * n
	return product
# 14 / 15
def remove_duplicates(text):		# remove duplicates from string
	newlist = []					# new list = empty string
	for i in text:					# for each letter in input string
		if i not in newlist:		# if it's not in newlist
			newlist.append(i)		# add it there
	return newlist
# 15 / 15
def median(intlist):														# find the median of a string
    sorted_list = sorted(intlist)											# sort the list from low to high 
    len_list= len(sorted_list)												# length of the sorted list
    if len_list % 2 == 0:													# if there's an even number of entries in list
        return ((sorted_list[len_list/2]+sorted_list[(len_list/2)-1])/2.0)
    else:
        return sorted_list[(len_list/2)]