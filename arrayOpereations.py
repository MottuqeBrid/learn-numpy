# Array Arathmetic Operations
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Array a:", a)
print("Array b:", b)
print(a + 3)
print(b - 2)
print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Exponentiation:", a**2)
print("Modulus:", b % a)

print("Reciprocal of a:", np.reciprocal(a))

print("----------------------\n")

# 2D Array Operations
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[7, 8, 9], [10, 11, 12]])
print("Array c:\n", c)
print("Array d:\n", d)
print("Addition:\n", c + d)
print("Subtraction:\n", d - c)
print("Multiplication:\n", c * d)
print("Division:\n", d / c)
print("Exponentiation:\n", c**2)
print("Modulus:\n", d % c)
print("Reciprocal of c:\n", np.reciprocal(c))

print("----------------------\n")
