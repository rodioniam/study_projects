from functools import reduce
import re


# return args and kwargs from function as dict
def func(*args, **kwargs):
    result = {f'positional_{k+1}': v for k, v in enumerate(args)}
    result.update(kwargs)
    return result


print(func(43, 111, a='abc', b='cde'))


# return sum of squares of numbers in list
nums = [2, 4, 5]
# last number is initial - 3rd arg in reduce - sets starting position
result = reduce(lambda x, y: x + y**2, nums, 0)
print(result)


# check list of phone numbers: format them to template and return Invalid if number is incorrect.
# number must begin with 7 or 8
# must be 11 digits
# Template - +7 (111) 111-1111
phones = ['+79262345566', '8 985 555 13 12',
          '7(999)123-3434', '6 777 455 32 32', '8 985 555 13 122', '+7926234556']


def phone_check(phones):

    clear = re.compile(r'\D+', re.MULTILINE)
    format = re.compile(r'^(7|8)(\d{3})(\d{3})(\d{4})', re.MULTILINE)

    cleaned_phones = []
    result = []

    for phone in phones:
        if len(clear.sub('', phone)) == 11 and clear.sub('', phone).startswith(('7', '8')):
            cleaned_phones.append(clear.sub('', phone))
        else:
            cleaned_phones.append('Invalid')

    for val in cleaned_phones:
        result.append(format.sub(r'+7 (\2) \3-\4', val))

    return result


print(phone_check(phones))


# find dates in text
text = 'This some 2024-09-11 text with 1999-11-31 dates in it. Also some 1985-13-23 incorrect ones 2001-04-65'


def find_dates_in_text(text):
    match = re.compile(
        r"(?:\d{4})-(?:0[0-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])", re.MULTILINE)
    return match.findall(text)


print(find_dates_in_text(text))
