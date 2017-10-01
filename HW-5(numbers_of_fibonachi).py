num = int(raw_input("input numbers: "))

a = 0
b = 1

for i in range(2, num + 1):
    c = a + b
    a, b = b, c
    print c


