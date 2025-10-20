# lambda < arguments > : < what to do with arguments > , < from where >
from functools import reduce
lst = [22, 32, 4, 5, 10, 6]


# lambda + filter: filterls with function
result = list(filter(lambda el: el >= 10, lst))

print(result)


# lambda + map: works like 'for' loop
result_2 = list(map(lambda el: el*100, lst))

print(result_2)


lst1 = [1, 2, 3, 4]
lst2 = [2, 3, 4, 5]
# map also works with several collections
result_3 = list(map(lambda x, y: x * y, lst1, lst2))

print(result_3)


lst3 = [1, 10, -1, 5, 6, 3]
# reduce applies function to each argument and to a result of previous interaction
result_4 = reduce(lambda x, y: x + y, lst3)
# equals: 1 + 10 - 1 + 5 + 6 + 3 = 24
print(result_4)

lst4 = ['123', '12345', '123', '1234']
# returns longest element from list
result_5 = reduce(lambda x, y: x if len(x) > len(y) else y, lst4)

print(result_5)

# sorting with lambda
lst5 = [['John', 25], ['Marry', 16], ['Lucio', 54]]

print(sorted(lst5, key=lambda x: x[1]))
