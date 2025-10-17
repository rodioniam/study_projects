# tuples are like lists, but immutable
a = (1, 2, 'abc', [1, 2])
print(type(a))

# i can change mutable objects inside tuple
b = []
c = [4, 5]
d = (b, c)
b.append(1)
b.append(2)
print(d)
