#!/bin/python2.7
# RPG Dice Roller

import random

dice = int(input("Enter the number of dice:  "))
sides = int(input("Enter number of sides on each die:  "))


def roll():
	result = random.randint(1,sides)
	print result

count = 0
while count < dice:
	roll()
	count = count + 1