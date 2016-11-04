#!/bin/python/2.7
# codecademy.com - Python
# Date and Time

print "Python can import commands from the shell"
print " Example:  \"from datetime import datetime\""
from datetime import datetime

print "You can use a function to call the datetime."
print " Set variable = datetime.now()"
now = datetime.now()
print now

print "You can also elicit explicit parts of what is imported."
print " from datetime import datetime"
print " now = datetime.now()"
print " current_year = now.year"
current_year = now.year
print now.year
print " current_month = now.month"
current_year = now.month
print now.month
print " current_day = now.day"
current_day = now.day
print now.day

print "You can still use %s so substitute functions like other variables."
print "%s-%s-%s" % (now.year, now.month, now.day)
print "The same can be done with HH:MM:SS part of \"datetime\""
print " current_hour = now.hour"
current_hour = now.hour
print " current_minute = now.minute"
current_minute = now.minute
print " current_second = now.second"
current_second = now.second
print "%s:%s:%s" % (now.hour, now.minute, now.second)

print "You can put it all together to get mm/dd/yyyy hh:mm:ss"
print " print \"%s/%s/%s %s:%s:%s\" % (now.month, now.day, now.year, now.hour, now.minute, now.second)"
print "%s/%s/%s %s:%s:%s" % (now.month, now.day, now.year, now.hour, now.minute, now.second)