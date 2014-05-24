#!/bin/python2.7

###########################
# Climbing Grade Conversion
# Reference - https://play.google.com/store/apps/details?id=com.logicnet.climbingGrades
######################
## Currently Supports:
# Yosemite Decimal System [YDS] 5.7 - 5.15c
# Hueco VB - V16
# French 5a - 9b+ 

error1 = "Error:  Not a valid choice.  Check your spelling."
print "NOTE:  Climbing grades are inherently subective.  Therefore converting between them is also subjective."
print "Conversions are not perfect matches.  If you get an error message try adding / subtracting a half (+/-) grade."
print "Available Grade Scales"
print "	YDS"
print "	Hueco"
print "	French"
base = raw_input("Select base scale: ")
if base == "YDS":
	value = raw_input("Enter base grade [5.7 - 5.14d]: ")
	target = raw_input("Enter target scale: ")
	if target == "Hueco":
		if value == "5.7":
			print "VB"
		elif value == "5.8":
			print "V0-"
		elif value == "5.9":
			print "V0-"
		elif value == "5.10a":
			print "V0"
		elif value == "5.10b":
			print "V0+"
		elif value == "5.10c":
			print "V0+"
		elif value == "5.10d":
			print "V1"
		elif value == "5.11a":
			print "V2"
		elif value == "5.11b":
			print "V3"
		elif value == "5.11c":
			print "V3"
		elif value == "5.11d":
			print "V3+"
		elif value == "5.12a":
			print "V4"
		elif value == "5.12b":
			print "V4+"
		elif value == "5.12c":
			print "V5"
		elif value == "5.12d":
			print "V6"
		elif value == "5.13a":
			print "V7"
		elif value == "5.13b":
			print "V7"
		elif value == "5.13c":
			print "V8"
		elif value == "5.13d":
			print "V9"
		elif value == "5.14a":
			print "V10"
		elif value == "5.14b":
			print "V10"
		elif value == "5.14c":
			print "V11"
		elif value == "5.14d":
			print "V12 / v13"
		elif value == "5.15a":
			print "V14"
		elif value == "5.15b":
			print "V5"
		elif value == "5.15c":
			print "V16"
		else:
			print error1
	elif target == "French":
		if value == "5.7":
			print "5a"
		elif value == "5.8":
			print "5b"
		elif value == "5.9":
			print "5c"
		elif value == "5.10a":
			print "6a"
		elif value == "5.10b":
			print "6a+"
		elif value == "5.10c":
			print "6b"
		elif value == "5.10d":
			print "6b+"
		elif value == "5.11a":
			print "6c"
		elif value == "5.11b":
			print "6c / 6c+"
		elif value == "5.11c":
			print "6c+"
		elif value == "5.11d":
			print "7a"
		elif value == "5.12a":
			print "7a+"
		elif value == "5.12b":
			print "7b"
		elif value == "5.12c":
			print "7b+"
		elif value == "5.12d":
			print "7c"
		elif value == "5.13a":
			print "7c+"
		elif vale == "5.13b":
			print "8a"
		elif value == "5.13c":
			print "8b"
		elif value == "5.13d":
			print "8b"
		elif value == "5.14a":
			print "8b+"
		elif value == "5.14b":
			print "8c"
		elif value == "5.14c":
			print "8c+"
		elif value == "5.14d":
			print "9a"
		elif value == "5.15a":
			print "9a+"
		elif value == "5.15b":
			print "9b"
		elif value == "5.15c":
			print "9b+"
		else:
			print error1
	else:
		print error1
