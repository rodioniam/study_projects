# the while loop will exist as long as the conditions are met

i = 0  # here i implemented count so i have condition to stop while

while i < 15:
    print(i)
    i += 1
else:
    print(f'Number is {i}')


# func and loop for deleting element from list
a = [1, 2, 3, 4, 5]


def list_clear():
    a.pop(0)
    return (a)


while a:
    list_clear()
    print('List is full', a)
else:
    print('List is empty')


# for loop is used when i need to do something with every item in collection
b = [2, 4, 6]

for el in b:
    print(el**2)


# continue, break, else operators in loops

# continue is used when i need to continue loop if some conditions are met
c = [1, 2, 3, 4, 'abc', 5, 6]
# if el in lst is not int continue the loop
for el in c:
    if not isinstance(el, int):  # isinstance() checks type of the obj
        continue
    print(el**2)

# break is used to stop loop if some conditions are met
d = [1, 2, 3, 4, 'abc', 5, 6]

for el in d:
    if not isinstance(el, int):
        break
    print(el**2)

# else will happen if loop finished by itself
