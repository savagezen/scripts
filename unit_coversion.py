#!/bin/python2.7
# Unit Converter - based on Google conversions

print "Available conversions:"
print "	Temperature"
print "	Length"
print "	Mass"
print "	Volume"
print "	Digital Storage"
conv_type = raw_input("Select conversion type: ")

if conv_type == "Temperature" :					# Temperature
	print "Available Units:"
	print "	Celcius"
	print "	Fahrenheit"
	print "	Kelvin"
	base = raw_input("Select base unit: ")
	value = int(raw_input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Celcius":
		if target == "Fahrenheit":
			value = value * 9
			value = value / 5
			value = value + 32
			print " %d Degrees Fahrenheit" % value
		elif target == "Kelvin":
			value = value + 273.15
			print " %k Kelvin" % value
		else:
			print "Not a valid choice."
	elif base == "Fahrenheit":
		if target == "Celcius":
			value = int(raw_input("Enter base value: "))
			value = value - 32
			value = value * 5
			value = value / 9
			print " %d Degrees Celcius" % value
		elif target == "Kelvin":
			value = value -32
			value = value * 5
			value = value / 9
			value = valu + 273
			print " %k Kelvin" % value
	elif base == "Kelvin":
		if target == "Celcius":
			value = value - 273.15
			print " %c Degrees Celcius" % value
		elif target == "Fahrenheit":
			value = value - 305.15
			value = value * 5
			value = value / 9
			print " %f Degrees  Fahrenheit" % value
		else:
			print "Not a valid choice."
	else:
		print "Not a valid choice"
elif conv_type == "Length":					# Length
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
		value = int(raw_input("Enter base value: "))
		target = raw_input("Enter target unit: ")
		if target == "Mile":
			value = value * 0.621371
			print " %m Miles" % value
		elif target == "Meter":
			value = value * 1000
			print " %m Meters" % value
		elif target == "Yard":
			value = value * 1093.61
			print " %y Yards" % value
		elif target == "Foot":
			value = value * 3280.84
			print " %f Feet" % value
		elif target == "Inch":
			value = value * 39370.1
			print " %i Inches" % value
		elif target == "Centimeter":
			value = value * 100000
			print " %c Centimeters" % value
		else:
			print "Not a valid choice."
	elif base == "Mile":
		value = int(raw_input("Enter base value: "))
		target = raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 1.60934
			print " %k Kilometers" % value
		elif target == "Meter":
			value = value * 1609.34
			print " %m Meters" % value
		elif target == "Yard":
			value = value * 1760
			print " %y Yards" % value
		elif target == "Foot":
			value = value * 5280
			print " %f Feet" % value
		elif target == "Inch":
			value = value * 63360
			print " %i Inches" % value
		elif target == "Centimeter":
			value = value * 160934
			print " %c Centimeters" % value
		else:
			print "Not a valid choice."
	elif base == "Meter":
		value = int(raw_input("Enter base value: "))
		target == raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 0.001
			print " %k Kilometers" % value
		elif target == "Mile":
			value = value * 0.000621371
			print " %m Miles" % value
		elif target == "Yard":
			value = value * 1.09361
			print " %y Yards" % value
		elif target == "Foot":
			value = value * 3.28084
			print " %f Feet" % value
		elif target == "Inch":
			value = value * 39.3701
			print " %i Inches" % value
		elif target == "Centimeter":
			value = value * 100
			print " %c Centimeters" % value
		else:
			print "Not a valid choice."
	elif base == "Yard":
		value = int(raw_input("Enter base value: "))
		target == raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 0.0009144
			print " %k Kilometers" % value
		elif target == "Mile":
			value = value * 0.000568182
			print " %m Miles" % value
		elif target == "Meter":
			value = value * 0.9144
			print " %m Meters" % value
		elif target == "Foot":
			value = value * 3
			print " %f Feet" % value
		elif target == "Inch":
			value = value * 36
			print " %i Inches" % value
		elif target == "Centimeter":
			value = value * 91.44
			print " %c Centimeters" % value
		else:
			print "Not a valid choice."
	elif base == "Foot":
		value = int(raw_input("Enter base value: "))
		target = raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 0.0003048
			print " %k Kilometers" % value
		elif target == "Mile":
			value = value * 0.000189394
			print " %m Miles" % value
		elif target == "Meter":
			value = value * 0.3048
			print " %m Meters" % value
		elif target == "Yard":
			value = value * 0.333333
			print " %y Yards" % value
		elif target == "Inch":
			value = value * 12
			print " %i Inches" % value
		elif target == "Centimeter":
			value = value * 30.48
			print " %c Centimeters" % value
		else:
			print "Not a valid choice."
	elif base == "Inch":
		value = int(raw_input("Enter base value: "))
		target = raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 0.00025399989
			print " %k Kilometers" % value
		elif target == "Mile":
			value = value * 0.00015782827
			print " %m Miles" % value
		elif target == "Meter":
			value = value * 0.0254
			print " %m Meters" % value
		elif target == "Yard":
			value = value * 0.277778
			print " %y Yards" % value
		elif target == "Foot":
			value = value * 0.0833333
			print " %f Feet" % value
		elif target == "Centimeter":
			value = value * 2.54
			print " %c Centimeters" % value
		else:
			print "Not a valid choice."
	elif base == "Centimeter":
		value = int(raw_input("Enter base value: "))
		target = raw_input("Enter target unit: ")
		if target == "Kilometer":
			value = value * 0.00001
			print " %k Kilometers" % value
		elif target == "Mile":
			value = value * 0.00000621371
			print " %m Miles" % value
		elif target == "Meter":
			value = value * 0.01
			print " %m Meters" % value
		elif target == "Yard":
			value = value * 0.0109361
			print " %y Yards" % value
		elif target == "Foot":
			value = value * 0.0328084
			print " %f Feet" % value
		elif target == "Inch":
			value = value * 0.393701
			print " %i Inches" % value
		else:
			print "Not a valid choice."
	else:
		print "Not a valid choice."
elif conv_type == "Mass":					# Mass
	print "Available Units:"
	print "	Metric Ton"
	print "	Stone"
	print "	Kilogram"
	print "	Pound"
	print "	Ounce"
	print "	Gram"
	print " Milligram"
	base = raw_input("Enter base unit: ")
	value = int(raw_input("Enter base value: "))
	target = raw_input("Enter target unit: ")
	if base == "Metric Ton":
		if target == "Stone":
			value = value * 157.473
			print " %t Metric Tons" % value
		elif target == "Kilogram":
			value = value * 1000
			print " %k Kilograms" % value
		elif target == "Pound":
			value = value * 2204.62
			print " %p Pounds" % value
		elif target == "Ounce":
			value = value * 35274
			print " %o Ounces" % value
		elif target == "Gram":
			value = value * 1000000.263
			print " %g Grams" % value
		elif target == "Milligram":
			value = value * 1000000263
			print " %m Milligrams" % value
		else:
			print "Not a valid choice."
	elif base == "Stone":
		if target == "Metric Ton":
			value = value * 0.00635029
			print " %m Metric Tons" % value
		elif target == "Kilogram":
			value = value * 6.35029
			print " %k Kilograms" % value
		elif target == "Pound":
			value = value * 14
			print " %p Pounds" % value
		elif target == "Ounce":
			value = value * 224
			print " %o Ounces" % value
		elif target == "Gram":
			value = value * 6350.29
			print " %g Grams" % value
		elif target == "Milligram":
			value = value * 6350290
			print " %m Milligrams" % value
		else:
			print "Not a valid choice."
	elif base == "Kilogram":
		if target == "Metric Ton":
			value = value * 0.001
			print " %m Metric Tons" % value
		elif target == "Stone":
			value = value * 0.157473
			print " %s Stones" % value
		elif target == "Pound":
			value = value * 2.20462
			print " %p Pounds" % value
		elif target == "Ounce":
			value = value * 35.274
			print " %o Ounces" % value
		elif target == "Gram":
			value = value * 1000
			print " %g Grams" % value
		elif target == "Milligram":
			value = value * 1000000
			print " %m Milligrams" % value
		else:
			print "Not a valid choice."
	elif base == "Pound":
		if target == "Metric Ton":
			value = value * 0.000453592
			print " %m Metric Tons" % value
		elif target == "Stone":
			value = value * 0.0714286
			print " %s Stones" % value
		elif target == "Kilogram":
			value = value * 0.453592
			print " %k Kilograms" % value
		elif target == "Ounce":
			value = value * 16
			print " %o Ounces" % value
		elif target == "Gram":
			value = value * 453.592
			print " %g Grams" % value
		elif target == "Milligram":
			value = value * 453492
			print " %m Milligrams" % value
		else:
			print "Not a valid choice."
	elif base == "Ounce":
		if target == "Metric Ton":
			value = value * 0.0000283495
			print " %t Metric Tons" % value
		elif target == "Stone":
			value = value * 0.00446429
			print " %s Stones" % value
		elif target == "Kilogram":
			value = value * 0.0283495
			print " %k Kilograms" % value
		elif target == "Pound":
			value = value * 0.0625
			print " %p Pounds" % value 
		elif target == "Gram":
			value = value * 28.3495
			print " %g Grams" % value
		elif target == "Milligram":
			value = value * 28349.5
			print " %m Milligrams" % value
		else:
			print "Not a valid choice."
	elif base == "Gram":
		if target == "Metric Ton":
			value = value * 0.000001
			print " %t Metric Tons" % value
		elif target == "Stone":
			value = value * 0.000157473
			print " %s Stones" % value
		elif target == "Kilogram":
			value = value * 0.001
			print " %k Kilograms" % value
		elif target == "Pound":
			value = value * 0.00220462
			print " %p Pounds" % value
		elif target == "Ounce":
			value = value * 0.035274
			print " %o Ounces" % value
		elif target == "Milligram":
			value = value * 1000
			print " %m Milligrams" % value
		else:
			print "Not a valid choice."
	elif base == "Milligram":
		if target == "Metric Ton":
			value = value * 0.000001
			value = value * 0.001
			print " %t Metric Tons" % value
		elif target == "Stone":
			value = value * 0.001
			value = value * 0.000157473
			print " %s Stones" % value
		elif target == "Kilogram":
			value = value * 0.000001
			print " %k Kilograms" % value
		elif target == "Pound":
			value = value * 0.001
			value = value * 0.00220462
			print " %p Pounds" % value
		elif target == "Ounce":
			value = value * 0.001
			value = value * 0.035274
			print " %o Ounces" % value
		elif target == "Gram":
			value = value * 0.001
			print " %g Grams" % value
		else:
			print "Not a valid choice."
	else:
		print "Not a valid choice."
#elif conv_type == "Volume":
#		base = raw_input("Enter base unit: ")
#		value = int(raw_input("Enter base value: "))
#		target = raw_input("Enter target unit: ")		
#elif conv_type == "Digital Storage":
#		base = raw_input("Enter base unit: ")
#		value = int(raw_input("Enter base value: "))
#		target = raw_input("Enter target unit: ")		
else:
	print "Not a valid choice."