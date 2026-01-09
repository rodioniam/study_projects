from zipfile import ZipFile
from pathlib import Path

files_to_zip = Path('modules_and_files/small_modules/files_to_zip')
zip_folder = 'modules_and_files/small_modules/zip_folder.zip'


def create_directory_and_files():
    i = 0

    if not files_to_zip.exists():
        files_to_zip.mkdir()

    while i < 4:
        if not (files_to_zip / f'file_{i}.txt').exists():
            file = open((files_to_zip / f'file_{i}.txt'), 'w')
            file.close()
            i += 1
        else:
            break


create_directory_and_files()


# logic is the same as if i was creating something with 'open' command
with ZipFile(zip_folder, 'w') as f_z:
    for file in files_to_zip.iterdir():  # iterdir is for iteration for files in directory
        # 'ZipFile' class method for writing something into file
        f_z.write(file)

# extracting files from zip_folder.
# For some reason unzipping with regular computer commands give wrong result
with ZipFile(zip_folder) as f_z:
    f_z.extractall('modules_and_files/small_modules/unzipped_files')
