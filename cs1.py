# calculation trigonometric function
import math

def cos(first, a):
    if a == "cos":
        res = math.cos(first)
        p = input("convert rad in degrees - y or n: ")
        if p == "y":
           res = (math.degrees(first), "deg")
    return res

def sin(first, a):
    if a == "sin":
        res = math.sin(first)
        p = input("convert rad in degrees - y or n: ")
        if p == "y":
            res = (math.degrees(first), "deg")
    return res

def fact(first, a):
    if a == "!":
        if first >= 0:
            res = math.factorial(first)
        elif first <= 0:
            print("factorial must be a positive")
    return res

def sqrt(first, a):
    if a == "sq":
        res = math.sqrt(first)
    elif first <= 0:
        print("number under square root must be a positive")
    return res

def pi(first):
    if first == "pi":
        first = math.pi
    return first

def e1(first):
    if first == "e":
        first = math.e
    return first

def e(first, a):
    first = int(first)
    if a == "e":
        res = math.exp(first)
    return res


