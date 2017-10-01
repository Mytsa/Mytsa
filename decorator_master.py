def decorator(func):
    def wrapper(line):
        print ("Код до выполения функции")
        func(line)
        print ("Код, который сработал после функции")

    return wrapper


def test(func):
    def wrapper(line):
        print ("Код до выполения функции 2")
        func(line)
        print ("Код, который сработал после функции 2")

    return wrapper


@decorator
@test
def show(line):
    print (line)


# show = decorator (show)
show("Я обычная функция")