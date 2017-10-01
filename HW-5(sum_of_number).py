num = raw_input("input numbers: ")
action = raw_input("input 'y' if you need cycle 'for': ")

n = 0
res1 = 0
i = 0
res2 = 0
rg = int(len(num))

if action == 'y':
    for n in range(rg):
        res = int(num[n])
        res1 = res1 + res

    for i in range(len(num)):
        num = int(num)
        res_num = num % 10
        num = num / 10
        i += 1
        res2 = res2 + res_num

    print "you used cycle 'for'"

else:
    while n < rg:
        res = int(num[n])
        res1 = res1 + res
        n += 1

    while i < rg:
        num = int(num)
        res_num = num % 10
        num = num / 10
        i += 1
        res2 = res2 + res_num

    print "you used cycle 'while'"

print "answer is: {}, calculation with list operations".format(res1)
print "answer is: {}, calculation with numbers operations".format(res2)