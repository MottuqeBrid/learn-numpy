# numpy indexing and slicing
import numpy as np

data = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
var = np.array([1, 2, 3, 4])

print(var[-3])
print(var[3])
print(var[1:3])
print("-----")
print(data[1, 2])
print(data[0:2, 1:3])
print("-----")
print(data[:, 1])
