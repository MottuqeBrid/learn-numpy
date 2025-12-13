# copy vs view example in NumPy
import numpy as np

a = np.array([1, 2, 3])
co = a.copy()

print("Original array a:", a)
print("Copy of a (co):", co)

vi = a.view()
print("View of a (vi):", vi)

a[0] = 10
print("Original array a:", a)
print("Copy of a (co):", co)
print("View of a (vi):", vi)
