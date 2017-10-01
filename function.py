def func(t, v):
    s = t * v
    return s
print("km/h")
v = input("v: ")
v = float(v)

print("hour(s)")
t = input("t: ")
t = float(t)
#print("ви подалаєте шлях у ", func(v, t), "km")

print("you will go",(lambda v, t: func(t, v))(v, t), "km")

#add = lambda x, y: x * y
#print (add (2, 5))1.6

#print (add ('q', 5))

#print ((lambda x, y: x * y)(2, 6))

#fun = lambda *args: args
#print (fun (2, 56, 78.56))