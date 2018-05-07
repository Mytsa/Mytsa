from itertools import combinations    # iterator


def primes(max_range):    # prime number action
    prime = [True] * max_range
    for i in range(2, max_range):
        if prime[i]:
            yield i  # prime
            for j in range(i * i, max_range, i):
                prime[j] = False


def num_revers(i):    # revers of number
    digits = str(i)
    return digits == digits[::-1]


res = [f_n for f_n in primes(10**5) if f_n > 10**4]
print(max((f_n * s_n, f_n, s_n) for f_n, s_n in combinations(res, 2) if num_revers(f_n * s_n)))
