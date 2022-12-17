import numpy as np
arr = np.arange(100000)
lista = list(range(100000))

import time

start_time = time.time()
for i in range(10):
    arr2 = arr * 2
print(f"--- {(time.time() - start_time)*1000} ms ---")

start_time = time.time()
for _ in range(10):
    lista = [x * 2 for x in lista]
print(f"--- {(time.time() - start_time)*1000} ms ---")

start_time = time.time()
for i in range(10):
    i = 0
    for a in arr:
        arr2[i] = a * 2
        i += 1
print(f"--- {(time.time() - start_time)*1000} ms ---")