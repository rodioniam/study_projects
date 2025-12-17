numbers = [2, 4, 6, 8]

result = []

for n in numbers:
    result.append(n*2)

print(result)


dict_nums = {'a': 1, 'b': 2, 'c': 3}

key = []
values = []

for k, v in dict_nums.items():
    key.append(k)
    values.append(v)

print(key, values)
