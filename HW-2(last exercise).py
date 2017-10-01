# a = ln|(y - sqrt(|x|)(x - (y / (z + (x^2 / 4))))|
# b = x - (x^2 / 3!) + (x^5 / 5!)

import math as m
x = float(raw_input("input x: "))
y = float(raw_input("input y: "))
z = float(raw_input("input z: "))

a = m.log1p(m.fabs((y - (m.sqrt(m.fabs(x)))) * (x - (y / (z + (m.pow(x,2) / 4))))))

print ("a answer is: " + str(a))

b = (x - (m.pow(x,2) / m.factorial(3)) + (pow(x,5) / m.factorial(5)))

print ("b answer is: " + str(b))
