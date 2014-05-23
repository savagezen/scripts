#!/bin/python2.7
# Unit Converter - based on Google conversions

error1 = "Error: The unit you selected is not available.  Check your spelling."
error2 = "Error: You slected the same unit as your base and target"
print "Available conversions:"
print "	Temperature"
print "	Length"
print "	Mass"
print "	Volume"
print "	Digital Storage"
print "	Speed"
print "	Area"
print "	Fuel Consumption (Not Yet Supported)"
print "	Time (Not Yet Supported)"
conv_type = raw_input("Select conversion type: ")
###############
# Temperature #
###############
if conv_type == "Temperature" :
	print "Available Units:"
	print "	Degrees Celcius"
	print "	Degrees Fahrenheit"
	print "	Kelvin"
	base = raw_input("Select base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Degrees Celcius":
		if target == "Degrees Fahrenheit":
			value = value * 9
			value = value / 5
			value = value + 32
			print "%s %s" % (value, target)
		elif target == "Kelvin":
			value = value + 273.15
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Degrees Fahrenheit":
		if target == "Degrees Celcius":
			value = int(input("Enter base value: "))
			value = value - 32
			value = value * 5
			value = value / 9
			print "%s %s" % (value, target)
		elif target == "Kelvin":
			value = value -32
			value = value * 5
			value = value / 9
			value = value + 273
			print "%s %s" % (value, target)
	elif base == "Kelvin":
		if target == "Degrees Celcius":
			value = value - 273.15
			print "%s %s" % (value, target)
		elif target == "Degrees Fahrenheit":
			value = value - 305.15
			value = value * 5
			value = value / 9
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	else:
		print error1
##########
# Length #
##########
elif conv_type == "Length":	
	print "Available Units:"
	print "	Kilometers"
	print "	Miles"
	print "	Meters"
	print "	Yards"
	print "	Feet"
	print "	Inches"
	print "	Centimeters"
	base = raw_input("Select base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Kilometers":
		if target == "Miles":
			value = value * 0.621371
			print "%s %s" % (value, target)
		elif target == "Meters":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == "Yards":
			value = value * 1093.61
			print "%s %s" % (value, target)
		elif target == "Feet":
			value = value * 3280.84
			print "%s %s" % (value, target)
		elif target == "Inches":
			value = value * 39370.1
			print "%s %s" % (value, target)
		elif target == "Centimeters":
			value = value * 100000
			print "%s %s" % (value, target)
		elif target == base:
			print error2		
		else:
			print error1
	elif base == "Miles":
		if target == "Kilometers":
			value = value * 1.60934
			print "%s %s" % (value, target)
		elif target == "Meters":
			value = value * 1609.34
			print "%s %s" % (value, target)
		elif target == "Yards":
			value = value * 1760
			print "%s %s" % (value, target)
		elif target == "Feet":
			value = value * 5280
			print "%s %s" % (value, target)
		elif target == "Inches":
			value = value * 63360
			print "%s %s" % (value, target)
		elif target == "Centimeters":
			value = value * 160934
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Meters":
		if target == "Kilometers":
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == "Miles":
			value = value * 0.000621371
			print "%s %s" % (value, target)
		elif target == "Yards":
			value = value * 1.09361
			print "%s %s" % (value, target)
		elif target == "Feet":
			value = value * 3.28084
			print "%s %s" % (value, target)
		elif target == "Inches":
			value = value * 39.3701
			print "%s %s" % (value, target)
		elif target == "Centimeters":
			value = value * 100
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Yards":
		if target == "Kilometers":
			value = value * 0.0009144
			print "%s %s" % (value, target)
		elif target == "Miles":
			value = value * 0.000568182
			print "%s %s" % (value, target)
		elif target == "Meters":
			value = value * 0.9144
			print "%s %s" % (value, target)
		elif target == "Feet":
			value = value * 3
			print "%s %s" % (value, target)
		elif target == "Inches":
			value = value * 36
			print "%s %s" % (value, target)
		elif target == "Centimeters":
			value = value * 91.44
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Feet":
		if target == "Kilometers":
			value = value * 0.0003048
			print "%s %s" % (value, target)
		elif target == "Miles":
			value = value * 0.000189394
			print "%s %s" % (value, target)
		elif target == "Meters":
			value = value * 0.3048
			print "%s %s" % (value, target)
		elif target == "Yards":
			value = value * 0.333333
			print "%s %s" % (value, target)
		elif target == "Inches":
			value = value * 12
			print "%s %s" % (value, target)
		elif target == "Centimeters":
			value = value * 30.48
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Inches":
		if target == "Kilometers":
			value = value * 0.00025399989
			print "%s %s" % (value, target)
		elif target == "Miles":
			value = value * 0.00015782827
			print "%s %s" % (value, target)
		elif target == "Meters":
			value = value * 0.0254
			print "%s %s" % (value, target)
		elif target == "Yards":
			value = value * 0.277778
			print "%s %s" % (value, target)
		elif target == "Feet":
			value = value * 0.0833333
			print "%s %s" % (value, target)
		elif target == "Centimeters":
			value = value * 2.54
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Centimeters":
		if target == "Kilometers":
			value = value * 0.00001
			print "%s %s" % (value, target)
		elif target == "Miles":
			value = value * 0.00000621371
			print "%s %s" % (value, target)
		elif target == "Meters":
			value = value * 0.01
			print "%s %s" % (value, target)
		elif target == "Yards":
			value = value * 0.0109361
			print "%s %s" % (value, target)
		elif target == "Feet":
			value = value * 0.0328084
			print "%s %s" % (value, target)
		elif target == "Inches":
			value = value * 0.393701
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	else:
		print error1
########
# Mass #
########
elif conv_type == "Mass":
	print "Available Units:"
	print "	Metric Tons"
	print "	Stones"
	print "	Kilograms"
	print "	Pounds"
	print "	Ounces"
	print "	Grams"
	print "	Milligrams"
	base = raw_input("Enter base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Metric Tons":
		if target == "Stones":
			value = value * 157.473
			print "%s %s" % (value, target)
		elif target == "Kilograms":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == "Pounds":
			value = value * 2204.62
			print "%s %s" % (value, target)
		elif target == "Ounces":
			value = value * 35274
			print "%s %s" % (value, target)
		elif target == "Grams":
			value = value * 1000000.263
			print "%s %s" % (value, target)
		elif target == "Milligrams":
			value = value * 1000000263
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Stones":
		if target == "Metric Tons":
			value = value * 0.00635029
			print "%s %s" % (value, target)
		elif target == "Kilograms":
			value = value * 6.35029
			print "%s %s" % (value, target)
		elif target == "Pounds":
			value = value * 14
			print "%s %s" % (value, target)
		elif target == "Ounces":
			value = value * 224
			print "%s %s" % (value, target)
		elif target == "Grams":
			value = value * 6350.29
			print "%s %s" % (value, target)
		elif target == "Milligrams":
			value = value * 6350290
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Kilograms":
		if target == "Metric Tons":
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == "Stones":
			value = value * 0.157473
			print "%s %s" % (value, target)
		elif target == "Pounds":
			value = value * 2.20462
			print "%s %s" % (value, target)
		elif target == "Ounces":
			value = value * 35.274
			print "%s %s" % (value, target)
		elif target == "Grams":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == "Milligrams":
			value = value * 1000000
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Pounds":
		if target == "Metric Tons":
			value = value * 0.000453592
			print "%s %s" % (value, target)
		elif target == "Stones":
			value = value * 0.0714286
			print "%s %s" % (value, target)
		elif target == "Kilograms":
			value = value * 0.453592
			print "%s %s" % (value, target)
		elif target == "Ounces":
			value = value * 16
			print "%s %s" % (value, target)
		elif target == "Grams":
			value = value * 453.592
			print "%s %s" % (value, target)
		elif target == "Milligrams":
			value = value * 453492
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Ounces":
		if target == "Metric Tons":
			value = value * 0.0000283495
			print "%s %s" % (value, target)
		elif target == "Stones":
			value = value * 0.00446429
			print "%s %s" % (value, target)
		elif target == "Kilograms":
			value = value * 0.0283495
			print "%s %s" % (value, target)
		elif target == "Pounds":
			value = value * 0.0625
			print "%s %s" % value , target
		elif target == "Grams":
			value = value * 28.3495
			print "%s %s" % (value, target)
		elif target == "Milligrams":
			value = value * 28349.5
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Grams":
		if target == "Metric Tons":
			value = value * 0.000001
			print "%s %s" % (value, target)
		elif target == "Stones":
			value = value * 0.000157473
			print "%s %s" % (value, target)
		elif target == "Kilograms":
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == "Pounds":
			value = value * 0.00220462
			print "%s %s" % (value, target)
		elif target == "Ounces":
			value = value * 0.035274
			print "%s %s" % (value, target)
		elif target == "Milligrams":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Milligrams":
		if target == "Metric Tons":
			value = value * 0.000001
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == "Stones":
			value = value * 0.001
			value = value * 0.000157473
			print "%s %s" % (value, target)
		elif target == "Kilograms":
			value = value * 0.000001
			print "%s %s" % (value, target)
		elif target == "Pounds":
			value = value * 0.001
			value = value * 0.00220462
			print "%s %s" % (value, target)
		elif target == "Ounces":
			value = value * 0.001
			value = value * 0.035274
			print "%s %s" % (value, target)
		elif target == "Grams":
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	else:
		print error1
##########
# Volume #
##########
elif conv_type == "Volume":
	print "Available Units:"
	print "	US Gallons"
	print "	US Quarts"
	print "	US Pints"
	print "	US Cups"
	print "	US Ounces"
	print "	US Tablespoons"
	print "	US Teaspoons"
	print "	Cubic Meters"
	print "	Cubic Feet"
	print "	Cubic Inches"
	print "	Liters"
	print "	Milliliters"
	base = raw_input("Enter base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "US Gallons":
		if target == "US Quarts":
			value = value * 4
			print "%s %s" % (value, target)
		elif target == "US Pints":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "US Cups":
			value = value * 16
			print "%s %s" % (value, target)
		elif target == "US Ounces":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "US Tablespoons":
			value = value * 256
			print "%s %s" % (value, target)
		elif target == "US Teaspoons":
			value = value * 768
			print "%s %s" % (value, target)
		elif target == "Cubic Meters":
			value = value * 0.00378541
			print "%s %s" % (value, target)
		elif target == "Cubic Feet":
			value = value * 0.133681
			print "%s %s" % (value, target)
		elif target == "Cubic Inches":
			value = value * 231
			print "%s %s" % (value, target)
		elif target == "Liters":
			value = value * 3.78541
			print "%s %s" % (value, target)
		elif target == "Milliliters":
			value = value * 3785.41
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US Quarts":
		if target == "US Gallons":
			value = value * 0.25
			print "%s %s" % (value, target)
		elif target == "US Pints":
			value = value * 2
			print "%s %s" % (value, target)
		elif target == "US Cups":
			value = value * 4
			print "%s %s" % (value, target)
		elif target == "US Ounces":
			value = value * 32
			print "%s %s" % (value, target)
		elif target == "US Tablespoons":
			value = value * 64
			print "%s %s" % (value, target)
		elif target == "US Teaspoons":
			value = value * 192
			print "%s %s" % (value, target)
		elif target == "Cubic Meters":
			value = value * 0.000946353
			print "%s %s" % (value, target)
		elif target == "Cubic Feet":
			value = value * 0.0334201
			print "%s %s" % (value, target)
		elif target == "Cubic Inches":
			value = value * 57.75
			print "%s %s" % (value, target)
		elif target == "Liters":
			value = value * 0.946353
			print "%s %s" % (value, target)
		elif target == "Milliliters":
			value = value * 946.353
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US Pints":
		if target == "US Gallons":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "US Quarts":
			value = value * 0.5
			print "%s %s" % (value, target)
		elif target == "US Cups":
			value = value * 2
			print "%s %s" % (value, target)
		elif target == "US Ounces":
			value = value * 32
			print "%s %s" % (value, target)
		elif target == "US Tablespoons":
			value = value * 64
			print "%s %s" % (value, target)
		elif target == "US Teaspoons":
			value = value * 192
			print "%s %s" % (value, target)
		elif target == "Cubic Meters":
			value = value * 0.000473176
			print "%s %s" % (value, target)
		elif target == "Cubic Feet":
			value = value * 0.0167101
			print "%s %s" % (value, target)
		elif target == "Cubic Inches":
			value = value * 28.875
			print "%s %s" % (value, target)
		elif target == "Liters":
			value = value * 0.473176
			print "%s %s" % (value, target)
		elif target == "Milliliters":
			value = value * 473.176
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US Cups":
		if target == "US Gallons":
			value = value * 0.0625
			print "%s %s" % (value, target)
		elif target == "US Quarts":
			value = value * 0.25
			print "%s %s" % (value, target)
		elif target == "US Pints":
			value = value * 0.5
			print "%s %s" % (value, target)
		elif target == "US Ounces":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "US Tablespoons":
			value = value * 16
			print "%s %s" % (value, target)
		elif target == "US Teaspoons":
			value = value * 48
			print "%s %s" % (value, target)
		elif target == "Cubic Meters":
			value = value * 0.00026588
			print "%s %s" % (value, target)
		elif target == "Cubic Feet":
			value = value * 0.00835503
			print "%s %s" % (value, target)
		elif target == "Cubic Inches":
			value = value * 14.4375
			print "%s %s" % (value, target)
		elif target == "Liters":
			value = value * 0.236588
			print "%s %s" % (value, target)
		elif target == "Milliliters":
			value = value * 236.588
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US Ounces":
		if target == "US Gallons":
			value = value * 0.0078125
			print "%s %s" % (value, target)
		elif target == "US Quarts":
			value = value * 0.03125
			print "%s %s" % (value, target)
		elif target == "US Pints":
			value = value * 0.0625
			print "%s %s" % (value, target)
		elif target == "US Cups":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "US Tablespoons":
			value = value * 2
			print "%s %s" % (value, target)
		elif target == "US Teaspoons":
			value = value * 6
			print "%s %s" % (value, target)
		elif target == "Cubic Meters":
			value = value * 0.00002419619
			print "%s %s" % (value, target)
		elif target == "Cubic Feet":
			value = value * 0.00104438
			print "%s %s" % (value, target)
		elif target == "Cubic Inches":
			value = value * 1.80469
			print "%s %s" % (value, target)
		elif target == "Liters":
			value = value * 0.0295735
			print "%s %s" % (value, target)
		elif target == "Milliliterss":
			value = value * 29.5735
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US Tablespoons":
		if target == "US Gallons":
			value = value * 0.00390625
			print "%s %s" % (value, target)
		elif target == "US Quarts":
			value = value * 0.015625
			print "%s %s" % (value, target)
		elif target == "US Pints":
			value = value * 0.03125
			print "%s %s" % (value, target)
		elif target == "US Cups":
			value = value * 0.0625
			print "%s %s" % (value, target)
		elif target == "US Ounces":
			value = value * 0.5
			print "%s %s" % (value, target)
		elif target == "US Teaspoons":
			value = value * 6
			print "%s %s" % (value, target)
		elif target == "Cubic Meters":
			value = value * 0.00002957349
			print "%s %s" % (value, target)
		elif target == "Cubic Feet":
			value = value * 0.00104438
			print "%s %s" % (value, target)
		elif target == "Cubic Inches":
			value = value * 0.902344
			print "%s %s" % (value, target)
		elif target == "Liters":
			value = value * 0.0147868
			print "%s %s" % (value, target)
		elif target == "Milliliters":
			value = value * 14.7868
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US Teaspoons":
		if target == "US Gallons":
			value = value * 0.00130208
			print "%s %s" % (value, target)
		elif target == "US Quarts":
			value = value * 0.00520833
			print "%s %s" % (value, target)
		elif target == "US Pints":
			value = value * 0.0104167
			print "%s %s" % (value, target)
		elif target == "US Cups":
			value = value * 0.020833
			print "%s %s" % (value, target)
		elif target == "US Ounces":
			value = value * 0.166667
			print "%s %s" % (value, target)
		elif target == "US Tablespoons":
			value = value * 0.333333
			print "%s %s" % (value, target)
		elif target == "Cubic Meters":
			value = value * 0.0000049289
			print "%s %s" % (value, target)
		elif target == "Cubic Feet":
			value = value * 0.000174063
			print "%s %s" % (value, target)
		elif target == "Cubic Inches":
			value = value * 0.300781
			print "%s %s" % (value, target)
		elif target == "Liters":
			value = value * 0.00492892
			print "%s %s" % (value, target)
		elif target == "Milliliters":
			value = value * 4.92892
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Cubic Meters":
		if target == "US Gallons":
			value = value * 264.172
			print "%s %s" % (value, target)
		elif target == "US Quarts":
			value = value * 1056.69
			print "%s %s" % (value, target)
		elif target == "US Pints":
			value = value * 2113.38
			print "%s %s" % (value, target)
		elif target == "US Cups":
			value = value * 4226.75
			print "%s %s" % (value, target)
		elif target == "US Ounces":
			value = value * 33814
			print "%s %s" % (value, target)
		elif target == "US Tablespoons":
			value = value * 67628
			print "%s %s" % (value, target)
		elif target == "US Teaspoons":
			value = value * 202884
			print "%s %s" % (value, target)
		elif target == "Cubic Feet":
			value = value * 35.3147
			print "%s %s" % (value, target)
		elif target == "Cubic Inches":
			value = value * 61023.7
			print "%s %s" % (value, target)
		elif target == "Liters":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == "Milliliters":
			value = value * 1000000
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Cubic Feet":
		if target == "US Gallons":
			value = value * 7.48052
			print "%s %s" % (value, target)
		elif target == "US Quarts":
			value = value * 29.9221
			print "%s %s" % (value, target)
		elif target == "US Pints":
			value = value * 59.8442
			print "%s %s" % (value, target)
		elif target == "US Cups":
			value = value * 119.688
			print "%s %s" % (value, target)
		elif target == "US Ounces":
			value = value * 957.506
			print "%s %s" % (value, target)
		elif target == "US Tablespoons":
			value = value * 1915.01
			print "%s %s" % (value, target)
		elif target == "US Teaspoons":
			value = value * 5745.04
			print "%s %s" % (value, target)
		elif target == "Cubic Meters":
			value = value * 0.0283168
			print "%s %s" % (value, target)
		elif target == "Cubic Inches":
			value = value * 1728
			print "%s %s" % (value, target)
		elif target == "Liters":
			value = value * 28.3168
			print "%s %s" % (value, target)
		elif target == "Milliliters":
			value = value * 28316.8
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Cubic Inches":
		if target == "US Gallons":
			value = value * 0.004329
			print "%s %s" % (value, target)
		elif target == "US Quarts":
			value = value * 0.017316
			print "%s %s" % (value, target)
		elif target == "US Pints":
			value = value * 0.034632
			print "%s %s" % (value, target)
		elif target == "US Cups":
			value = value * 0.0692641
			print "%s %s" % (value, target)
		elif target == "US Ounces":
			value = value * 0.554113
			print "%s %s" % (value, target)
		elif target == "US Tablespoons":
			value = value * 1.10823
			print "%s %s" % (value, target)
		elif target == "US Teaspoons":
			value = value * 3.32468
			print "%s %s" % (value, target)
		elif target == "Cubic Meters":
			value = value * 0.00001638704
			print "%s %s" % (value, target)
		elif target == "Cubic Feet":
			value = value * 0.000578704
			print "%s %s" % (value, target)
		elif target == "Liters":
			value = value * 0.0163871
			print "%s %s" % (value, target)
		elif target == "Milliliters":
			value = value * 16.3871
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Liters":
		if target == "US Gallons":
			value = value * 0.264172
			print "%s %s" % (value, target)
		elif target == "US Quarts":
			value = value * 1.05669
			print "%s %s" % (value, target)
		elif target == "US Pints":
			value = value * 2.11338
			print "%s %s" % (value, target)
		elif target == "US Cups":
			value = value * 4.22675
			print "%s %s" % (value, target)
		elif target == "US Ounces":
			value = value * 33.814
			print "%s %s" % (value, target)
		elif target == "US Tablespoons":
			value = value * 67.628
			print "%s %s" % (value, target)
		elif target == "US Teaspoons":
			value = value * 202.884
			print "%s %s" % (value, target)
		elif target == "Cubic Meters":
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == "Cubic Feet":
			value = value * 0.0353147
			print "%s %s" % (value, target)
		elif target == "Cubic Inches":
			value = value * 61.0237
			print "%s %s" % (value, target)
		elif target == "Milliliters":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Milliliters":
		if target == "US Gallons":
			value = value * 0.000264172
			print "%s %s" % (value, target)
		elif target == "US Quarts":
			value = value * 0.00105669
			print "%s %s" % (value, target)
		elif target == "US Pints":
			value = value * 0.00211338
			print "%s %s" % (value, target)
		elif target == "US Cups":
			value = value * 0.00422675
			print "%s %s" % (value, target)
		elif target == "US Ounces":
			value = value * 0.033814
			print "%s %s" % (value, target)
		elif target == "US Tablespoons":
			value = value * 0.067628
			print "%s %s" % (value, target)
		elif target == "US Teaspoons":
			value = value * 0.202884
			print "%s %s" % (value, target)
		elif target == "Cubic Meters":
			value = value * 0.000001
			print "%s %s" % (value, target)
		elif target == "Cubic Feet":
			value = value * 0.00003531465
			print "%s %s" % (value, target)
		elif target == "Cubic Inches":
			value = value * 0.0610237
			print "%s %s" % (value, target)
		elif target == "Liters":
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	else:
		print error1
####################
# Digital Storaget #
####################
elif conv_type == "Digital Storage":
	print "Available Units:"
	print "	Bits"
	print "	Bytes"
	print "	Kilobits"
	print "	Kilobytes"
	print "	Megabits"
	print "	Megabytes"
	print "	Gigabits"
	print "	Gigabytes"
	print "	Terabits"
	print "	Terabytes"
	print "	Petabits"
	print "	Petabytes"
	base = raw_input("Enter base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Bits":
		if target == "Bytes":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Kilobits":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Kilobytes":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == "Megabits":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Megabytes":
			value = value * 1.1921e-7
			print "%s %s" % (value, target)
		elif target == "Gigabits":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == "Gigabytes":
			value = value * 1.1642e-10
			print "%s %s" % (value, target)
		elif target == "Terabits":
			value = value * 9.0949e-13
			print "%s %s" % (value, target)
		elif target == "Terabytes":
			value = value * 1.1369e-13
			print "%s %s" % (value, target)
		elif target == "Petabits":
			value = value * 8.8818e-16
			print "%s %s" % (value, target)
		elif target == "Petabytes":
			value = value * 1.1102e-16
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Bytes":
		if target == "Bits":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "Kilobits":
			value = value * 0.0078125
			print "%s %s" % (value, target)
		elif target == "Kilobytes":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Megabits":
			value = value * 7.6294e-6
			print "%s %s" % (value, target)
		elif target == "Megabytes":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Gigabits":
			value = value * 7.4506e-9
			print "%s %s" % (value, target)
		elif target == "Gigabytes":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == "Terabits":
			value = value * 7.276e-12
			print "%s %s" % (value, target)
		elif target == "Terabytes":
			value = value * 9.0949e-13
			print "%s %s" % (value, target)
		elif target == "Petabits":
			value = value * 7.1054e-15
			print "%s %s" % (value, target)
		elif target == "Petabytes":
			value = value * 8.8818e-16
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Kilobits":
		if target == "Bits":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Bytes":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "Kilobytes":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Megabits":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Megabytes":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == "Gigabits":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Gigabytes":
			value = value * 1.921e-7
			print "%s %s" % (value, target)
		elif target == "Terabits":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == "Terabytes":
			value = value * 1.1642e-10
			print "%s %s" % (value, target)
		elif target == "Petabits":
			value = value * 9.0949e-13
			print "%s %s" % (value, target)
		elif target == "Petabytes":
			value = value * 1.1369e-13
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1		
	elif base == "Kilobytes":
		if target == "Bits":
			value = value * 8192
			print "%s %s" % (value, target)
		elif target == "Bytes":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Kilobits":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "Megabits":
			value = value * 0.0078125
			print "%s %s" % (value, target)
		elif target == "Megabytes":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Gigabits":
			value = value * 7.6294e-6
			print "%s %s" % (value, target)
		elif target == "Gigabytes":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Terabits":
			value = value * 7.4506e-9
			print "%s %s" % (value, target)
		elif target == "Terabytes":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == "Petabits":
			value = value * 7.276e-12
			print "%s %s" % (value, target)
		elif target == "Petabytes":
			value = value * 9.0949e-13
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Megabits":
		if target == "Bits":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Bytes":
			value = value * 131072
			print "%s %s" % (value, target)
		elif target == "Kilobits":
			value = value * 102
			print "%s %s" % (value, target)
		elif target == "Kilobytes":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "Megabytes":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Gigabits":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Gigabytes":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == "Terabits":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Terabytes":
			value = value * 1.1921e-7
			print "%s %s" % (value, target)
		elif target == "Petabits":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == "Petabytes":
			value = value * 1.1642e-10
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Megabytes":
		if target == "Bits":
			value = value * 8.389e+6
			print "%s %s" % (value, target)
		elif target == "Bytes":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Kilobits":
			value = value * 8192
			print "%s %s" % (value, target)
		elif target == "Kilobytes":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Megabits":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "Gigabits":
			value = value * 0.00078125
			print "%s %s" % (value, target)
		elif target == "Gigabytes":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Terabits":
			value = value * 7.6294e-6
			print "%s %s" % (value, target)
		elif target == "Terabytes":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Petabits":
			value = value * 7.4506e-9
			print "%s %s" % (value, target)
		elif target == "Petabytes":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Gigabits":
		if target == "Bits":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Bytes":
			value = value * 1.342e+8
			print "%s %s" % (value, target)
		elif target == "Kilobits":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Kilobytes":
			value = value * 131072
			print "%s %s" % (value, target)
		elif target == "Megabits":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Megabytes":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "Gigabytes":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Terabits":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Terabytes":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == "Petabits":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Petabytes":
			value = value * 1.1921e-7
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Gigabytes":
		if target == "Bits":
			value = value * 8.5e+9
			print "%s %s" % (value, target)
		elif target == "Bytes":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Kilobits":
			value = value * 8.39e+6
			print "%s %s" % (value, target)
		elif target == "Kilobytes":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Megabits":
			value = value * 8192
			print "%s %s" % (value, target)
		elif target == "Megabytes":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Gigabits":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "Terabits":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Terabytes":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == "Petabits":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Petabytes":
			value = value * 1.1921e-7
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Terabits":
		if target == "Bits":
			value = value * 1.1e+12
			print "%s %s" % (value, target)
		elif target == "Bytes":
			value = value * 1.374e+11
			print "%s %s" % (value, target)
		elif target == "Kilobits":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Kilobytes":
			value = value * 1.342e+8
			print "%s %s" % (value, target)
		elif target == "Megabits":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Megabytes":
			value = value * 131072
			print "%s %s" % (value, target)
		elif target == "Gigabits":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Gigabytes":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "Terabytes":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Petabits":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Petabytes":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Terabytes":
		if target == "Bits":
			value = value * 8.796e+12
			print "%s %s" % (value, target)
		elif target == "Bytes":
			value = value * 1.1e+12
			print "%s %s" % (value, target)
		elif target == "Kilobits":
			value = value * 8.59e+9
			print "%s %s" % (value, target)
		elif target == "Kilobytes":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Megabits":
			value = value * 8.389e+6
			print "%s %s" % (value, target)
		elif target == "Megabytes":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Gigabits":
			value = value * 8192
			print "%s %s" % (value, target)
		elif target == "Gigabytes":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Terabits":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "Petabits":
			value = value * 0.0078125
			print "%s %s" % (value, target)
		elif target == "Petabytes":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Petabits":
		if target == "Bits":
			value = value * 1.126e+15
			print "%s %s" % (value, target)
		elif target == "Bytes":
			value = value * 1.407e+14
			print "%s %s" % (value, target)
		elif target == "Kilobits":
			value = value * 1.1e+12
			print "%s %s" % (value, target)
		elif target == "Kilobytes":
			value = value * 1.374e+11
			print "%s %s" % (value, target)
		elif target == "Megabits":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Megabytes":
			value = value * 1.342e+8
			print "%s %s" % (value, target)
		elif target == "Gigabits":
			value = value * 1.04e+6
			print "%s %s" % (value, target)
		elif target == "Gigabytes":
			value = value * 131072
			print "%s %s" % (value, target)
		elif target == "Terabits":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Terabytes":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "Petabytes":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Petabytes":
		if target == "Bits":
			value = value * 9.007e+15
			print "%s %s" % (value, target)
		elif target == "Bytes":
			value = value * 1.126e+15
			print "%s %s" % (value, target)
		elif target == "Kilobits":
			value = value * 8.796e+12
			print "%s %s" % (value, target)
		elif target == "Kilobytes":
			value = value * 8.59e+9
			print "%s %s" % (value, target)
		elif target == "Megabytes":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Gigabits":
			value = value * 8.389e+6
			print "%s %s" % (value, target)
		elif target == "Gigabytes":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Terabits":
			value = value * 8192
			print "%s %s" % (value, target)
		elif target == "Terabytes":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Petabits":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	else:
		print error1			
#########
# Speed #
#########
elif conv_type == "Speed":
	print "Available Units:"
	print "	Miles per Hour"
	print "	Feet per Second"
	print "	Meters per Second"
	print "	Kilometers per Hour"
	print "	Knots"
	base = raw_input("Enter base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Miles per Hour":
		if target == "Feet per second":
			value = value * 1.46667
			print "%s %s" % (value, target)
		elif target == "Meters per Second":
			value = value * 0.44704
			print "%s %s" % (value, target)
		elif target == "Kilometers per Hour":
			value = value * 1.60934
			print "%s %s" % (value, target)
		elif target == "Knots":
			value = value * 0.868976
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Feet per Second":
		if target == "Miles per Hour":
			value = value * 2.23694
			print "%s %s" % (value, target)
		elif target == "Meters per Second":
			value = value * 0.44704
			print "%s %s" % (value, target)
		elif target == "Kilometers per Hour":
			value = value * 1.60934
			print "%s %s" % (value, target)
		elif target == "Knots":
			value = value * 0.868976
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Meters per Second":
		if target == "Miles per Hour":
			value = value * 2.23694
			print "%s %s" % (value, target)
		elif target == "Feet per Second":
			value = value * 3.28084
			print "%s %s" % (value, target)
		elif target == "Kilometers per Hour":
			value = value * 3.6
			print "%s %s" % (value, target)
		elif target == "Knots":
			value = value * 1.94384
			print "%s %s" % (value, target)
		elif target == base:
			print error2
	elif base == "Kilometers per Hour":
		if target == "Miles per Hour":
			value = value * 0.621371
			print "%s %s" % (value, target)
		elif target == "Feet per Second":
			value = value * 0.911344
			print "%s %s" % (value, target)
		elif target == "Meters per Second":
			value = value * 1.09728
			print "%s %s" % (value, target)
		elif target == "Knots":
			value = value * 0.592484
			print "%s %s" % (value, target)
		elif target == base:
			print error2
	elif base == "Knots":
		if target == "Miles per Hour":
			value = value * 1.15078
			print "%s %s" % (value, target)
		elif target == "Feet per Second":
			value = value * 1.68781
			print "%s %s" % (value, target)
		elif target == "Meters per Second":
			value = value * 0.514444
			print "%s %s" % (value, target)
		elif target == "Kilometers per Hour":
			value = value * 1.852
			print "%s %s" % (value, target)
		elif target == base:
			print error2
	else:
		print error1
########
# Area #
########
elif conv_type == "Area":
	print "Available Units:"
	print "	Square Kilometers"
	print "	Square Meters"
	print "	Square Miles"
	print "	Acres"
	print "	Square Yards"
	print "	Square Feet"
	print "	Square Inches"
	base = raw_input("Enter base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Square Kilometers":
		if target == "Square Meters":
			value = value * 1e+6
			print "%s %s" % (value, target)
		elif target == "Square Miles":
			value = value * 0.386102
			print "%s %s" % (value, target)
		elif target == "Acres":
			value = value * 247.105
			print "%s %s" % (value, target)
		elif target == "Square Yards":
			value = value * 1.196e+6
			print "%s %s" % (value, target)
		elif target == "Square Feet":
			value = value * 1.076e+7
			print "%s %s" % (value, target)
		elif target == "Square Inches":
			value = value * 1.55e+9
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Square Meters":
		if target == "Square Kilometers":
			value = value * 1e-6
			print "%s %s" % (value, target)
		elif target == "Square Miles":
			value = value * 3.861e-7
			print "%s %s" % (value, target)
		elif target == "Acres":
			value = value * 0.000247105
			print "%s %s" % (value, target)
		elif target == "Square Yards":
			value = value * 1.19599
			print "%s %s" % (value, target)
		elif target == "Square Feet":
			value = value * 10.7639
			print "%s %s" % (value, target)
		elif target == "Square Inches":
			value = value * 1550
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1	
	elif base == "Square Miles":
		if target == "Square Kilometers":
			value = value * 2.58999
			print "%s %s" % (value, target)
		elif target == "Square Meters":
			value = value * 2.59e+6
			print "%s %s" % (value, target)
		elif target == "Acres":
			value = value * 640
			print "%s %s" % (value, target)
		elif target == "Square Yards":
			value = value * 3.098e+6
			print "%s %s" % (value, target)
		elif target == "Square Feet":
			value = value * 2.788e+7
			print "%s %s" % (value, target)
		elif target == "Square Inches":
			value = value * 4.014e+9
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Acres":
		if target == "Square Kilometers":
			value = value * 0.00404686
			print "%s %s" % (value, target)
		elif target == "Square Meters":
			value = value * 4046.86
			print "%s %s" % (value, target)
		elif target == "Square Miles":
			value = value * 0.0015625
			print "%s %s" % (value, target)
		elif target == "Square Yards":
			value = value * 4840
			print "%s %s" % (value, target)
		elif target == "Square Feet":
			value = value * 43560
			print "%s %s" % (value, target)
		elif target == "Square Inches":
			value = value * 6.273e+6
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Square Yards":
		if target == "Square Kilometers":
			value = value * 8.3613e-7
			print "%s %s" % (value, target)
		elif target == "Square Meters":
			value = value * 0.836127
			print "%s %s" % (value, target)
		elif target == "Square Miles":
			value = value * 3.2283e-7
			print "%s %s" % (value, target)
		elif target == "Acres":
			value = value * 0.000206612
			print "%s %s" % (value, target)
		elif target == "Square Feet":
			value = value * 9
			print "%s %s" % (value, target)
		elif target == "Square Inches":
			value = value * 1296
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Square Feet":
		if target == "Square Kilometers":
			value = value * 9.2903e-8
			print "%s %s" % (value, target)
		elif target == "Square Meters":
			value = value * 0.92903
			print "%s %s" % (value, target)
		elif target == "Square Miles":
			value = value * 3.587e-8
			print "%s %s" % (value, target)
		elif target == "Acres":
			value = value * 2.2957e-5
			print "%s %s" % (value, target)
		elif target == "Square Yards":
			value = value * 0.111111
			print "%s %s" % (value, target)
		elif target == "Square Inches":
			value = value * 144
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Square Inches":
		if target == "Square Kilometers":
			value = value * 6.4516e-10
			print "%s %s" % (value, target)
		elif target == "Square Meters":
			value = value * 0.00064516
			print "%s %s" % (value, target)
		elif target == "Square Miles":
			value = value * 2.491e-10
			print "%s %s" % (value, target)
		elif target == "Acres":
			value = value * 1.5942e-7
			print "%s %s" % (value, target)
		elif target == "Square Yards":
			value = value * 0.000771605
			print "%s %s" % (value, target)
		elif target == "Square Feet":
			value = value * 0.00694444
			print "%s %s" % (value, target)
		elif target == base:
			print error2 
		else:
			print error1
	else:
		print error1
#elif conv_type == "Fuel":
#	print "Available Units:"
#	base = raw_input("Enter base unit: ")
#	value = int(input("Enter base value: "))
#	target = raw_input("Enter target unit: ")
#	else:
#		print error1
#elif conv_type == "Time":
#	print "Available Units:"
#	base = raw_input("Enter base unit: ")
#	value = int(input("Enter base value: "))
#	target = raw_input("Enter target unit: ")
#	else:
#		print error1
else:
	print error1