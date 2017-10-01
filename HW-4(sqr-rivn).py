import math

a = float(raw_input("input a: "))
b = float(raw_input("input b: "))
c = float(raw_input("input c: "))

d = b**2 - (4 * a * c)

if d > 0:
  x1 = -b + math.sqrt(d) / (2 * a)
  x2 = -b - math.sqrt(d) / (2 * a)
  print x1, x2
elif d == 0:
  x = -b / (2 * a)
  print x 
else:
  print ("not exist")
