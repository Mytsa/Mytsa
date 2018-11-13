# Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.

import math
a = int(input('ввести значення сторони квадрату: ')) # if you work only with this file - take-off firs"#"
tup = []
def square(a):
    per = int(a * 4)
    tup.append(per)
    sq = int(a * a)
    tup.append(sq)
    d1 = int(a**2)
    d = int(d1 + d1)
    di = math.sqrt(d)
    tup.append(di)
    return print(tuple(tup))

square(a)




