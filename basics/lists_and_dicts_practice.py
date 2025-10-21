# function that takes list and index and returns value from list by index
lst = ['abc', 44, [1, 2]]
index = 0


def get_value_by_index(index, lst):
    if lst and type(lst) == list and index <= len(lst):
        return lst[index]
    return None


print(get_value_by_index(index, lst))


# making list of lists one list
def list_flatten(lst):
    result_list = []
    for sublst in lst:
        if type(sublst) == list:
            for el in sublst:
                result_list.append(el)
        else:
            result_list.append(sublst)
    return result_list


print(list_flatten(lst))


# insert value into a list on a specific place
lst2 = [1, 2, 3]
position = 1
value = 'abc'
rep = 2


def list_insert(lst2, position, value, rep):
    if len(lst2) < position:
        return -1

    lst2[position:position] = [value] * rep
    return lst2


print(list_insert(lst2, position, value, rep))

# generate numbers in range
start = 30
end = 20


def generate_values(start, end):
    a = 1 if start <= end else -1  # added this so it generate in descending order
    result = list(range(start, end + 1 * a, 1 * a))
    return result


print(generate_values(start, end))

# merge two dicts, so keys from first one become keys of merged dict and values with same keys become a list
dict1 = {1: 'abc', 2: 'def'}
dict2 = {3: 'ghi', 2: '234'}


def merge_dicts(dict1, dict2):
    result_dict = dict1.copy()

    for key, value in dict2.items():
        if key in result_dict:
            if isinstance(result_dict[key], list):
                result_dict[key].append(value)
            else:
                result_dict[key] = [result_dict[key], value]
        else:
            result_dict[key] = value
    return result_dict


print(merge_dicts(dict1, dict2))


# make a dict with keys as el from collection and values as times they appears in collection
collection = 'This is a string'


def count_el(collection):
    result_dict = {}
    for el in collection:
        if el in result_dict:
            result_dict[el] += 1
        else:
            result_dict[el] = 1
    return result_dict


print(count_el(collection))


# sort dictionary with different variables
d = {3: 'b', 2: 'a', 1: 'c'}
type = 'valuewise'  # 'keywise'
order = 'desc'  # 'asc'


def dict_sorted(d, type, order):
    if type == 'keywise':
        if order == 'asc':
            return dict(sorted(d.items(), key=lambda x: x[0], reverse=False))
        return dict(sorted(d.items(), key=lambda x: x[0], reverse=True))
    else:
        if order == 'asc':
            return dict(sorted(d.items(), key=lambda x: x[1], reverse=False))
        return dict(sorted(d.items(), key=lambda x: x[1], reverse=True))


print(dict_sorted(d, type, order))
