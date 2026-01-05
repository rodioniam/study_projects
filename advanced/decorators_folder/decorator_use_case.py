# logging data

def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Function name is '{fn.__name__}'.")
        print(f"Function arguments are: {args}, {kwargs}.")
        result = fn(*args, **kwargs)

        return result

    return wrapper


@log_function_call
def mult(a, b):
    return a*b


print(mult(5, b=2))

print('')


@log_function_call
def text(a, b):
    return f"{a} {b}"


print(text('Hello', 'world!'))
