# Iterating through NumPy arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
arr1 = np.array([[1, 2], [11, 4], [5, 6]])

for x in arr:
    print(x)

for x in arr1:
    print(x)
    for y in x:
        print(y)

print("-----")

for x in np.nditer(arr1):
    print(x)
for x in np.nditer(arr1, flags=["buffered"], op_dtypes=["S"]):
    print(x)

print("-----")
for x, d in np.ndenumerate(arr1):
    print(x, d)
