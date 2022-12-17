def sum_of_values(slownik):
    suma_wartosci = 0
    for wartosc in slownik.values():
        suma_wartosci += wartosc
    return suma_wartosci


dict1 = {'data1': 10, 'data2': -4, 'data3': 2}
x = sum_of_values(dict1)
print(x)

dict2 = {1: 1, 2: 4, 3: 9}
y = sum_of_values(dict2)
print(y)