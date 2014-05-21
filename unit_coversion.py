#!/bin/python2.7
# Unit Converter - based on Google conversions

print "Available conversions:"
print "	[1] Temperature"
print "	[2] Length"
print "	[3] Mass"
print "	[4] Volume"
print "	[5] Digital Storage"
conv_type = raw_input("Select conversion type: ")

# Temnperature
if conv_type == "Temperature" or "1":
	base = raw_input("Enter base unit [Celcius / Fahrenheit]: ")
	if base == "Celcius":
		value = int(raw_input("Enter value: "))
		value = value * 9
		value = value / 5
		value = value + 32
		print " %d Degrees Fahrenheit" % value
	elif:
		value = int(raw_input("Enter value: "))
		value = value - 32
		value = value * 5
		value = value / 9
		print " %d Degrees Celcius" % value
	else:
		print "Not a valid choice"

# Length
elif conv_type == "Length" or "2":
	print "Select base unit: "
	print "	Kilometer"
	print "	Mile"
	print "	Meter"
	print "	Yard"
	print "	Foot"
	print "	Inch"
	print "	Centimeter"
	base = raw_input(" ")
	if base == "Kilometer":
		value = int(raw_input("Enter base value: "))
		target = raw_input("Enter target unit: ")
		if target == "Mile":
			value == value * 0.621371
			print " %m Miles" % value
		elif target == "Meter":
			value == value * 1000
			print " %m Meters" % value
		elif target == "Yard":
			value == value * 1093.61
			print " %y Yards" % value
		elif target == "Foot":
			value == value * 3280.84
			print " %f Feet" % value
		elif target == "Inch":
			value == value * 39370.1
			print " %i Inches" % value
		elif target == "Centimeter":
			value == value * 100000
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
				value = value * 0.833333
				value = value * 0.0003048
				print " %k Kilometers" % value
			elif target == "Mile":
				value = value * 0.833333
				value = value * 0.000189394
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
				value = value * 0.01
				value = value * 0.001
				print " %k Kilometers" % value
			elif target == "Mile":
				value = value * 0.0328084
				value = value * 0.000189394
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
#elif conv_type == "Length" or "2"
#elif conv_type == "Mass" or "3"
#elif conv_type == "Volume" or "4"
#else:
#	conv_type == "Digital Storage" or "5"