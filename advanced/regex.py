# regex are a tool to work with strings. I can search for specific charachters, letters, symbols, words etc.
# to use regex i need to import re and also use raw strings
# https://regex101.com/ is good website to check regex

import re

example = 'This is example 123 of regex'
# findall searches for all matches in a string, returns list
a = re.findall(r'\d+', example)
print(a)

# also searches for a match by template, only a first one and returns special object
b = re.search(r'\d+', example)
print(b)  # <re.Match object; span=(16, 19), match='123'>
# span is boundaries of where match was found

c = re.split(' ', example)  # splits string into list by chosen template
print(c)

d = re.sub(r'\d+', 'CHANGED', example)  # replaces by given template
print(d)

# checks only beggining of the string, if does not match returns None
e = re.match('This', example)
print(e)  # returns Match object
print(e.group())  # returns match itself

# this way i can store regex and use it later
comp = re.compile(r'\d+', re.MULTILINE)
print(comp.findall(example))
