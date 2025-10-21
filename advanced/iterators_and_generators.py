# iterator is an object which can can be used in 'for' loop or with next() function
lst = [1, 2, 3]  # iterator

it = iter(lst)  # 'it' is now iterator object

print(next(it))  # used with next()

for el in lst:  # used in 'for' loop
    print(el)

# generator is a special type of iterator which is made by function with 'yield' instead of 'return'
# generators generate values by one and dont need to generate whole range. Also they continue from the place where they stopped


def pow(x):  # generator
    while True:
        yield x**2
        x += 1


x = pow(5)  # generator object
d = pow(10)  # different generator object, but with same logic inside

print(next(x))
print(next(d))
