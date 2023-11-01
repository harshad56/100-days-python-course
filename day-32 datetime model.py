import datetime as dt

now = dt.datetime.now()

year = now.year
month = now.month

day_of_weak = now.weekday()
print(day_of_weak)

date_of_birth = dt.datetime(year=2003, month=7, day=7, hour=4)
print(date_of_birth)
