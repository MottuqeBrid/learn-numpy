# Matrix in NumPy
import numpy as np

var = np.matrix([[1, 2, 3], [4, 34, 6], [7, 11, 9]])
var2 = np.matrix([[1, 20, 3], [34, 34, 6], [70, 11, 9]])
print(var)
print(type(var))
print(var * 2)
print(var + var)
print(var * var2)
print(var.T)
print(var.I)
print(var.T * var)
print(var.I * var)
print(var.dot(var2))  # Convert to ndarray
print(np.matrix.diagonal(var))
print("Swapaxes:\n", np.swapaxes(var, 1, 0))
print("power:\n", np.linalg.matrix_power(var, 6))
print("determinant:\n", np.linalg.det(var))
print("eigenvalues and eigenvectors:\n", np.linalg.eig(var))
