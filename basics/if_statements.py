# with if statements i can set up specific conditions for code

a = 15

if a == 10:
    print('10')
elif a == 15:
    print('15')
elif a == 20:
    print('20')
else:
    print('Not in the range')


def if_st():
    if a == 10:
        print('10')
    elif a == 15:
        print('15')
    elif a == 20:
        print('20')
    else:
        print('Not in the range')


# i can combine conditions using and or
def text_checker(a):
    if len(a) < 10 and a.startswith('A'):
        return 'Correct string'
    elif len(a) > 10 and a.startswith('A'):
        return 'String is too long'
    else:
        return 'Incorrect string'


b = text_checker('An alphabet')

# when using and both conditions must be true
# when using or at least one of conditions must be true
