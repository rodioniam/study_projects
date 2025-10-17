# numbers written as string can be converted to int if only they are integer
a = '42'
print(int(a))

# i can repeat strings by using *
b = 'txt'
print(b*3)

# i can join strings with +
c = a + " " + b
print(c)


# len function
print(len(c))


# special things
multiline = """
First line

Second line
"""
txt = "Some text with 'word' in it"
txt2 = 'Some text with \'word \' in it'

# string methods
s = '   abc  '
print(s.strip())
print(s.strip(' c'))

d = 'a, b, c'
print(d.split(', '))  # returns list

h = ['a', 'b', 'c']
print(''.join(h))
print(', '.join(h))

j = 'UPPER lower cAPITALIZE'
print(j.lower(), j.upper(), j.capitalize())
print(j.islower(), j.isupper(), j.islower())  # returns bool type
print(j.startswith('U'), j.endswith('e'))  # also returns bool type

print(j.find('lower'))  # will return index of requested search
print('lower' in j)  # will return bool type

print(j.replace('lower', 'HUGE'))
old_str = 'lower'
new_str = 'HUGE'
print(j.replace(old_str, new_str))

o = 42
print(f'Using f-strings to insert some variables {o}')
