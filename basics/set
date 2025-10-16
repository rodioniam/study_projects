# collection, that stores only unique elements without any particular order. mutable
a = {1, 2, 2, 'abs'}
print(a)

# sets are a good way of clearing a list from duplicates for example. It will change the order though

b = [2, 55, 43, 55, 76, 55]
c = list(set(b))
print(c)

# set methods
d = {1, 2, 3}
d.add(5)
d.discard(2)


s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 7, 8, 9}
s3 = {1, 2, 3}
s4 = {100, 1000}
print(s1.intersection(s2))  # shows what elemens are the same in both sets
# checks if sets have same elements, returns bool type, False = there are same elements
print(s1.isdisjoint(s2), s1.isdisjoint(s4))
# checks if one set has all elements of another set
print(s1.issuperset(s3), s1.issuperset(s2))
print(s3.issubset(s1))  # checks if this set is subset of another
print(s1.union(s2))  # shows all same elements and those that are only in second one
