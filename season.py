# Написать функцию season,
# принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, ]
# которому этот месяц принадлежит (зима, весна, лето или осень).

m = float(input('введіть номер місяця: '))

def season(m):
    dict = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
    return print(dict.get(m))
season(m)
