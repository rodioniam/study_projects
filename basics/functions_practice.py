# display a greeing with user input name

def greeting():
    user_input = input('Please enter your name: ')
    print(f"Hello, {user_input}")


# ask user lenght and width of the room and calculate its size

def room_size():
    length = float(input('Enter length: '))
    width = float(input('Enter width: '))
    size = length * width
    print(f'Size of the room is {size} meters')
