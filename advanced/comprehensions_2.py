lst = [2, 4, 6]
lst2 = [el*2 for el in lst]
print(lst2)
lst3 = [el*100 for el in lst if el >= 4]
print(lst3)

old_set = {10, 20, 56}
new_set = {el * el for el in old_set}
print(new_set)

old_dict = {'a': 100, 'b': 20, 'c': 50}
new_dict = {k: v * 100 for k, v in old_dict.items()}
new_dict_2 = {k: v * 100 for k, v in old_dict.items() if k == 'a'}
print(new_dict, new_dict_2)

old_dict_2 = {'key': 123, 'key_Two': 321, 'key_3': 543}
new_dict_3 = {k.upper(): v for k, v in old_dict_2.items()}
print(new_dict_3)
