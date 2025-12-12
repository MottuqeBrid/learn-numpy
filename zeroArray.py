# Zero Array
import numpy as np

zero_ar = np.zeros(4)
print("Zero Array:", zero_ar)
print("Number of dimensions:", zero_ar.ndim)

zero_ar1 = np.zeros((3, 3))
print(zero_ar1)
print("Number of dimensions:", zero_ar1.ndim)

ar_one = np.ones(4)
print(ar_one)
print("Number of dimensions:", ar_one.ndim)
ar_one1 = np.ones((2, 4))
print(ar_one1)

# emtpy array
empty_ar = np.empty(3)
print(empty_ar)

empty_ar1 = np.empty((2, 3))
print(empty_ar1)
print("--------------")

# arange

ar_rn = np.arange(4)
print(ar_rn)
print("---------------------")
# Digonal Array
dig_ar = np.eye(3)
print(dig_ar)

dig_ar1 = np.eye(3, 5)
print(dig_ar1)
print("--------------")

# identity matrix
id_mat = np.identity(4)
print(id_mat)
id_mat1 = np.identity(3)
print(id_mat1)
print("--------------")

# linspace
ls_ar = np.linspace(0, 10, num=5)
print(ls_ar)
