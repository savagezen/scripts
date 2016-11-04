#!/bin/python/2.7
# codecademy.com - Python
# Loops

##########   
# Review #
##########
print "Reminder: \"for\" loops allow you to iterate through all the elements in a list"
print " Exmple:"
print "   a = [\"List of some sort\"]"
print "   for x in a:"
print "     Do something for every x"
print
name1 = raw_input("Enter a persons name: ")
name2 = raw_input("Enter another name: ")
name3 = raw_input("One more name: ")
name_list = [name1, name2, name3]								# [List]
for x in name_list:
  print x
print
age1 = int(input("Enter the age of Person 1: "))
age2 = int(input("Enter the age of Person 2: "))
age3 = int(input("Enter the age of Person 3: "))
name_dictionary = {name1 : age1, name2 : age2, name3 : age3}	# {Dictionary}
for x in name_dictionary:
	print name_dictionary[x]
print name_dictionary
ages = [age1, age2, age3]										# adding "if"
for age in ages:
	if (age % 2) == 0:
		print "%s is an even number" % age
#################
# Grocery Store #
#################
food1 = raw_input("Enter a food: ")
food2 = raw_input("Enter another food: ")
food3 = raw_input("Enter a third food: ")
price1 = int(input("What's the price of the first food: "))
price2 = int(input("What's the price of the second food: "))
price3 = int(input("What's the price of the third food: "))
prices = {
    food1 : price1,
    food2 : price2,
    food3 : price3,
}
stock = {
    food1 : 1,
    food2  : 5,
    food3 : 0,
}
for key in prices:												# Multiplying an argument through loops
    print key
    print "Price: %s" % prices[key]
    print "Stock: %s" % stock[key]
    
total = 0
for key in prices: 												#Inventory worth
    print (prices[key] * stock[key])
    total =  total + (prices[key] * stock[key])
    print total

shopping_list = [food1, food2, food3]

def compute_bill(food): 										# Cost of grocery bill
	total = 0
	for item in food:
         total = bill_total + prices[item]
	print "Grocery Bill: %s " % total

def compute_bill(food): 										# Adjusted bill, you can't buy what's nt in stock
	total = 0
	for x in food:
		if stock[x] > 0:
			total = total + prices[x]
			stock[x] = stock[x] - 1
		print "Adjusted Bill: %s" % total