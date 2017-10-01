# Написать функцию is_prime,
# принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.
x = int(input("введіть ціле число: "))

def is_prime(x):

    """Эту функцию можно сильно оптимизировать. Подумайте, как"""
    
    if x == 1:
        return False  # 1 - не простое число

    for possible_divisor in range(2, x):
        if x % possible_divisor == 0:
            return False
    return True

print(is_prime(x))