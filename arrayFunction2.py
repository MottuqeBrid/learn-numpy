# Array function in numpy
import numpy as np

print(
    "np.random.shuffle() function is used to shuffle the elements of an array randomly."
)
var1 = np.array([1, 2, 3, 4])
np.random.shuffle(var1)
print(var1, "\n")

print("np.unique() function is used to find the unique elements of an array.")
var2 = np.array([5, 7, 8, 5, 6, 6])
x = np.unique(var2, return_index=True, return_counts=True)
print(x)

print("\nnp.resize() function is used to resize an array to a new shape.")
var3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.resize(var3, (2, 3, 2))
print(y)

print(
    "\nnp.flatten() function is used to convert a multi-dimensional array into a one-dimensional array.\nnp.ravel() function is used to convert a multi-dimensional array into a one-dimensional array."
)
var4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(var4.flatten(order="F"))
print(var4.ravel(order="F"))
