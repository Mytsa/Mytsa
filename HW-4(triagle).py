import math

a = float(raw_input("side a: "))
b = float(raw_input("side b: "))
c = float(raw_input("side c: "))

p = (a + b + c)
s = math.sqrt(p/2 * (p/2 - a) * (p/2 - b) * (p/2 - c))

if (((b + c - a) > 0) and ((a + c - b) > 0) and ((a + b - c) > 0)):
     print "perimetr is {} \nsquare is {}".format(p, s)
else:
     print "Not real triagle"

