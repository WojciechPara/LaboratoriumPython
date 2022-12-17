import numpy as np

tablica = np.zeros((3, 3))

print('1')
tablica1 = tablica.copy()
tablica1[1:, :2].fill(1)
print(tablica1)
print('2')

tablica2 = tablica.copy()
tablica2[:, 2:].fill(1)
print(tablica2)
print('3')

tablica3 = tablica.copy()
tablica3[:2, :].fill(1)
print(tablica3)
print('4')

tablica4 = tablica.copy()
tablica4[:2, 0].fill(1)
print(tablica4)
print('5')

tablica5 = tablica.copy()
tablica5[:2, 0::2].fill(1)
# tablica5[:2, (True, False, True)].fill(1)
print(tablica5)