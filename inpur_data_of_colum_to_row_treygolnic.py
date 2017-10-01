# n = input()
#
# # for i in range(28):
# #     a, b, c = input().split()
#
# k = int(input())
#
# for i in range(k):
#     n, d = input().split()
#     n, d = float(n), float(d)
#     x = n/d
#     print(round(x), '')


#як пройтися по всім рядкам
# n = int(input())
# for i in range(n) :
#     a, b = input().split()
#     print(round(int(a) / int(b)), " ")

n = int(input())

for i in range(n):
    a, b, c = raw_input().split()


#ця функція працює, потрібно ввести дані і зациклити
    def trey(a, b, c):
        if (int(a) ** 2) == (((int(b) ** 2)) + ((int(c) ** 2))):
            return print('1')
        elif (int(b) ** 2) == (((int(a) ** 2)) + ((int(c) ** 2))):
            return print('1')
        elif (int(c) ** 2) == (((int(b) ** 2)) + ((int(a) ** 2))):
            return print('1')
        return print('0')

    trey(a, b, c)