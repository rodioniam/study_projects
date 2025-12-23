import numpy as np

# class is some kind of template for creating objects
# like list class or dict, float, etc


class Car:  # classes should be NamedLikeThis
    # this is class methods, never forget (self)!
    def move_car(self):
        return 'Car is moving'

    def stop_car(self):
        return 'Car stopped'


# 'self' id basically a variable, this class will be assigned to, telling methods to operate on itself
my_car = Car()
# it is the same as
my_list = list((1, 2, 3))  # [1, 2, 3]

my_car.move_car()  # Car is moving
my_car.stop_car()  # Car stopped
# just like
my_list.append(5)  # [1, 2, 3, 5]
# or
Car.move_car(my_car)  # Car is moving


class Pow:
    def pow_num(self):
        num = np.random.randint(low=1, high=24)
        return num**2


number_1 = Pow()
number_2 = Pow()

number_1.pow_num()  # gives different value everytime
number_2.pow_num()  # gives different value everytime

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

first_comment.text  # Text for a comment
first_comment.votes_qty  # 0

first_comment.upvote()

first_comment.text  # Text for a comment
first_comment.votes_qty  # 1

first_comment.__dict__  # {'text': 'Text for a comment', 'votes_qty': 1}

# a little upgrade


class Comment_2:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    # i can change it so i can give a custom number and give it default value
    def upvote(self, qty=1):
        self.votes_qty += qty


second_comment = Comment_2('Text for a second comment')

second_comment.votes_qty  # 0

second_comment.upvote(10)

second_comment.votes_qty  # 10


# static methods
# a method that belongs to a class but does not access or modify the class's state or a specific instance's state
# It behaves like a regular function that is logically grouped within the class's namespace for organizational purposes


class Comment_3:
    def __init__(self, text):
        self.text = text

    @staticmethod  # this is decorator
    def merge_comments(first, second):
        return f"{first} {second}"


third_comment = Comment_3('Text for the third comment')

m1 = Comment_3.merge_comments('Hello', 'World!')  # Hello World!

# because 'merge_comments' method does not have 'self' it will not have access to the variable parameters
m2 = third_comment.merge_comments('Hello', 'Again!')  # Hello Again!
third_comment.__dict__  # {'text': 'Text for the third comment'}

# class's own attributes
# they are defind in the body of the class and shared between all objects


class Messages:
    total_messages = 0

    def __init__(self, text):
        self.text = text
        self.msg_rating = 0
        Messages.total_messages += 1


msg1 = Messages('First message')

Messages.total_messages  # 1

msg2 = Messages('Second message')

Messages.total_messages  # 2
# i can rewrite this attribute if i call it directly
Messages.total_messages = 200
Messages.total_messages  # 200

msg3 = Messages('Third message')
Messages.total_messages  # 201


# making custom magic methods for classes

class Messages_2:
    def __init__(self, text):
        self.text = text
        self.msg_rating = 0

    def give_rating(self):
        self.msg_rating += 1

    # added the ability to add
    def __add__(self, other):
        return (f"{self.text} {other.text}", self.msg_rating + other.msg_rating)

    # added comparison option
    def __eq__(self, other):
        if self.text == other.text and self.msg_rating == other.msg_rating:
            return True
        else:
            return False


ms1 = Messages_2('Hello')
ms2 = Messages_2('World!')
ms3 = Messages_2('Hello')
ms4 = Messages_2('Hello')
ms1.give_rating()
ms2.give_rating()
ms3.give_rating()
ms1.msg_rating  # 1
ms2.msg_rating  # 1

ms1 + ms2  # ('Hello World!', 2)

ms1 == ms2  # False
# because 'text' is different
ms1.__dict__, ms2.__dict__
# {'text': 'Hello', 'msg_rating': 1} {'text': 'World!', 'msg_rating': 1}

ms1 == ms3  # True
# because 'text' and 'msg_rating' are the same
ms1.__dict__, ms3.__dict__
# {'text': 'Hello', 'msg_rating': 1} {'text': 'Hello', 'msg_rating': 1}


ms1 == ms4  # False
# because 'msg_rating' is different
ms1.__dict__, ms4.__dict__
# {'text': 'Hello', 'msg_rating': 1} {'text': 'Hello', 'msg_rating': 0}
