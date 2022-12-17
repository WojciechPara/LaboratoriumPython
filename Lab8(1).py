def find(lista, szukana_wartosc):
    indeksy = []
    for i in range(len(lista)):
        if lista[i] == szukana_wartosc:
            indeksy.append(i)
    return indeksy


list = [0, 1, 1, 1, 2, 2, 2, 0, 0, 0]
wynik = find(list, 0)
print(wynik)

wynik2 = find(['A', 'B', 'C', 'D'], 'C')
print(wynik2)
