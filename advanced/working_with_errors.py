def example():
    try:
        'code that could potentially cause an error'
    except:
        'code that will be run if an error occurs'


def div(a, b):
    try:
        return a/b
    except:
        return 'an error'


print(div(4, 0))


# if i want to catch an error i can write like this


def div_2(a, b):
    try:
        return a/b
    except Exception as error:
        return error


print(div_2(4, 0))


# i can use mupliple exceptions, if i know what types of errors i can get

def div_3(a, b):
    try:
        return a/b
    except ZeroDivisionError as err:  # if i divide by 0
        print(1)  # to distinguish which one i cought
        return err
    except TypeError as err:  # if i dont give a number
        print(2)
        return repr(err)  # i can use this function to get full error


print(div_3(4, 0))
print(div_3(4, 'a'))


# i can also use else and finally in try...except...

def div_4(a, b):
    try:
        a/b
    except Exception as err:
        return repr(err)
    else:
        # this section will run if 'try' did not cause an error
        return a/b
    finally:
        # this section will run regardless of errors and result of 'try'
        print('Done')


print(div_4(4, 2))


# if i want to manually call an error i can use 'raise'

def div_5(a, b):
    if b != 10:
        return a/b
    # this thing will stop the code
    raise ValueError('Custom text to describe an error')


print(div_5(50, 5))
print(div_5(50, 10))
