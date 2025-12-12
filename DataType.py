# data type in numpy Array
import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
print("Data type:", array1.dtype)

array2 = np.array([1.5, 2.5, 3.5])
print("Data type:", array2.dtype)
array3 = np.array(["apple", "banana", "cherry"])
print("Data type:", array3.dtype)

array4 = np.array([True, False, True])
print("Data type:", array4.dtype)
array5 = np.array([1 + 2j, 3 + 4j])
print("Data type:", array5.dtype)

array9 = np.array([1, 2, 3, "A", "B", "C"])
print("Data type:", array9.dtype)

array6 = np.array([1, 2, 3], dtype=np.int8)
print("Data type:", array6.dtype)

array7 = np.array([1.5, 2.5, 3.5], dtype=np.float32)
print("Data type:", array7.dtype)
array8 = np.array(["apple", "banana", "cherry"], dtype=np.str_)
print("Data type:", array8.dtype)


x = np.array([1, 2, 3, 4], dtype=np.int16)
print("Data type before:", x.dtype)
x1 = np.float32(x)
print("Data type after:", x1.dtype)
