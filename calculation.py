# main file. Run this file
import cs1   # trigonometry file
import hf    # work with history file
#import input-calc    # work with history file

first = float(input('first number: '))   # first number must be float for cos, sin, !, sq
a = input('action: ')  # action

# if first == "pi":                        # need desigion about type of first number, or constant like 'e' or 'pi'
#     first = cs1.pi(first)
# if first == "e":
#     first = cs1.e1(first)
if first == "pi":
    first = cs1.pi(first)
if first == "e":
    first = cs1.e1(first)
if a is '':
    res = first                 # working with press enter. Not with button "space"
if a == "cos":
    res = cs1.cos(first, a)
if a == "sin":
    res = cs1.sin(first, a)
if a == "!":
    res = cs1.fact(first, a)
if a == "sq":
    res = cs1.sqrt(first, a)
if a == "e":
    res = cs1.e(first, a)

if a == "+":
    s = int(input('second number: '))  # second number
    res = first + s
if a == "-":
    s = int(input('second number: '))  # second number
    res = first - s
if a == "*":
    s = int(input('second number: '))  # second number
    res = first * s
if a == "^":
    s = int(input('second number: '))  # second number
    res = first ** s
if a == "/":
    s = int(input('second number: '))  # second number
    res = first / s

print("answer is: ", res)

hf.wrt(res)   # write data to file
hf.rd()       # read data from file if you pres 'y' in question



# old version without input outside file

# if a == "cos":
#     math.cos(first)
#     p = input("convert rad in degrees - y or n: ")
#     if p == "y":
#         res = (math.degrees(first), "deg")
#
# if a == "sin":
#     math.sin(first)
#     p = input("convert rad in degrees - y or n: ")
#     if p == "y":
#         res = (math.degrees(first), "deg")
#
# if a == "!":
#     if first >= 0:
#         res = (math.factorial(first))
#     elif first <= 0:
#         print("factorial must be a positive")


# k = open('history.txt', 'a')
# k.write(str(res))
# k.close()
#
# hist = input("show calculation history - y or n: ")
# if hist == "y":
#     k = open('history.txt')
#     print("data in file is: ", k.read())
#     k.close()
