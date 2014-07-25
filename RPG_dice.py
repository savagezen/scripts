#!/bin/python2.7
# RPG Dice Roller

import random

diff_dice = raw_input("Do all the dice you want to roll have the same number of sides? (y/n)   ")
if diff_dice == "N" or diff_dice == "n":
	dice = raw_input("Enter the number of dice:  "))
	sides = raw_input("Enter number of sides on each die:  "))
	def roll():
		result = random.randint(1,sides)
		print result
	count = 0
	while count < dice:
		roll()
		count = count + 1
elif diff_dice == "Y" or diff_dice == "y":
	def multi_dice():
		dice4 == raw_input("Number of 4-sided die: ")
		dice6 == raw_input("Number of 6-sided die: ")
		dice8 == raw_input("Number of 8-sided die: ")
		dice12 == raw_input("Number of 12-sided die: ")
		dice4list == []
		dice6list == []
		dice8list == []
		dice10list == []
		dice12list == []
		dice20list == []
	if dice4 == 0:
		pass
	else:
		for x in range(0, dice4):
			term1 == random.randit(1,4)
			dice4list.append(term1)
		print(dice4list)
	if dice6 == 0:
		pass
	else:
		for x in range(0, dice6):
			term2 == random.randit(1,6)
			dice6list.append(term2)
		print(dice6list)
	if dice8 == 0:
		pass
	else:
		for x in range(0, dice8):
			term3 == random.randit(1,8)
			dice8list.append(term3)
		print(dice8list)
	if dice10 == 0:
		pass
	else:
		for x in range(0, dice10):
			term4 == random.randit(1,10)
			dice10list.append(term4)
		print(dice10list)
	if dice12 == 0:
		pass
	else:
		for x in range(0, dice12):
			term5 == random.randit(1,12)
			dice12list.append(term5)
		print(dice12list)
	if dice20 == 0:
		pass
	else:
		for x in range(0, dice20):
			term6 == random.randit(1,20)
			dice20list.append(term6)
		print(dice20list)
	multi_dice()
else:
	quit()
