# Insert and delete elements in numpy arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original array:\n", arr, "\n")
# Inserting elements
arr_inserted = np.insert(arr, (2, 4), 4.56)
print("Array after insertion:\n", arr_inserted, "\n")

# 2D array insertion
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", arr2, "\n")
arr2_inserted = np.insert(arr2, 1, [999, 88, 8], axis=0)
print("Array after insertion:\n", arr2_inserted, "\n")

# appending elements
arr_appended = np.append(arr, [6, 7, 8])
print("Array after appending:\n", arr_appended, "\n")

# 2D array appending
arr2_appended = np.append(arr2, [[7, 8, 9]], axis=0)
print("2D Array after appending:\n", arr2_appended, "\n")

# Deleting elements
arr3 = np.array([1, 2, 3, 4, 5])
print("Original array:\n", arr3, "\n")
arr3_deleted = np.delete(arr3, 2)
print("Array after deletion:\n", arr3_deleted, "\n")

# 2D array deletion
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", arr4, "\n")
arr4_deleted = np.delete(arr4, 0, axis=0)
print("Array after deletion:\n", arr4_deleted, "\n")
