#!/bin/python2.7
# codecademy - Python
# Lists

animal = raw_input('What is your favorite animal? ')
zoo_animals = ['pangolin', 'cassowary', 'sloth', animal];			# List of values

if len(zoo_animals) > 3:
	print 'The first animal at the zoo is the ' + zoo_animals[0]	# Identify list item by index
	print 'The second animal at the zoo is the ' + zoo_animals[1]	# Indexes start with '0'
	print 'The thrid animal at the zoo is the ' + zoo_animals[2]
	print 'The fourth animal at the zoo is the ' + zoo_animals[3]

numbers = [5, 6, 7, 8]
print 'Adding the numbers at indicies 0 and 2...'
print numbers[0] + numbers[2]
print 'Adding the second and fourth number...'
print numbers[1] + numbers[3]
# Remove list items with "listname.remove['variable']

print 'You can also redefine variables by index number'
print '	Rceall the above zoo example...'
animal = raw_input('Enter the name of another animal: ')
zoo_animals[3] = animal
print zoo_animals

letters = ['a', 'b', 'c']
letters.append('d')													# Add () to end of list
print len(letters)													# Counts items in list
print letters

suitcase = ['sunglasses', 'hat', 'passsport', 'laptop', 'suit', 'shoes']	# A list and its items
first = suitcase[0:2]												# Print only a section of the list
middle = suitcase[2:4]												# Beginning index number on the left of the ':'
last = suitcase[4:6]												# Up to (but not including) the right index number
print suitcase
print first + middle + last

animals = 'catdogfrog'												# You can break up strings the same way
print animals
cat = animals[:3]													# 'animals' from beginning to (but not  including) 3rd index
dog = animals[3:6]
frog = animals[6:]													# From index 6 to the end
print cat + dog + frog

animals = ['aardvark', 'badger', 'duck', 'emu', 'ennec fox']		# Replacing items in list
print animals
duck = animals.index('duck')										# variable = list.index('item')
animals.insert(duck, 'cobra')										# list.insert(index, 'item')
print animals														# 'item' replaces what is at index 'duck'

my_list = [1,2,3,4,5,6]												# Manipulate every item in list - 'for'
#for variable in list_name:
#	do stuff
for number in my_list:												# For every number in the list
	print 2 * number												# Multiply it by two

start_list = [5,4,1,2,4]											# Defined list
square_list = []													# Undefined list
for number in start_list:
	square_list.append(number**2)									# Square each item in start_list and add to the end of square_list
	square_list.sort()												# Sort entires alpha-numerically
print start_list
print square_list

print 'Dictionaries are good for paring data.'
print 	'When using len() each pair is only counted once'
print		'even thoug lists ca be inside dictionaries'
dictionary = {'key1' : 1, 'key2' : 2}								# Dictionaries use {} rather than []
print dictionary['key1']											# Will print the corresponding entery to key1
dictionary['key3'] = 2.5											# Add 'key3' to the dictionary and corresonding to 2.5
print 'One example of a dictionary would be a menu'														# Can also reassign value rather than delete / add

# Lists inside Dictionaries & Review
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

inventory['pouch'].sort() 

inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()										# Perform list function on list inside dictionary

inventory['backpack'].remove('dagger')								# Same syntax as above:  dictionary[list_name].function(item)

inventory['gold'] = 550