vvod = raw_input("input 4 numbers: ")
l = str(vvod)

sort = sorted(l)
print "sort of numbers: {}".format(sort)

a = sort[::-1]
print "revers of sort: {}".format(a)

res = int(l[0])*int(l[1])*int(l[2])*int(l[3])
print "mnozenna: {}".format(res)
