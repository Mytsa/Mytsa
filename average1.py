# Входные данные в первой строке содержат количество списков.
# Остальные строки содержат по одному списку чисел каждая.
# Числа в каждом списке целые и положительные. Конец списка отмечен значением 0 - его не нужно включать в расчеты!!!
# Ответ должен содержать средние значения для каждого из списков, округлённые до ближайшего целого (см задачу на округление), разделенные пробелами.

a = input().split()

long = int(len(a) - 1)
# sa = float(sum(a))
# def listsum(a):
#     theSum = 0
#     for i in a:
#         theSum = theSum + i
#     return theSum
#

def average(a, long):
   theSum = 0
   for i in a:
      theSum = theSum + i
   return print(theSum / long)

average


# zip(*a)
#
# def average(a, default=float('nan')):
#    return sum(a) / float(len(a)-1) if a else default
#
# print([average(n) for n in zip(*a)])

# average = 0
# sum = 0
# for n in a:
#     sum = float(sum) + float(n)
# average = round(sum / len(a))
# print(average)



# sum=0
# for element in a:
#     sum += element
# print (sum / (len(a)-1))

#
# def summa(a):
#     s = len(a)-1
#     b = sum(Decimal(i) for i in a)
#     return print(b / s)
#
# summa(a)

# def averages( a ):
#     it = iter(a) # get a iterator over the list
#     first = next(it)
#     for item in it:
#         yield (first+item)/2
#         first = item
#
# print (averages(range(1,(len(a)-1))))
# import statistics
# print(statistics.mean(a))


# 183 28 175 117 104 0
# 11724 4800 9066 2438 8638 8187 0
# 1427 35 1361 60 1926 577 0
# 29 728 687 515 325 747 572 384 452 680 59 919 71 0
# 12857 7945 7104 15294 198 15291 1377 0
# 414 630 2699 169 1783 1638 1902 1899 453 550 0
# 884 537 821 312 193 880 207 264 52 84 43 549 528 999 561 0
# 10 21 41 49 189 52 161 36 171 0
# 410 29 346 340 297 0




