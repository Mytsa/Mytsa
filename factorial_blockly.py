result = 1
i = 0
N = 0

def mess(msg):
    try:
        return input(msg)
    except NameError:
        return input(msg)

N = float(mess('need N: '))
if N < 0:
    print('N must be positive number')
else:
    for count in range(int(N)):
        i += 1
        result = result * i
        print(result)






