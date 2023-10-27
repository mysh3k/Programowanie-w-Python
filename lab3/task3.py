import datetime
import calendar

year: int = int(input("Podaj rok: "))


for month in range(1, 13):
    print(calendar.month_name[month])

