# Пользователь делает вклад в размере a рублей
# сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%.
# Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#
# Написать функцию bank, принимающая аргументы a и years,
# и возвращающую сумму, которая будет на счету пользователя.

a = float(input('введіть суму вкладу: '))
years = float(input('термін вкладу в роках: '))

def bank(a, years):
    return a*(1+((10 * 365) / (100 * 365)))**years

print(bank(a, years))