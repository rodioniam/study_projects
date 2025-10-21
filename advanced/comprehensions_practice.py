lst1 = [2, -4, 5, -6, 3]

# sum only positive numbers
a = sum(el for el in lst1 if el > 0)

print(a)

# return only positive numbers mult by 2
b = [el*2 for el in lst1 if el > 0]

print(b)


# make a dict from two lists
keys = [1, 2, 3]
values = ['a', 'b', 'c']

# zip combines two or more collections el by el
d = {k: v for k, v in zip(keys, values)}
print(d)
