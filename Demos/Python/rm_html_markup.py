#!/bin/python2.7
# HTML markup remover
# Udacity - Software Debugging
# https://www.youtube.com/watch?v=mPKT3ATZIws#t=32

html_code1 = raw_input("Enter a short HTML code: (<b>foo</b>)  ")
html_code2 = raw_input("Enter another snippet: (\'xyz\')  ")
html_code3 = raw_input("Now get more complicated: (\'\"<b>foo</b>\"\')  ")

def remove_html_markup(s):
	tag = False
	out = ""

	for c in s:
#		print c									# Prints character
#		print tag								# Prints variable
#		print quote								# Prints status of quote

		if c == "<" and not quote:				# Start of markup
			tag = True
		elif c == ">" and not quote:			# End of markup
			tag = False
		elif (c == ' " ' or c == " ' ") and tag:	# Checking for quotations in markup
			# w/o () implies - c == ' " ' or (c == " ' " and tag):
			# "and" has greater priority over "or"
			quote = not quote
		elif not tag:
			out = out + c
	return out

print remove_html_markup(html_code1)
print remove_html_markup(html_code2)
print remove_html_markup(html_code3)