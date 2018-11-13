# input data:
# 8
# 10 20 30 40 5 6 7 8
#
# answer:
# 126

# a = 10
# b = 20
# c = 30
# d = 40
# e = 5
# f = 6
# g = 7
# h = 8
#
# print(a+b+c+d+e+f+g+h)


l = [10, 20, 30, 40, 5, 6, 7, 8]

a = l[0] + l[1]
b = [a]

x = len(l)
i = 2
while i > x:
    sum = b[0] + l[i]
    b.insert(0, sum)
    i += 1


# sum = b[0] + l[2]
# b.insert(0, sum)
#
# sum = b[0] + l[3]
# b.insert(0, sum)

print(b)





