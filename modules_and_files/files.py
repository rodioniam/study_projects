
# giving a number for each line in file
from itertools import cycle  # so i can cycle


def add_line_numbers():
    # opening and reading a file
    with open('modules_and_files/test_files/test_1.txt', 'r') as old_file:
        lines = old_file.readlines()                         # list of strings

    # creating new file to write in it
    with open('modules_and_files/test_files/test_3.txt', 'w') as new_file:
        # enumerate so i can have tuple with two values - number and line
        for index, line in enumerate(lines):
            new_file.write(f"{index + 1}: {line}")


a = add_line_numbers()


# combining two files with differnt amount of lines, with repeating values
def open_files():
    result = []

    with open('modules_and_files/test_files/test_1.txt', 'r') as file_1:
        rf1 = file_1.read()
        a = rf1.replace('\n', ' ')
        seasons = a.split(', ')  # making a list from lines
    with open('modules_and_files/test_files/test_2.txt', 'r') as file_2:
        rf2 = file_2.read()
        years = rf2.split(', ')
        years_cycler = cycle(years)  # using cycle with this file

    for season in seasons:  # i cycle lines in smaller file so lines from it repeats
        result.append(f"{season} - {next(years_cycler)}")
    return result


result = open_files()
my_result = '\n'.join(result)

file_4 = open('modules_and_files/test_files/test_4.txt',
              'w')  # creating a new file with result
s = file_4.write(my_result)
