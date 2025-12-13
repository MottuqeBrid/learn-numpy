# Join And Split Example
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# Joining arrays
joined = np.concatenate((a, b))
print("Joined array:", joined)

a1 = np.array([[1, 2, 3], [4, 5, 6]])
b1 = np.array([[7, 8, 9], [10, 11, 12]])
joimed1 = np.concatenate((a1, b1), axis=1)
print("Joined array along axis 1:\n", joimed1)

joimed2 = np.concatenate((a1, b1), axis=0)
print("Joined array along axis 0:\n", joimed2)

ar = np.stack((a, b))
print("Stacked array:\n", ar)

# Splitting arrays
a2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
split_arrays = np.array_split(a2, 3)
print("Split arrays:", split_arrays)
for i, arr in enumerate(split_arrays):
    print(f"Array {i}:", arr)
