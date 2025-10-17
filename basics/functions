def greeting():  # creating function
    print('Hello, World!')


greeting()  # calling function, so it does its thing


# instead of print i should use return, so function only returns the result
def func():
    return 2+3


print(func())

# i can also assign function to a variable
a = func()
print(a)


# if i dont know what func will do yet, i can write pass or ...
def func_pass():
    pass


# i can give arguments to a function
def num_sum(a, b):
    return a + b


print(num_sum(2, 2))  # now i have to give some values to function so it works


# i also can give default value for an argument
def pow(a, b=2):
    return a**b


print(pow(2))  # if i dont give second argument, func will take default one


# there are positional arguments and key word arguments
def sum_nums(a, b, c=3, d=4):
    return a + b + c + d


b = sum_nums(a, b=-4)  # b is keyword argument, since i specified its value
print(b)


# i can add *, so all args before it are positional and all after are kwargs
def func_2(a, b, *, c, d):
    return a + b + c + d


# this way i have to specify arg with its value
print(func_2(2, 2, c=-2, d=-2))


# i can use *args, **kwargs construction
def func_3(*args, **kwargs):
    print(args)  # returns tuple
    print(kwargs)  # returns dict


func_3(2, 3, 'abc', g='kwarg', h=555)


# there is a thing with funcs that all variables inside them are only usebale by its function
# i cant call them outside of the function, only if i use global

def glob():
    global a
    a = 10


print(a)  # here i called a without calling function


# i can document functions, give them short explanation
def exp():
    """Description of this function"""
    return 1


exp()
