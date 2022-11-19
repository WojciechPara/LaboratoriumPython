import random

zestaw_1 = []

n = int(input("Ile elementów listy 1 utworzyć?: "))

for i in range(n):
    zestaw_1.append(random.randint(1, 10))

print(f"Zestaw1 - {zestaw_1}")

zestaw_2 = [random.randint(5, 15) for i in range(n)]
print(f"Zestaw2 - {zestaw_2}")

liczba = int(input("Podaj liczbę: "))

if liczba in zestaw_1 and liczba in zestaw_2:
    print("Liczba z zestawu 1 i 2")
elif liczba in zestaw_1:
    print("Liczba z zestawu 1")
elif liczba in zestaw_2:
    print("Liczba z zestawu 2")
else:
    print("Nie ma takiej liczby w obu zestawach")

zestaw_1_2 = zestaw_1 + zestaw_2

print(f"Zestaw 1 + 2 przed sortowaniem - {zestaw_1_2}")

zestaw_1_2.sort()

print(f"Zestaw 1 + 2 po sortowaniu - {zestaw_1_2}")