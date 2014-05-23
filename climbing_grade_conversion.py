#!/bin/python2.7

###########################
# Climbing Grade Conversion
# Reference - https://play.google.com/store/apps/details?id=com.logicnet.climbingGrades
######################
## Currently Supports:
# Yosemite Decimal System [YDS] 5.7 - 5.15c
# Hueco [Hueco] VB - V16

erorr1 = "Error:  Not a valid choice.  Check your spelling."
print "Available Grade Scales"
print "	YDS"
print "	Hueco"
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
	else:
		print error1
elif base == "Hueco":
	value = raw_input("Enter base grade [V0 - V14]: ")
	target = raw_input("Enter target scale: ")
	if target == "YDS":
		if value == "VB":
			print "5.7"
		elif value == "V0-"
			print ".58 / 5.9"
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
else:
	print error1