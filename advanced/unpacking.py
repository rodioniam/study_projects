# i can use * to unpack collections

l = [1, 2, 3, 4]

a, *b = l  # this way first el from l will be given to 'a' variable, rest - to 'b'

print(a)
print(b)

# i can use * when i need to unpack several collection to one

lst = [1, 2, 3]
tuple = (4, 5, 6)
set = {7, 8, 9}
dict = {10: 'a', 11: 'b', 12: 'c'}  # only keys will be unpacked

collection = [*lst, *tuple, *set, *dict]

print(collection)

# using * i can unpack/combine two dicts into one

d1 = {1: 'a', 2: 'b'}
d2 = {'abc': True, 'key': 'value', 2: 'bbb'}

# same keys will be overwritten by values from last unpacked collection
d_all = {**d1, **d2}
print(d_all)
