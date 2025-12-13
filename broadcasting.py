# Broadcasting in NumPy
import numpy as np

var1 = np.array([1, 2, 3])
var2 = np.array([[4], [5], [6]])
print(var1 + var2)
print((var1 + var2).shape)

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([10, 20, 30])
print(x + y)
print((x + y).shape)
