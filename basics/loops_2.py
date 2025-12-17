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

# 1

d = {'a': 444, 2: 555, 'c': 666}


def dict_to_list(dict):
    list = []

    for k, v in dict.items():
        if isinstance(k, int):
            list.append((k*2, v))
        else:
            list.append((k, v))

    return list


res = dict_to_list(d)

print(res)
print(type(res[0]))


# 2

l = ['aaa', 'bbb', 23, 555, 345.5, 10.0, True, False]


def filter_list(list_to_filter, value_type):

    l2 = []

    for el in list_to_filter:
        # if i use isinstance() it will also return [True, False] since in Python they are 1 and 0
        if type(el) == value_type:
            l2.append(el)

    if len(l2) == 0:
        return list_to_filter
    else:
        return l2


res_2 = filter_list(l, int)

print(res_2)

# 2.5


def filter_list_2(list_to_filter, value_type):
    return filter(lambda x: type(x) == value_type, list_to_filter)


res_3 = list(filter_list_2(l, int))

print(res_3)
