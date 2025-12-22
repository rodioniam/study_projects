import numpy as np

# class is some kind of template for creating objects
# like list class or dict, float, etc


class Car:  # classes should be NamedLikeThis
    # this is class methods, never forget (self)!
    def move_car(self):
        print('Car is moving')

    def stop_car(self):
        print('Car stopped')


# 'self' id basically a variable, this class will be assigned to, telling methods to operate on itself
my_car = Car()
# it is the same as
my_list = list((1, 2, 3))  # [1, 2, 3]

my_car.move_car()
my_car.stop_car()
# just like
my_list.append(5)  # [1, 2, 3, 5]


class Pow:
    def pow_num(self):
        num = np.random.randint(low=1, high=24)
        print(num**2)


number_1 = Pow()
number_2 = Pow()

number_1.pow_num()
number_2.pow_num()

# this is how i can make my own attributes


class Comment:
    # this will be mandatory argument, each new object from this class will have
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    # this way i can define logic for attribute
    def upvote(self):
        self.votes_qty += 1


first_comment = Comment('Text for a comment')

print(first_comment.text)
print(first_comment.votes_qty)

first_comment.upvote()

print(first_comment.text)
print(first_comment.votes_qty)

print(first_comment.__dict__)  # {'text': 'Text for a comment', 'votes_qty': 1}

# a little upgrade


class Comment_2:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    # i can change it so i can give a custom number and give it default value
    def upvote(self, qty=1):
        self.votes_qty += qty


second_comment = Comment_2('Text for a second comment')

print(second_comment.votes_qty)

second_comment.upvote(10)

print(second_comment.votes_qty)
