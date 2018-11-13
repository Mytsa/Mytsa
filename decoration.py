def decorator(func):
    def wrapper(line):
        print(vvod1)
        func(line)
        print(vvod2)
    return wrapper

vvod1 = input("ведіть щось: ")  #до виконання коду
vvod = input("ведіть щось: ")   # виконання коду
vvod2 = input("ведіть щось: ")  # після виконання коду

@decorator
def show(line):
    print(line)


show(vvod)


#def show(line):
#    print (line)


# show = decorator (show)
#show("Я обычная функция")