elif base == "Hueco":
	value = raw_input("Enter base grade [V0 - V14]: ")
	target = raw_input("Enter target scale: ")
	if target == "French":
		if value == "VB":
			print "5a"
		elif value == "V0-":
			print "5b / 5c"
		elif value == "V0":
			print "6a"
		elif value == "V1":
			print "6b+"
		elif value == "V2":
			print "6c"
		elif value == "V3":
			print "6c / 6c+"
		elif value == "V3+":
			print "7a"
		elif value == "V4":
			print "7a+"
		elif value == "V4+":
			print "7b"
		elif value == "V5":
			print "7b+"
		elif value == "V6":
			print "7c"
		elif value == "V7":
			print "7c+ / 8a"
		elif value == "V8":
			print "8a+"
		elif value == "V9":
			print "8b"
		elif value == "V10":
			print "8b+ / 8c"
		elif value == "V11":
			print "8c+"
		elif value == "V12":
			print "9a"
		elif value == "V13":
			print "9a"
		elif value == "V14":
			print "9a+"
		elif value == "V15":
			print "9b"
		elif value == "V16":
			print "9b+"
		else:
			print error1
	elif target == "YDS":
		if value == "VB":
			print "5.7"
		elif value == "V0-":
			print "5.8 / 5.9"
		elif value == "V0":
			print "5.10a"
		elif value == "V0+":
			print "5.10b / 5.10c"
		elif value == "V1":
			print "5.10d"
		elif value == "V2":
			print "5.11a"
		elif value == "V3":
			print "5.11b"
		elif value == "V3+":
			print "5.11d"
		elif value == "V4":
			print "5.12a"
		elif value == "V4+":
			print "5.12b"
		elif value == "V5":
			print "5.12c"
		elif value == "V6":
			print "5.12d"
		elif value == "V7":
			print "5.13a"
		elif value == "V8":
			print "5.13c"
		elif value == "V9":
			print "5.13d"
		elif value == "V10":
			print "5.14a"
		elif value == "V11":
			print "5.14c"
		elif value == "V12":
			print "5.14d"
		elif value == "V13":
			print "5.14d"
		elif value == "V14":
			print "5.15a"
		elif value == "V15":
			print "5.15b"
		elif value == "V16":
			print "5.15c"
		else:
			print error1
	else:
		print error1
elif base == "French":
	value = raw_input("Enter base grade [5a - 9b+]: ")
	target = raw_input("Enter target scale: ")
	if target == "Hueco":
		if value == "5a":
			print "VB"
		elif value == "5b":
			print "V0-"
		elif value == "5c":
			print "V0-"
		elif value == "6a":
			print "V0"
		elif value == "6a+":
			print "V0+"
		elif value == "6b":
			print "V0+"
		elif value == "6b+":
			print "V1"
		elif value == "6c":
			print "V2"
		elif value == "6c+":
			print "V3"
		elif value == "7a":
			print "V3+"
		elif value == "7a+":
			print "V4"
		elif value == "7b":
			print "V4+"
		elif value == "7b+":
			print "V5"
		elif value == "7c":
			print "V6"
		elif value == "7c+":
			print "V7"
		elif value == "8a":
			print "V7"
		elif value == "8a+":
			print "V8"
		elif value == "8b":
			print "V9"
		elif value == "8b+":
			print "V10"
		elif value == "8c":
			print "V10"
		elif value == "8c+":
			print "V11"
		elif value == "9a":
			print "V12 / V13"
		elif value == "9a+":
			print "V14"
		elif value == "9b":
			print "V15"
		elif value == "9b+":
			print "V16"
		else:
			print error1
	elif target == "YDS":
		if value == "5a":
			print "5.7"
		elif value == "5b":
			print "5.8"
		elif value == "5c":
			print "5.9"
		elif value == "6a":
			print "5.10a"
		elif value == "6a+":
			print "5.10b"
		elif value == "6b":
			print "5.10c"
		elif value == "6b+":
			print "5.10d"
		elif value == "6c":
			print "5.11a"
		elif value == "6c+":
			print "5.11c"
		elif value == "7a":
			print "5.11d"
		elif value == "7a+":
			print "5.12a"
		elif value == "7b":
			print "5.12b"
		elif value == "7b+":
			print "5.12c"
		elif value == "7c":
			print "5.12d"
		elif value == "7c+":
			print "5.13a"
		elif value == "8a":
			print "5.13b"
		elif value == "8a+":
			print "5.13c"
		elif value == "8b":
			print "5.13d"
		elif value == "8b+":
			print "5.14a"
		elif value == "8c":
			print "5.14b"
		elif value == "8c+":
			print "5.14c"
		elif value == "9a":
			print "5.14d"
		elif value == "9a+":
			print "5.15a"
		elif value == "9b":
			print "5.15b"
		elif value == "9b+":
			print "5.15c"
		else:
			print error1
	else:
		print error1
else:
	print error1