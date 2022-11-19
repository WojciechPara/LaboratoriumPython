import random

punkty = [round(random.uniform(0,50),2) for i in range(15)]

print(punkty)

print(f"Najwięcej zdobytych punktów: {max(punkty)}, najmniej zdobytych punktów: {min(punkty)}")

liczba = float(input("Podaj liczbę punktów : "))

if liczba in punkty:
    print(punkty.index(liczba))
else:
    print("Liczba nie występuje w liście PUNKTY")

suma = sum(punkty)
srednia = round(suma/len(punkty),2)
print(f"Średnia punktów: {srednia}")

pkt_powyzej = []

for i in punkty:
    if i > srednia:
        pkt_powyzej.append(i)

pkt_ponizej = [i for i in punkty if i < srednia]

print(f"Ile osób uzyskało liczbę punktów powyżej średniej {srednia} : {len(pkt_powyzej)}")
print(f"Ile osób uzyskało liczbę punktów poniżej średniej {srednia} : {len(pkt_ponizej)}")
