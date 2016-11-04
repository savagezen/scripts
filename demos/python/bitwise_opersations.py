#!/bin/python2.7
# codecademy - Python
# Bitwise Operations

# Bitwise operations directly manipulate bits in computers
print "Basic bitwise operations:"
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

# Counting isually base 10 (0-9), in binary its base 2 (0 or 1)
# In Python numbers are written in binary form by starting with "0b"; 1010 is like "10"
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print 0b1 + 0b11
print 0b11 * 0b11

print "one = 0b1"
print "two = 0b10"
print "three = 0b11"
print "four = 0b100"
print "five = 0b101"
print "six = 0b110"
print "seven = 0b111"
print "eight = 0b1000"
print "nine = 0b1001"
print "ten = 0b1010"
print "eleven = 0b1011"
print "twelve = 0b1100"

print "\'bin()\' is used to find the binary form of a number:"
num = input("Enter a number to test:  ")
bin(num)

# int's 2nd parameter
print "REMINDER:  int() turns non-integers into integers; \"43\" to 42."
print "	int() can also take a second paramater; int(\"para1\", para2)"
print "	  This converts the string (para1) that is in baseX (para2) to a base 10 integer"
print "	  For example:  int(\"10\", 2) = 2"
print "	  NOTE:  The \"ob\" expression before the binary form is not neeeded"
print "		print int(\"0b100\",2) ---> 4"
print "		print int(\"100\",2) -----> 4"

# Left / Right Sliding
print "\"<<\" indicates shift left"
print "	5 << 3 - move all 1s and 0s in bin(5) to the LEFT 3 spaces"
print "	5 << 3 = 40"
print "	0b101 << 3 = 40"
print "	0b101 << 3 = 0b101000"

print "\">>\" indicates shift right"
print "	50 >> 4 - move all 1s and 0s in bin(1) to the RIGHT 4 spaces"
print "	50 >> 4 = 3"
print "	0b110010 >> 4 = 3"
print "	0b110010 >> 4 = 0b11"

# Using AND (&)
print "\"bin(var1 & var2)\" compares the binaries of var1 and var2"
print "	Example:  bin(0b1110 & 0b101) = bin(15 & 5)"
print "	- bin() converts var1 and var2 to binaries"
print "	- compares the two binaries"
print "	- notes switches that are the same in BOTH var1 and var2"
print "	- returns the resulting binary"
num1 = input("Enter the first number for a bin(AND) operation:  ")
num2 = input("Enter the second number for a bin(AND operation:  ")
bin_and = bin(num1 & num2)
bin_and_dec = int(bin_and,2)
print "The binaries found in BOTH %s and %s = %s (%s)" % (num1,num2,bin_and,bin_and_dec)

# Using OR (|)
print "\"bin(var1 | var2)\" also compares the binaries of var1 and var2"
print "	Example:  bin(0b1110 | 0b101) = bin(15 | 5)"
print "	- OR searches for other binaries switched on in EITHER va1 or var2"
print "	- returns the binary result"
num3 = input("Enter the first number for a bin(OR) operation:  ")
num4 = input("Enter the second number for a bin(OR) operation:  ")
print "Executing:  bin(%s | %s)" % (num3,num4)
bin_or = bin(num3 | num4)
bin_or_dec = int(bin_or,2)
print "The binaries found in EITHER %s or %s = %s (%s)" % (num3,num4,bin_or,bin_or_dec)

# Using XOR (^)
print "XOR = exclusive or"
print "	Example:  bin(00101010 ^ 00001111) = bin(42 ^ 15)"
print "	- XOR seraches for binaries turned on in either variable"
print "	- but NOT binaries switched on in both"
num5 = input("Enter the first nubmer for a bin(XOR) operation:  ")
num6 = input("Enter the second number for a bin(XOR) operation:  ")
bin_xor = bin(num5 ^ num6)
bin_xor_dec = int(bin_xor,2)
print "The binaries found in either, but NOT both %s and %s = %s (%s)" % (num5,num6,bin_xor,bin_xor_dec)

# Using NOT (~)
print "NOT (~) shows binary switches that are NOT found in the variable's binary"
print "print ~1 ---> -2"
print "print ~10 ---> -11"
print "print ~-100 ---> 99"

# Using Bit Mask
print "A bit mask can check if a specific bit is on / off"
print "	Example:  Check if 4th bit is on / off"
check_bit = input("Enter an integer to check:  ")
# The input neets to be an integer, don't include a bin() expression, that's a string
def check_bit4(number):
	mask = 0b1000		# This is where you turn on / off the desire bit to check against
	desired = number & mask
	if desired > 0:
		print "on"
	else:
		print "off"
check_bit4(check_bit)

print "A bit mask can also turn a specific bit on / off"
print "  Example:  Turn on the 4th bit if it is not already"
bit_on = input("Enter an integer to check:  ")
mask = 0b1000
print bin(bit_on | mask)

print "You can also flip all the bits in a number"
print "	Turn the ones that are on, off; and vice versa"
flip = input("Enter an integer to check:  ")
print "The \"mask\" needs to be the same number of bits as the entered number:"
bin_flip = bin(flip)
print "The binary of your number is %s" % (bin_flip)
mask = input("Enter a binary of the same length with all bits ON:  ")
print bin(flip ^ mask)

print "Finally you can move operators left (<<) or right (>>)"
print "	For example:  Turn on the Nth bit of numberX"
shift_int = input("Enter an integer:  ")
shift_n = input("Enter number of bits to shift:  ")
mask = 0b1 << (shift_n - 1)	# This needs to be one less than the desire number of spaces
shift = shift_int ^ mask
print bin(shift)