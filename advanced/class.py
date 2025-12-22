import numpy as np

# class is some kind of template for creating objects
# like list class or dict, float, etc


class Car:  # classes should be NamedLikeThis
    # this is class methods, never forget (self)!
    def move_car(self):
        print('Car is moving')

    def stop_car(self):
        print('Car stopped')


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
