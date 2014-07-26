#!/bin/python2.7
# RPG Dice Roller 
# by grandtheftjiujitsu & Senglis3

import random

diff_dice = raw_input("Do all the dice you want to roll have the same number of sides? (y/n)   ")
if diff_dice == "Y" or diff_dice == "y":
	dice = input("Enter the number of dice:  ")
	sides = input("Enter number of sides on each die:  ")
	def roll():
		result = random.randint(1,sides)
		print result
	count = 0
	while count < dice:
		roll()
		count = count + 1
elif diff_dice == "N" or diff_dice == "n":
	dice4 = input("Number of 4-sided die:  ")
	dice6 = input("Number of 6-sided die:  ")
	dice8 = input("Number of 8-sided die:  ")
	dice10 = input("Number of 10-sided die:  ")
	dice12 = input("Number of 12-sided die:  ")
	dice20 = input("Number of 20-sided die:  ")
	def multi_dice():
		dice4list = []
		dice6list = []
		dice8list = []
		dice10list = []
		dice12list = []
		dice20list = []
		if dice4 == 0:
			pass
		else:
			for x in range(0, dice4):
				term1 = random.randint(1,4)
				dice4list.append(term1)
			print "4-sided Die Results:  %s" % (dice4list)
		if dice6 == 0:
			pass
		else:
			for x in range(0, dice6):
				term2 = random.randint(1,6)
				dice6list.append(term2)
			print "6-sided Die Results:  %s" % (dice6list)
		if dice8 == 0:
			pass
		else:
			for x in range(0, dice8):
				term3 = random.randint(1,8)
				dice8list.append(term3)
			print "8-sided Die Results:  %s" % (dice8list)
		if dice10 == 0:
			pass
		else:
			for x in range(0, dice10):
				term4 = random.randint(1,10)
				dice10list.append(term4)
			print "10-sided Die Results:  %s" % (dice10list)
		if dice12 == 0:
			pass
		else:
			for x in range(0, dice12):
				term5 = random.randint(1,12)
				dice12list.append(term5)
			print "12-sided Die Results:  %s" % (dice12list)
		if dice20 == 0:
			pass
		else:
			for x in range(0, dice20):
				term6 = random.randint(1,20)
				dice20list.append(term6)
			print "20-sided Die Results:  %s" % (dice20list)
	multi_dice()
else:
	quit()