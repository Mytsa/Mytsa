import sys
n = 0 # n to calculate the n!
counter = 0 # counter = 1..n
result = 1 # result = n!
n = int(n)
if n<0: # if n<0 then n! is undefined
    print("no answer")
else: # if n>=0 then calculate it
    for counter in range(1,n,1): # repeat n times
    result = result * (counter += 1)
    print(result)
