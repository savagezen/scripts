#!/bin/python2.7
# codecademy - Python
# PygLatin

print "Welcome to the Pig Latin Translator!"

pyg = "ay"
word = raw_input("Press \'Enter\' then type a word and press \'Enter\' to submit:")
original = raw_input()
empty_string = ""
# Check that user has entered alphabetical characters
if len(original) > 0 and original.isalpha():
# variable.isalpha() checks for numbers in "variable"
	print "You entered: " + original
else:
	print "Error:  No text entered"
word = original.lower()
first_letter = word[0]
new_word = word[1:] + original[0] + pyg
print "Pig Latin Translation: " + new_word