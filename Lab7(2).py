import numpy as np

tab3d = np.random.randint(low=0, high=50, size=(5, 5))
print(tab3d)

print(f"max in rows: {tab3d.max(axis=1)}")
print(f"min in cols: {tab3d.min(axis=0)}")

print(f"max in rows: {tab3d.sum(axis=1)}")
print(f"sum in cols: {tab3d.sum(axis=0)}")