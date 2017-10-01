day = int(raw_input("day: "))
month = int(raw_input("month: "))
year = int(raw_input("year: "))

if 0 < month < 13:
    if month % 2 == 0:
        if month == 2:
            if year % 4 == 0 and day < 30:
                print "date is correct"
            elif day < 29:
                print "date is correct"
            else:
                print "date is NOT correct"
        elif month == 8:
            if day < 32:
                print "date is correct"
            else:
                print "date is NOT correct"
        elif day < 31:
            print "date is correct"
        else:
            print "date is NOT correct"
    else:
        if day < 32:
            print "date is correct"
        else:
            print "date is NOT correct"
else:
    print "date is NOT correct"
print "you input: \nday is {}\nmonth is {}\nyear is {}".format(day, month, year)

