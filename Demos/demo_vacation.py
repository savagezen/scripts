#!/bin/python2.7
# codecademy - Python
# Taking a Vacation

def answer():							# Review, (def)ine function without argument
	return 42							# That returns "42"

def hotel_cost(nights):					# Define hotel cost in terms if nights
	return 140 * nights					# Cost = 140 / night

def plane_ride_cost(city):				# plane cost defined by city
	if city == "Charlotte":
		return 183						# $183 if flight as crom Charlotte
	elif city == "Tampa":
		return 220
	elif city == "Pittsburgh":
		return 222
	elif city == "Los Angeles":
		return 475

def rental_car_cost(days):
	if days >= 3 and days < 7:			# There is a discount for renting for 3 or more days
		return (40 * days) - 20
	elif days >= 7:						# There is a discount for renting for 7 or more days
		return (40 * days) - 50
	else:								# You cannot get both discounts
		return 40 * days				# The rate for < 3 days is 40 / day

def trip_cost(city, days, spending_money):		# Total trip cost
	return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print trip_cost("Los Angeles", 5, 600)