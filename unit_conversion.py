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
print "	Area (Not Yet Supported)"
print "	Fuel Consumption (Not Yet Supported)"
print "	Time (Not Yet Supported)"
conv_type = raw_input("Select conversion type: ")
###############
# Temperature #
###############
if conv_type == "Temperature" :
	print "Available Units:"
	print "	Celcius"
	print "	Fahrenheit"
	print "	Kelvin"
	base = raw_input("Select base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Celcius":
		if target == "Fahrenheit":
			value = value * 9
			value = value / 5
			value = value + 32
			print "%s %s" % (value, target)
		elif target == "Kelvin":
			value = value + 273.15
			print " %s %s " % value, target
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Fahrenheit":
		if target == "Celcius":
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
		if target == "Celcius":
			value = value - 273.15
			print "%s %s" % (value, target)
		elif target == "Fahrenheit":
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
	print "	Kilometer"
	print "	Mile"
	print "	Meter"
	print "	Yard"
	print "	Foot"
	print "	Inch"
	print "	Centimeter"
	base = raw_input("Select base unit: ")
	if base == "Kilometer":
		value = int(input("Enter base value: "))
		target = raw_input("Enter target unit: ")
		if target == "Mile":
			value = value * 0.621371
			print "%s %s" % (value, target)
		elif target == "Meter":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == "Yard":
			value = value * 1093.61
			print "%s %s" % (value, target)
		elif target == "Foot":
			value = value * 3280.84
			print "%s %s" % (value, target)
		elif target == "Inch":
			value = value * 39370.1
			print "%s %s" % (value, target)
		elif target == "Centimeter":
			value = value * 100000
			print "%s %s" % (value, target)
		elif target == base:
			print error2		
		else:
			print error1
	elif base == "Mile":
		value = int(input("Enter base value: "))
		target = raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 1.60934
			print "%s %s" % (value, target)
		elif target == "Meter":
			value = value * 1609.34
			print "%s %s" % (value, target)
		elif target == "Yard":
			value = value * 1760
			print "%s %s" % (value, target)
		elif target == "Foot":
			value = value * 5280
			print "%s %s" % (value, target)
		elif target == "Inch":
			value = value * 63360
			print "%s %s" % (value, target)
		elif target == "Centimeter":
			value = value * 160934
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Meter":
		value = int(input("Enter base value: "))
		target == raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == "Mile":
			value = value * 0.000621371
			print "%s %s" % (value, target)
		elif target == "Yard":
			value = value * 1.09361
			print "%s %s" % (value, target)
		elif target == "Foot":
			value = value * 3.28084
			print "%s %s" % (value, target)
		elif target == "Inch":
			value = value * 39.3701
			print "%s %s" % (value, target)
		elif target == "Centimeter":
			value = value * 100
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Yard":
		value = int(input("Enter base value: "))
		target == raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 0.0009144
			print "%s %s" % (value, target)
		elif target == "Mile":
			value = value * 0.000568182
			print "%s %s" % (value, target)
		elif target == "Meter":
			value = value * 0.9144
			print "%s %s" % (value, target)
		elif target == "Foot":
			value = value * 3
			print "%s %s" % (value, target)
		elif target == "Inch":
			value = value * 36
			print "%s %s" % (value, target)
		elif target == "Centimeter":
			value = value * 91.44
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Foot":
		value = int(input("Enter base value: "))
		target = raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 0.0003048
			print "%s %s" % (value, target)
		elif target == "Mile":
			value = value * 0.000189394
			print "%s %s" % (value, target)
		elif target == "Meter":
			value = value * 0.3048
			print "%s %s" % (value, target)
		elif target == "Yard":
			value = value * 0.333333
			print "%s %s" % (value, target)
		elif target == "Inch":
			value = value * 12
			print "%s %s" % (value, target)
		elif target == "Centimeter":
			value = value * 30.48
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Inch":
		value = int(input("Enter base value: "))
		target = raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 0.00025399989
			print "%s %s" % (value, target)
		elif target == "Mile":
			value = value * 0.00015782827
			print "%s %s" % (value, target)
		elif target == "Meter":
			value = value * 0.0254
			print "%s %s" % (value, target)
		elif target == "Yard":
			value = value * 0.277778
			print "%s %s" % (value, target)
		elif target == "Foot":
			value = value * 0.0833333
			print "%s %s" % (value, target)
		elif target == "Centimeter":
			value = value * 2.54
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Centimeter":
		value = int(input("Enter base value: "))
		target = raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 0.00001
			print "%s %s" % (value, target)
		elif target == "Mile":
			value = value * 0.00000621371
			print "%s %s" % (value, target)
		elif target == "Meter":
			value = value * 0.01
			print "%s %s" % (value, target)
		elif target == "Yard":
			value = value * 0.0109361
			print "%s %s" % (value, target)
		elif target == "Foot":
			value = value * 0.0328084
			print "%s %s" % (value, target)
		elif target == "Inch":
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
	print "	Metric Ton"
	print "	Stone"
	print "	Kilogram"
	print "	Pound"
	print "	Ounce"
	print "	Gram"
	print " Milligram"
	base = raw_input("Enter base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Metric Ton":
		if target == "Stone":
			value = value * 157.473
			print "%s %s" % (value, target)
		elif target == "Kilogram":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == "Pound":
			value = value * 2204.62
			print "%s %s" % (value, target)
		elif target == "Ounce":
			value = value * 35274
			print "%s %s" % (value, target)
		elif target == "Gram":
			value = value * 1000000.263
			print "%s %s" % (value, target)
		elif target == "Milligram":
			value = value * 1000000263
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Stone":
		if target == "Metric Ton":
			value = value * 0.00635029
			print "%s %s" % (value, target)
		elif target == "Kilogram":
			value = value * 6.35029
			print "%s %s" % (value, target)
		elif target == "Pound":
			value = value * 14
			print "%s %s" % (value, target)
		elif target == "Ounce":
			value = value * 224
			print "%s %s" % (value, target)
		elif target == "Gram":
			value = value * 6350.29
			print "%s %s" % (value, target)
		elif target == "Milligram":
			value = value * 6350290
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Kilogram":
		if target == "Metric Ton":
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == "Stone":
			value = value * 0.157473
			print "%s %s" % (value, target)
		elif target == "Pound":
			value = value * 2.20462
			print "%s %s" % (value, target)
		elif target == "Ounce":
			value = value * 35.274
			print "%s %s" % (value, target)
		elif target == "Gram":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == "Milligram":
			value = value * 1000000
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Pound":
		if target == "Metric Ton":
			value = value * 0.000453592
			print "%s %s" % (value, target)
		elif target == "Stone":
			value = value * 0.0714286
			print "%s %s" % (value, target)
		elif target == "Kilogram":
			value = value * 0.453592
			print "%s %s" % (value, target)
		elif target == "Ounce":
			value = value * 16
			print "%s %s" % (value, target)
		elif target == "Gram":
			value = value * 453.592
			print "%s %s" % (value, target)
		elif target == "Milligram":
			value = value * 453492
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Ounce":
		if target == "Metric Ton":
			value = value * 0.0000283495
			print "%s %s" % (value, target)
		elif target == "Stone":
			value = value * 0.00446429
			print "%s %s" % (value, target)
		elif target == "Kilogram":
			value = value * 0.0283495
			print "%s %s" % (value, target)
		elif target == "Pound":
			value = value * 0.0625
			print "%s %s" % value , target
		elif target == "Gram":
			value = value * 28.3495
			print "%s %s" % (value, target)
		elif target == "Milligram":
			value = value * 28349.5
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Gram":
		if target == "Metric Ton":
			value = value * 0.000001
			print "%s %s" % (value, target)
		elif target == "Stone":
			value = value * 0.000157473
			print "%s %s" % (value, target)
		elif target == "Kilogram":
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == "Pound":
			value = value * 0.00220462
			print "%s %s" % (value, target)
		elif target == "Ounce":
			value = value * 0.035274
			print "%s %s" % (value, target)
		elif target == "Milligram":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Milligram":
		if target == "Metric Ton":
			value = value * 0.000001
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == "Stone":
			value = value * 0.001
			value = value * 0.000157473
			print "%s %s" % (value, target)
		elif target == "Kilogram":
			value = value * 0.000001
			print "%s %s" % (value, target)
		elif target == "Pound":
			value = value * 0.001
			value = value * 0.00220462
			print "%s %s" % (value, target)
		elif target == "Ounce":
			value = value * 0.001
			value = value * 0.035274
			print "%s %s" % (value, target)
		elif target == "Gram":
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
	print "	US gal"
	print "	US quart"
	print "	US pint"
	print "	US cup"
	print "	US ounce"
	print "	US tbsp"
	print "	US tsp"
	print "	Cubic meter"
	print "	Cubic foot"
	print "	Cubic inch"
	print "	Liter"
	print "	Milliliter"
	base = raw_input("Enter base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "US gal":
		if target == "US quart":
			value = value * 4
			print "%s %s" % (value, target)
		elif target == "US pint":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "US cup":
			value = value * 16
			print "%s %s" % (value, target)
		elif target == "US ounce":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "US tbsp":
			value = value * 256
			print "%s %s" % (value, target)
		elif target == "US tsp":
			value = value * 768
			print "%s %s" % (value, target)
		elif target == "Cubic meter":
			value = value * 0.00378541
			print "%s %s" % (value, target)
		elif target == "Cubic foot":
			value = value * 0.133681
			print "%s %s" % (value, target)
		elif target == "Cubic inch":
			value = value * 231
			print "%s %s" % (value, target)
		elif target == "Liter":
			value = value * 3.78541
			print "%s %s" % (value, target)
		elif target == "Milliliter":
			value = value * 3785.41
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US quart":
		if target == "US gal":
			value = value * 0.25
			print "%s %s" % (value, target)
		elif target == "US pint":
			value = value * 2
			print "%s %s" % (value, target)
		elif target == "US cup":
			value = value * 4
			print "%s %s" % (value, target)
		elif target == "US ounce":
			value = value * 32
			print "%s %s" % (value, target)
		elif target == "US tbsp":
			value = value * 64
			print "%s %s" % (value, target)
		elif target == "US tsp":
			value = value * 192
			print "%s %s" % (value, target)
		elif target == "Cubic meter":
			value = value * 0.000946353
			print "%s %s" % (value, target)
		elif target == "Cubic foot":
			value = value * 0.0334201
			print "%s %s" % (value, target)
		elif target == "Cubic inch":
			value = value * 57.75
			print "%s %s" % (value, target)
		elif target == "Liter":
			value = value * 0.946353
			print "%s %s" % (value, target)
		elif target == "Milliliter":
			value = value * 946.353
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US pint":
		if target == "US gal":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "US quart":
			value = value * 0.5
			print "%s %s" % (value, target)
		elif target == "US cup":
			value = value * 2
			print "%s %s" % (value, target)
		elif target == "US ounce":
			value = value * 32
			print "%s %s" % (value, target)
		elif target == "US tbsp":
			value = value * 64
			print "%s %s" % (value, target)
		elif target == "US tsp":
			value = value * 192
			print "%s %s" % (value, target)
		elif target == "Cubic meter":
			value = value * 0.000473176
			print "%s %s" % (value, target)
		elif target == "Cubic foot":
			value = value * 0.0167101
			print "%s %s" % (value, target)
		elif target == "Cubic inch":
			value = value * 28.875
			print "%s %s" % (value, target)
		elif target == "Liter":
			value = value * 0.473176
			print "%s %s" % (value, target)
		elif target == "Milliliter":
			value = value * 473.176
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US cup":
		if target == "US gal":
			value = value * 0.0625
			print "%s %s" % (value, target)
		elif target == "US quart":
			value = value * 0.25
			print "%s %s" % (value, target)
		elif target == "US pint":
			value = value * 0.5
			print "%s %s" % (value, target)
		elif target == "US ounce":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "US tbsp":
			value = value * 16
			print "%s %s" % (value, target)
		elif target == "US tsp":
			value = value * 48
			print "%s %s" % (value, target)
		elif target == "Cubic meter":
			value = value * 0.00026588
			print "%s %s" % (value, target)
		elif target == "Cubic foot":
			value = value * 0.00835503
			print "%s %s" % (value, target)
		elif target == "Cubic inch":
			value = value * 14.4375
			print "%s %s" % (value, target)
		elif target == "Liter":
			value = value * 0.236588
			print "%s %s" % (value, target)
		elif target == "Milliliter":
			value = value * 236.588
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US ounce":
		if target == "US gal":
			value = value * 0.0078125
			print "%s %s" % (value, target)
		elif target == "US quart":
			value = value * 0.03125
			print "%s %s" % (value, target)
		elif target == "US pint":
			value = value * 0.0625
			print "%s %s" % (value, target)
		elif target == "US cup":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "US tbsp":
			value = value * 2
			print "%s %s" % (value, target)
		elif target == "US tsp":
			value = value * 6
			print "%s %s" % (value, target)
		elif target == "Cubic meter":
			value = value * 0.00002419619
			print "%s %s" % (value, target)
		elif target == "Cubic foot":
			value = value * 0.00104438
			print "%s %s" % (value, target)
		elif target == "Cubic inch":
			value = value * 1.80469
			print "%s %s" % (value, target)
		elif target == "Liter":
			value = value * 0.0295735
			print "%s %s" % (value, target)
		elif target == "Milliliters":
			value = value * 29.5735
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US tbsp":
		if target == "US gal":
			value = value * 0.00390625
			print "%s %s" % (value, target)
		elif target == "US quart":
			value = value * 0.015625
			print "%s %s" % (value, target)
		elif target == "US pint":
			value = value * 0.03125
			print "%s %s" % (value, target)
		elif target == "US cup":
			value = value * 0.0625
			print "%s %s" % (value, target)
		elif target == "US ounce":
			value = value * 0.5
			print "%s %s" % (value, target)
		elif target == "US tsp":
			value = value * 6
			print "%s %s" % (value, target)
		elif target == "Cubic meter":
			value = value * 0.00002957349
			print "%s %s" % (value, target)
		elif target == "Cubic foot":
			value = value * 0.00104438
			print "%s %s" % (value, target)
		elif target == "Cubic inch":
			value = value * 0.902344
			print "%s %s" % (value, target)
		elif target == "Liter":
			value = value * 0.0147868
			print "%s %s" % (value, target)
		elif target == "Milliliter":
			value = value * 14.7868
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "US tsp":
		if target == "US gal":
			value = value * 0.00130208
			print "%s %s" % (value, target)
		elif target == "US quart":
			value = value * 0.00520833
			print "%s %s" % (value, target)
		elif target == "US pint":
			value = value * 0.0104167
			print "%s %s" % (value, target)
		elif target == "US cup":
			value = value * 0.020833
			print "%s %s" % (value, target)
		elif target == "US ounce":
			value = value * 0.166667
			print "%s %s" % (value, target)
		elif target == "US tbsp":
			value = value * 0.333333
			print "%s %s" % (value, target)
		elif target == "Cubic meter":
			value = value * 0.0000049289
			print "%s %s" % (value, target)
		elif target == "Cubic foot":
			value = value * 0.000174063
			print "%s %s" % (value, target)
		elif target == "Cubic inch":
			value = value * 0.300781
			print "%s %s" % (value, target)
		elif target == "Liter":
			value = value * 0.00492892
			print "%s %s" % (value, target)
		elif target == "Milliliter":
			value = value * 4.92892
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Cubic meter":
		if target == "US gal":
			value = value * 264.172
			print "%s %s" % (value, target)
		elif target == "US quart":
			value = value * 1056.69
			print "%s %s" % (value, target)
		elif target == "US pint":
			value = value * 2113.38
			print "%s %s" % (value, target)
		elif target == "US cup":
			value = value * 4226.75
			print "%s %s" % (value, target)
		elif target == "US ounce":
			value = value * 33814
			print "%s %s" % (value, target)
		elif target == "US tbsp":
			value = value * 67628
			print "%s %s" % (value, target)
		elif target == "US tsp":
			value = value * 202884
			print "%s %s" % (value, target)
		elif target == "Cubic foot":
			value = value * 35.3147
			print "%s %s" % (value, target)
		elif target == "Cubic inch":
			value = value * 61023.7
			print "%s %s" % (value, target)
		elif target == "Liter":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == "Milliliter":
			value = value * 1000000
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Cubic foot":
		if target == "US gal":
			value = value * 7.48052
			print "%s %s" % (value, target)
		elif target == "US quart":
			value = value * 29.9221
			print "%s %s" % (value, target)
		elif target == "US pint":
			value = value * 59.8442
			print "%s %s" % (value, target)
		elif target == "US cup":
			value = value * 119.688
			print "%s %s" % (value, target)
		elif target == "US ounce":
			value = value * 957.506
			print "%s %s" % (value, target)
		elif target == "US tbsp":
			value = value * 1915.01
			print "%s %s" % (value, target)
		elif target == "US tsp":
			value = value * 5745.04
			print "%s %s" % (value, target)
		elif target == "Cubic meters":
			value = value * 0.0283168
			print "%s %s" % (value, target)
		elif target == "Cubic inch":
			value = value * 1728
			print "%s %s" % (value, target)
		elif target == "Liter":
			value = value * 28.3168
			print "%s %s" % (value, target)
		elif target == "Milliliter":
			value = value * 28316.8
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Cubic inch":
		if target == "US gal":
			value = value * 0.004329
			print "%s %s" % (value, target)
		elif target == "US quart":
			value = value * 0.017316
			print "%s %s" % (value, target)
		elif target == "US pint":
			value = value * 0.034632
			print "%s %s" % (value, target)
		elif target == "US cup":
			value = value * 0.0692641
			print "%s %s" % (value, target)
		elif target == "US ounce":
			value = value * 0.554113
			print "%s %s" % (value, target)
		elif target == "US tbsp":
			value = value * 1.10823
			print "%s %s" % (value, target)
		elif target == "US tsp":
			value = value * 3.32468
			print "%s %s" % (value, target)
		elif target == "Cubic meter":
			value = value * 0.00001638704
			print "%s %s" % (value, target)
		elif target == "Cubic foot":
			value = value * 0.000578704
			print "%s %s" % (value, target)
		elif target == "Liter":
			value = value * 0.0163871
			print "%s %s" % (value, target)
		elif target == "Milliliter":
			value = value * 16.3871
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Liter":
		if target == "US gal":
			value = value * 0.264172
			print "%s %s" % (value, target)
		elif target == "US quart":
			value = value * 1.05669
			print "%s %s" % (value, target)
		elif target == "US pint":
			value = value * 2.11338
			print "%s %s" % (value, target)
		elif target == "US cup":
			value = value * 4.22675
			print "%s %s" % (value, target)
		elif target == "US ounce":
			value = value * 33.814
			print "%s %s" % (value, target)
		elif target == "US tbsp":
			value = value * 67.628
			print "%s %s" % (value, target)
		elif target == "US tsp":
			value = value * 202.884
			print "%s %s" % (value, target)
		elif target == "Cubic meter":
			value = value * 0.001
			print "%s %s" % (value, target)
		elif target == "Cubic foot":
			value = value * 0.0353147
			print "%s %s" % (value, target)
		elif target == "Cubic inch":
			value = value * 61.0237
			print "%s %s" % (value, target)
		elif target == "Milliliter":
			value = value * 1000
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Milliliter":
		if target == "US gal":
			value = value * 0.000264172
			print "%s %s" % (value, target)
		elif target == "US quart":
			value = value * 0.00105669
			print "%s %s" % (value, target)
		elif target == "US pint":
			value = value * 0.00211338
			print "%s %s" % (value, target)
		elif target == "US cup":
			value = value * 0.00422675
			print "%s %s" % (value, target)
		elif target == "US ounce":
			value = value * 0.033814
			print "%s %s" % (value, target)
		elif target == "US tbsp":
			value = value * 0.067628
			print "%s %s" % (value, target)
		elif target == "US tsp":
			value = value * 0.202884
			print "%s %s" % (value, target)
		elif target == "Cubic meter":
			value = value * 0.000001
			print "%s %s" % (value, target)
		elif target == "Cubic foot":
			value = value * 0.00003531465
			print "%s %s" % (value, target)
		elif target == "Cubic inch":
			value = value * 0.0610237
			print "%s %s" % (value, target)
		elif target == "Liter":
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
	print "	Bit"
	print "	Byte"
	print "	Kilobit"
	print "	Kilobyte"
	print "	Megabit"
	print "	Megabyte"
	print "	Gigabit"
	print "	Gigabyte"
	print "	Terabit"
	print "	Terabyte"
	print "	Petabit"
	print "	Pteabyte"
	base = raw_input("Enter base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Bit":
		if target == "Byte":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Kilobit":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Kilobyte":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == "Megabit":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Megabyte":
			value = value * 1.1921e-7
			print "%s %s" % (value, target)
		elif target == "Gigabit":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == "Gigabyte":
			value = value * 1.1642e-10
			print "%s %s" % (value, target)
		elif target == "Terabit":
			value = value * 9.0949e-13
			print "%s %s" % (value, target)
		elif target == "Terabyte":
			value = value * 1.1369e-13
			print "%s %s" % (value, target)
		elif target == "Petabit":
			value = value * 8.8818e-16
			print "%s %s" % (value, target)
		elif target == "Petabyte":
			value = value * 1.1102e-16
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Byte":
		if target == "Bit":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "Kilobit":
			value = value * 0.0078125
			print "%s %s" % (value, target)
		elif target == "Kilobyte":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Megabit":
			value = value * 7.6294e-6
			print "%s %s" % (value, target)
		elif target == "Megabyte":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Gigabit":
			value = value * 7.4506e-9
			print "%s %s" % (value, target)
		elif target == "Gigabyte":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == "Terabit":
			value = value * 7.276e-12
			print "%s %s" % (value, target)
		elif target == "Terabyte":
			value = value * 9.0949e-13
			print "%s %s" % (value, target)
		elif target == "Petabit":
			value = value * 7.1054e-15
			print "%s %s" % (value, target)
		elif target == "Petabyte":
			value = value * 8.8818e-16
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Kilobit":
		if target == "Bit":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Byte":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "Kilobyte":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Megabit":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Megabyte":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == "Gigabit":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Gigabyte":
			value = value * 1.921e-7
			print "%s %s" % (value, target)
		elif target == "Terabit":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == "Terabyte":
			value = value * 1.1642e-10
			print "%s %s" % (value, target)
		elif target == "Petabit":
			value = value * 9.0949e-13
			print "%s %s" % (value, target)
		elif target == "Petabyte":
			value = value * 1.1369e-13
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1		
	elif base == "Kilobyte":
		if target == "Bit":
			value = value * 8192
			print "%s %s" % (value, target)
		elif target == "Byte":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Kilobit":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "Megabit":
			value = value * 0.0078125
			print "%s %s" % (value, target)
		elif target == "Megabyte":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Gigabit":
			value = value * 7.6294e-6
			print "%s %s" % (value, target)
		elif target == "Gigabyte":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Terabit":
			value = value * 7.4506e-9
			print "%s %s" % (value, target)
		elif target == "Terabyte":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == "Petabit":
			value = value * 7.276e-12
			print "%s %s" % (value, target)
		elif target == "Petabyte":
			value = value * 9.0949e-13
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Megabit":
		if target == "Bit":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Byte":
			value = value * 131072
			print "%s %s" % (value, target)
		elif target == "Kilobit":
			value = value * 102
			print "%s %s" % (value, target)
		elif target == "Kilobyte":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "Megabyte":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Gigabit":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Gigabyte":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == "Terabit":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Terabyte":
			value = value * 1.1921e-7
			print "%s %s" % (value, target)
		elif target == "Petabit":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == "Petabyte":
			value = value * 1.1642e-10
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Megabyte":
		if target == "Bit":
			value = value * 8.389e+6
			print "%s %s" % (value, target)
		elif target == "Byte":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Kilobit":
			value = value * 8192
			print "%s %s" % (value, target)
		elif target == "Kilobyte":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Megabit":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "Gigabit":
			value = value * 0.00078125
			print "%s %s" % (value, target)
		elif target == "Gigabyte":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Terabit":
			value = value * 7.6294e-6
			print "%s %s" % (value, target)
		elif target == "Terabyte":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Petabit":
			value = value * 7.4506e-9
			print "%s %s" % (value, target)
		elif target == "Petabyte":
			value = value * 9.3132e-10
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Gigabit":
		if target == "Bit":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Byte":
			value = value * 1.342e+8
			print "%s %s" % (value, target)
		elif target == "Kilobit":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Kilobyte":
			value = value * 131072
			print "%s %s" % (value, target)
		elif target == "Megabit":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Megabyte":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "Gigabyte":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Terabit":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Terabyte":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == "Petabit":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Petabyte":
			value = value * 1.1921e-7
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Gigabyte":
		if target == "Bit":
			value = value * 8.5e+9
			print "%s %s" % (value, target)
		elif target == "Byte":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Kilobit":
			value = value * 8.39e+6
			print "%s %s" % (value, target)
		elif target == "Kilobyte":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Megabit":
			value = value * 8192
			print "%s %s" % (value, target)
		elif target == "Megabyte":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Gigabit":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "Terabit":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Terabyte":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == "Petabit":
			value = value * 9.5367e-7
			print "%s %s" % (value, target)
		elif target == "Petabyte":
			value = value * 1.1921e-7
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Terabit":
		if target == "Bit":
			value = value * 1.1e+12
			print "%s %s" % (value, target)
		elif target == "Byte":
			value = value * 1.374e+11
			print "%s %s" % (value, target)
		elif target == "Kilobit":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Kilobyte":
			value = value * 1.342e+8
			print "%s %s" % (value, target)
		elif target == "Megabit":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Megabyte":
			value = value * 131072
			print "%s %s" % (value, target)
		elif target == "Gigabit":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Gigabyte":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "Terabyte":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == "Petabit":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == "Petabyte":
			value = value * 0.00012207
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Terabyte":
		if target == "Bit":
			value = value * 8.796e+12
			print "%s %s" % (value, target)
		elif target == "Byte":
			value = value * 1.1e+12
			print "%s %s" % (value, target)
		elif target == "Kilobit":
			value = value * 8.59e+9
			print "%s %s" % (value, target)
		elif target == "Kilobyte":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Megabit":
			value = value * 8.389e+6
			print "%s %s" % (value, target)
		elif target == "Megabyte":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Gigabit":
			value = value * 8192
			print "%s %s" % (value, target)
		elif target == "Gigabyte":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Terabit":
			value = value * 8
			print "%s %s" % (value, target)
		elif target == "Petabit":
			value = value * 0.0078125
			print "%s %s" % (value, target)
		elif target == "Petabyte":
			value = value * 0.000976563
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Petabit":
		if target == "Bit":
			value = value * 1.126e+15
			print "%s %s" % (value, target)
		elif target == "Byte":
			value = value * 1.407e+14
			print "%s %s" % (value, target)
		elif target == "Kilobit":
			value = value * 1.1e+12
			print "%s %s" % (value, target)
		elif target == "Kilobyte":
			value = value * 1.374e+11
			print "%s %s" % (value, target)
		elif target == "Megabit":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Megabyte":
			value = value * 1.342e+8
			print "%s %s" % (value, target)
		elif target == "Gigabit":
			value = value * 1.04e+6
			print "%s %s" % (value, target)
		elif target == "Gigabyte":
			value = value * 131072
			print "%s %s" % (value, target)
		elif target == "Terabit":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Terabyte":
			value = value * 128
			print "%s %s" % (value, target)
		elif target == "Petabyte":
			value = value * 0.125
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Petabyte":
		if target == "Bit":
			value = value * 9.007e+15
			print "%s %s" % (value, target)
		elif target == "Byte":
			value = value * 1.126e+15
			print "%s %s" % (value, target)
		elif target == "Kilobit":
			value = value * 8.796e+12
			print "%s %s" % (value, target)
		elif target == "Kilobyte":
			value = value * 8.59e+9
			print "%s %s" % (value, target)
		elif target == "Megabyte":
			value = value * 1.074e+9
			print "%s %s" % (value, target)
		elif target == "Gigabit":
			value = value * 8.389e+6
			print "%s %s" % (value, target)
		elif target == "Gigabyte":
			value = value * 1.049e+6
			print "%s %s" % (value, target)
		elif target == "Terabit":
			value = value * 8192
			print "%s %s" % (value, target)
		elif target == "Terabyte":
			value = value * 1024
			print "%s %s" % (value, target)
		elif target == "Petabit":
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
	print "	Miles per hour"
	print "	Feet per second"
	print "	Meters per second"
	print "	Kilometers per hour"
	print "	Knots"
	base = raw_input("Enter base unit: ")
	value = int(input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Miles per hour":
		if target == "Feet per second":
			value = value * 1.46667
			print "%s %s" % (value, target)
		elif target == "Meters per second":
			value = value * 0.44704
			print "%s %s" % (value, target)
		elif target == "Kilometers per hour":
			value = value * 1.60934
			print "%s %s" % (value, target)
		elif target == "Knots":
			value = value * 0.868976
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Feet per second":
		if target == "Miles per hour":
			value = value * 2.23694
			print "%s %s" % (value, target)
		elif target == "Meters per second":
			value = value * 0.44704
			print "%s %s" % (value, target)
		elif target == "Kilometers per hour":
			value = value * 1.60934
			print "%s %s" % (value, target)
		elif target == "Knots":
			value = value * 0.868976
			print "%s %s" % (value, target)
		elif target == base:
			print error2
		else:
			print error1
	elif base == "Meters per second":
		if target == "Miles per hour":
			value = value * 2.23694
			print "%s %s" % (value, target)
		elif target == "Feet per second":
			value = value * 3.28084
			print "%s %s" % (value, target)
		elif target == "Kilometers per hour":
			value = value * 3.6
			print "%s %s" % (value, target)
		elif target == "Knots":
			value = value * 1.94384
			print "%s %s" % (value, target)
		elif target == base:
			print error2
	elif base == "Kilometers per hour":
		if target == "Miles per hour":
			value = value * 0.621371
			print "%s %s" % (value, target)
		elif target == "Feet per second":
			value = value * 0.911344
			print "%s %s" % (value, target)
		elif target == "Meters per second":
			value = value * 1.09728
			print "%s %s" % (value, target)
		elif target == "Knots":
			value = value * 0.592484
			print "%s %s" % (value, target)
		elif target == base:
			print error2
	elif base == "Knots":
		if target == "Miles per hour":
			value = value * 1.15078
			print "%s %s" % (value, target)
		elif target == "Feet per second":
			value = value * 1.68781
			print "%s %s" % (value, target)
		elif target == "Meters per second":
			value = value * 0.514444
			print "%s %s" % (value, target)
		elif target == "Kilometers per hour":
			value = value * 1.852
			print "%s %s" % (value, target)
		elif target == base:
			print error2
	else:
		print error1
#elif conv_type == "Area":
#	print "Available Units:"
#	base = raw_input("Enter base unit: ")
#	value = int(input("Enter base value: "))
#	target = raw_input("Enter target unit: ")
#	else:
#		print error1
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