# EXAMPLE 1

def decorator_func(original_fn):
    def wrapper_fn():
        # this will perform before the execution of origina_fn (func in this case)
        print('Executed before function.')

        result = original_fn()  # this is 'func'

        # this will perform after the execution of origina_fn (func in this case)
        print('Executed after function.')

        return result

    return wrapper_fn


# decorators will perform automatically if assigned before function
@decorator_func
def func():
    print('This is function.')


# im calling only this 'func' (aka original_fn), but because of '@'(aka decorator) i also have 'wrapper_fn' function results
func()


# EXAMPLE 2

# in case of original function having parameters i need to also mention them in decorator function

def dec_fn(fn):
    def wrapper_fn(a, b):  # usually it is better to write (*args, **kwargs) here
        print('Executed before function 1.')

        result = fn(a, b)  # and here (*args, **kwargs)
        # also this part is mandatory so original function still returns its result

        print('Executed after function 1.')

        return result  # this is also needed to original func to work
    return wrapper_fn


@dec_fn
def func_1(a, b):
    print('This is function 1.')
    return (a, b)


result = func_1(100, 50)

print(result)
