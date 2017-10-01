i = None
N = None
result = None


def mess(msg):
    try:
        return raw_input(msg)
    except NameError:
        return input(msg)

N = float(mess('need N: '))
if N < 0:
    print('n must be positive')
else:
        i = 0
        result = 1
        for count in range(int(N)):
            i += 1
            result *= i
            print(result)
