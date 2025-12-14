# Search
import numpy as np

var1 = np.array([1, 2, 3, 4, 5])

x = np.where((var1 % 2) == 0)
print(x)

# Sort
var2 = np.array([3, 2, 4, 1, 5])
x = np.searchsorted(var2, 6, side="right")
print(x)
