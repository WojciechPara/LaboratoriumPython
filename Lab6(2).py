def oblicz(liczba1, liczba2):
    suma = liczba1 + liczba2
    roznica = liczba1 - liczba2
    return suma, roznica


l1 = int(input("Podaj 1 liczbę: "))
l2 = int(input("Podaj 2 liczbę: "))

x, y = oblicz(l1, l2)
print(x, type(x))
print(y, type(y))
