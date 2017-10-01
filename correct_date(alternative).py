
import datetime

day = int(input("day: "))
month = int(input("month: "))
year = int(input("year: "))

def date(year, month, day):
    try:
        datetime.date(year, month, day)
    except ValueError:
        return False
    else:
        return True



print(date(year, month, day))

