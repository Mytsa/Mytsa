import math as m
x = float(raw_input("input x: "))
y = float(raw_input("input y: "))
z = float(raw_input("input z: "))


a1 = float(2*m.cos(x - (m.pi/6)))
a2 = float(m.pow(m.sin(y),2))

a = a1 / ((1 / 2) + a2)
print ("a answer is: " + str(a))


b1 = float(m.pow(z,2))

b = 1 + ((b1 / (3 + (b1 / 5))))
print ("b answer is: " + str(b))
