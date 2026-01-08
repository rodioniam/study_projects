from os import path
from pathlib import Path

# command to show absolute path to current directory
print(path.abspath('.'))
print(Path('.').absolute())  # in this case i created 'Path' class object


file = Path('test_file.txt')

print([m for m in dir(file) if not m.startswith('_')])

# also shows current directory, without creating new object
print(Path.cwd())


# creating new path on Mac/Unix

a = Path('my_path').joinpath('local').joinpath('bin')
a  # my_path/local/bin
# or
a1 = Path('my_path')/'local'/'bin'
a1  # my_path/local/bin

# for windows it usually starts with disc name

# to check if file or directory exists i can use this

b = Path('modules_and_files').exists()
b  # True
b1 = Path('modules_and_files/files_2.py').exists()
b1  # True

# check if it is directory or a file
Path('modules_and_files').is_dir()  # True
Path('modules_and_files/files_2.py').is_file()  # True

list_of_files = []

# returns all files in directory
for file in Path('.').iterdir():
    list_of_files.append(file)

print(list_of_files)


# this is how i can create directory
make_dir = Path('modules_and_files').joinpath('making_folder')
# make_dir.mkdir() if it already exists it will give an error, so better to do it with if statement
if not make_dir.exists():
    make_dir.mkdir()
    print('Directory created!')
else:
    print('Directory with that name already exists.')


# same with deleting directory
if make_dir.exists():
    make_dir.rmdir()
    print('Directory deleted!')
else:
    print('Directory does not exist.')


# open and reading files
with open('modules_and_files/test_file.txt') as test_file:
    # reads as string
    read_file = test_file.read()

print(read_file)

with open('modules_and_files/test_file.txt') as test_file:
    # reads as each row as element in list
    read_lines = test_file.readlines()

print(read_lines)

# to write in a file i need to do this
# it will overwrite everthing in the file!

with open('modules_and_files/test_file.txt', 'w') as write_file:
    write_file.write('Added new line\n')

# if i dont want to overwrite file i can do this

with open('modules_and_files/test_file.txt', 'a') as file_to_add:
    file_to_add.write('Added one more line to the file\n')

with open('modules_and_files/test_file.txt') as read:
    print(read.read())


# to delete file i can use this
try:
    Path('modules_and_files/test_file_delete.txt').unlink()
    print('File deleted!')
except Exception as e:
    print(e)

# here is how i can create new file
new_file = open('modules_and_files/creating_file.txt', 'w')
