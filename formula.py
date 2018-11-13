sex = input('стать: ')
height = float(input('зріст: '))

if (sex == 'ч'):
    index = (((height * 4 / 2.54) - 128) * 0.453)
elif (sex == 'ж'):
    index = (((height * 4 / 3.50) - 108) * 0.453)

print('ваша вага має бути : ' + str(index))
