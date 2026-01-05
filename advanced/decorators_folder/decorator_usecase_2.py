# arguments validation

def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, float) and not isinstance(arg, int):
                raise ValueError(f'Type of the {arg} is {type(arg)}.',
                                 'All arguments must be integer or float.')

        result = fn(*args, **kwargs)
        return result

    return wrapper


@validate_args
def sum_nums(a, b):
    return a+b


try:
    print(sum_nums(7, 3))
    print(sum_nums(7.4, 2.6))
    print(sum_nums(a=7.4, b='2.6'))
except ValueError as e:
    print(e)
