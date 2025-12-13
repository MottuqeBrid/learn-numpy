# ArathmaticOperation in numpy
import numpy as np

var = np.array([10, 20, 30, 40])
print("Original array:", var)

# Arathmatic operations
print("Minimum value:", np.min(var))
print("Maximum value:", np.max(var))
print("Index of minimum value:", np.argmin(var))
print("Index of maximum value:", np.argmax(var))

var2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Second array:\n", var2)
print("Minimum value:", np.min(var2, axis=0))  # Minimum along columns
print("Maximum value:", np.max(var2, axis=1))  # Maximum along rows
print(np.sqrt(var))  # Square root of each element
print(np.std(var))  # Standard deviation of the array
print(np.sum(var))  # Sum of all elements
print(np.cumsum(var))  # Cumulative sum of elements

print("------------------\n")

# Trigonometric functions
angle = np.array([0, 30, 45, 60, 90])
print(np.sin(angle * np.pi / 180))  # Sine of angles in radians
print(np.cos(angle * np.pi / 180))  # Cosine of angles in radians
print(np.tan(angle * np.pi / 180))  # Tangent of angles in radians
