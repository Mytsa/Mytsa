year = float(input('ввести рік: '))

def is_year_leap(year):
    return year % 4

ex = is_year_leap(year)%4
if ex == 0:
    print('true')
else:
    print('false')