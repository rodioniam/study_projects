# collection, where elements are keys:values
a = {1: 'abc', 2: 'def'}

# i can access value by key
print(a[2])

# if i want to add new element
a[3] = 'ghi'
print(a)  # it will rewrite value if key is already in dict

# keys can only be immutabe objects


# dict methods

b = a.copy()
b.clear()
print(b)
a.get(1)  # this method returns value, but without an error if key is not present in dict
a.get(4, -1)  # i can also add default value to return if key is not present
print(a.keys())  # return special object, contains keys
print(a.values())  # return special object, contains values
print(a.items())  # return special object, contains keys and values
c = {1: 'abc', 2: 'def'}
d = {555: True, 'KEY': 484}
# adds all elements from one dict to another, similar keys will be overwritten
c.update(d)
print(c.pop('KEY'))  # gives value by key, deletes it from source
c.popitem()  # deletes last item from dict
