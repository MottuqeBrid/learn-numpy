# Learn About Shapes and Reshaping in NumPy
import numpy as np

var = np.array([[1, 2, 3], [4, 5, 6]])
print(var)
print("Shape of the array:", var.shape)

var1 = np.array([1, 2, 3, 4, 5, 6], ndmin=4)
print(var1)
print("Shape of the array with minimum 4 dimensions:", var1.shape)

# Reshaping Arrays
var2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
var2_reshaped = var2.reshape(2, 2, 3, order="F")
print(var2_reshaped)

var_3 = var2_reshaped.reshape(-1)
print(var_3)
print(var2_reshaped)
