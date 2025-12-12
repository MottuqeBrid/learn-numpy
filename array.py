import numpy as np


# Creating a 1D NumPy array
x = [1, 2, 3]
y = np.array(x)
print(y)
print(y.ndim)

# Creating a 2D NumPy array
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print(a.ndim)
print(a.mean())

# Creating a 3D NumPy array
b = np.array(
    [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ]
)
print(b)
print(b.ndim)
print(b.mean())

# Creating an array with a minimum number of dimensions
arn = np.array([1, 2, 3, 4, 5], ndmin=10)
print(arn)
print(arn.ndim)


# l = []
# for i in range(1, 5):
#     k = int(int(input("Enter a number: ")))
#     l.append(k)
# arr = np.array(l)
# print("Array:", arr)

# print("Mean of the array:", arr.mean())
