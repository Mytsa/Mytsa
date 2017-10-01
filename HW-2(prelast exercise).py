# a = ((1 + sin^2(x + y)) / (2 + (|(x - 2x) / (1 + x^2y^2)|))) + x
# b = cos^2(arctg(1 / z))


import math as m
x = float(raw_input("input x: "))
y = float(raw_input("input y: "))
z = float(raw_input("input z: "))

a = ((1 + m.pow(m.sin(x + y),2)) / (2 + (m.fabs(x - 2*x) / (1+ m.pow(x,2)*m.pow(y,2))))) + x

print ("a answer is: " + str(a))

b = m.pow(m.cos(m.atan(1 / z)),2)

print ("b answer is: " + str(b))
