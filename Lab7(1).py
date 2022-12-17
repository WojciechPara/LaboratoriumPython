import numpy as np
x = []
for i in range(7, -1, -1):
    x.append(2**i)

x = [2**i for i in range(7, -1, -1)]
print(x)

wagi = np.array(x)
print(wagi)

liczba_bin = np.random.randint(low=0, high=2, size=8)
print(liczba_bin)

liczba_dziesietna = wagi * liczba_bin
print(sum(liczba_dziesietna))
