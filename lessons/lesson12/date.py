import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)
month = now.month
print(month)
day_of_week = now.weekday()
print(day_of_week)

# create date tim object
date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)
