k = int(raw_input("input day of the year: "))

day = float(k % 7)

if day == 0:
    print "is sunday"
elif day == 6:
    print "is saturday"
elif day == 5:
    print "is friday"
elif day == 4:
    print "is thursday"
elif day == 3:
    print "is wednesday"
elif day == 2:
    print "is tuesday"
else:
    print "is monday"