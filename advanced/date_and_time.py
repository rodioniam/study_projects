# to work with date and time i need to import datetime module
# it has three main classes:
# date - stores only date (year, month, day)
# time - stores only time (hours, minutes, seconds, mseconds)
# datetime - stores both time and date

from datetime import datetime, timedelta
from datetime import date

# DATE
day = date(2025, 3, 28)
day.year  # get year from date
day.month  # month
day.day  # day
d = day.weekday()  # what day of the week was that date, 0 - Monday, 6 - Sunday
date.today()  # get todays date
date.today().day  # get todays date day
g = day.strftime('%d/%m/%Y')  # set format for date
print(g)  # 28/03/2025


# DATETIME
dt = datetime(2025, 10, 10, 16, 30, 00)
print(dt)


# set format for date
dd = dt.strftime('%d/%m/%Y, %H:%M:%S')
print(dd)


# getting datetime object from string. Second argument is for format of the date in string
s = '2025-10-10 16:30:00'
gg = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
print(gg)
h = gg.date()  # this way i can get only date without time

# timestamp is time in seconds since 1 of January 1970
a = datetime.today()  # todays date
f = datetime.timestamp(a)  # date to timestamp
k = datetime.fromtimestamp(f)  # timestamp to date
print(f)
print(k)


# with timedelta i can - and + with dates

aa = datetime.now()
bb = datetime(2025, 10, 9)
cc = aa - bb  # difference between dates
print(cc)


# what date it will be after 30 days
ddd = aa + timedelta(days=30)
print(ddd)
