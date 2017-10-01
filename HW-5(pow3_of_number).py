num = raw_input("input number: ")

n = 0
res1 = 0
rg = int(len(num))

while n < rg:
    res = int(num[n])
    res1 = res1 + (res**3)
    n += 1
print "sum cubes of number {} is: {}".format(num, res1)
