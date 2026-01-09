import csv
from pathlib import Path

path = Path('modules_and_files/small_modules/csv_mod')

with open((path / 'test.csv'), 'w') as csv_file:
    # with this command i can write something to the csv file i created
    # i can change delimiter, but will change how csv reads files (default - ',')
    writer = csv.writer(csv_file, delimiter=';')
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([24, 'User44', 3])
    writer.writerow([100, 'User2', 56])
    writer.writerow([1, 'User909', 124])


with open((path/'test.csv')) as csv_file:
    # this is how to read csv file
    # if i used custom delimiter i need to mention it here too
    reader = csv.reader(csv_file, delimiter=';')
    # each line will be presented as list of strings
    # i can iterate on reader object only once!

    # for line in reader:
    #    print(line)
    list_csv = list(reader)
    print(list_csv)  # will give list of lists
