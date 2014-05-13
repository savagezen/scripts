#!/usr/local/bin/python2.7
# codeacademy.com - Python
# Tip Calculatory

meal = 44.5
tax = 0.0675
tip = 0.15

print "In this example:"
print " Your meal cost:  $44.50"
print " Tax on the meal was:  6.75%"
print " You plan to tip:  15%"

print "To run the maths you can redefine \"meal\""
print " Variables can be defined in terms of themselves"
meal = meal + meal * tax
print " meal = meal + meal * tax"
print " (new)meal = " 
print meal

print "The variable needs reassigned again to include the tip"
print " meal (new new) = meal (new) + meal (new) * tip"
meal = meal + meal * tip
print " (new new)meal = "
print meal