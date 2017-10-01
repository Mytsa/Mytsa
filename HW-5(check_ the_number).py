num = int(raw_input("input number: "))

i = 2
for i in range(2, num):
    if num % i == 0:
        print("you input NOT prime number")
    else:
        print("you input prime number")
    break
