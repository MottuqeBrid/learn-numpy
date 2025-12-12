import numpy as np
import time

list1 = [1, 2, 3, 4, 5]
array1 = np.array(list1)
print(array1)
print(type(array1))
print(list1)
print(type(array1.shape))


start = time.time()
[j**4 for j in range(1, 9)]
end = time.time()

print("Time:", end - start)

start1 = time.time()
np.arange(1, 9) ** 4
end1 = time.time()

print("Time:", end1 - start1)
