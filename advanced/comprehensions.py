# it is some kind of collection generator
# [element for element in collection]
# first element - what to do
# second element - for what element
# collention - where to do

lst1 = [1, 2, 3, 4, 5]
result1 = []
for el in lst1:
    result1.append(el*2)
print(result1)

# or i can do the same with list comprehension

result2 = [el*2 for el in lst1]
print(result2)


# comprehensions accept if - else statement
lst2 = [23, 4, 63, 10, 22, 8, 100]
bigger_50 = [el if el > 50 else 1 for el in lst2]  # if else
smaller_50 = [el for el in lst2 if el < 50]  # only if
print(bigger_50)
print(sorted(smaller_50))

# list comprehensions can work with sub collecions
'[<what to do> for <global var> in <global collection> for <sub var> in <global var>]'
a = [[1, 2, 3], [], [4, 5, 6, 7]]
result3 = []

# with 'for' loop
for sublst in a:
    for i in sublst:
        result3.append(el)

# with list comprehension
result4 = [el for sublst in a for i in sublst]

print(result3)
print(result4)


# set and dictionary comprehensions are same as list, but with different () {}

lst3 = [1, 2, 3, 4]

result5 = {el**2 for el in lst3}

print(result5)
print(type(result5))

# for dict comprehension i need to write for keys and values
values = ['abc', 'def', 'ghi', 'jkl']

d = {k: v for k, v in enumerate(values, 1)}

print(d)
