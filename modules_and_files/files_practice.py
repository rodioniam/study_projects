from pathlib import Path

files_folder = Path('modules_and_files/files_practice_folder')

# instead of this i can use '.mkdir(exist_ok = True)' - will ignore error
if not files_folder.exists():
    files_folder.mkdir()
    print('Folder created!')
else:
    print('Could not create folder.')

file_1_path = Path(files_folder / 'file_1.txt')
file_2_path = Path(files_folder / 'file_2.txt')

with open(file_1_path, 'w') as file_one:
    file_one.write('Line one,\nLine two,\nLine three.\n')

with open(file_1_path) as file_one:
    print(file_one.read())

with open(file_2_path, 'w') as file_two:
    file_two.write('Line one,\nLine two,\nLine three.\n')

with open(file_2_path) as file_two:
    while True:
        line = file_two.readline()
        print(line)
        if not line:
            break


if file_1_path.exists() and file_2_path.exists():
    file_1_path.unlink()
    print('File deleted.')
    file_2_path.unlink()
    print('File deleted.')

if files_folder.exists():
    files_folder.rmdir()
    print('Folder deleted!')
else:
    print("Can't delete folder.")
