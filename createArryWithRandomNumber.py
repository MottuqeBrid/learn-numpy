# Create Array with Random Numbers
import numpy as np

# Create a 1D array of 4 random numbers
var = np.random.rand(4)
print(var)
print("-----")
# Create a 2D array of shape (2, 3) with random numbers
var1 = np.random.rand(2, 3)
print(var1)
print("-----")

# randn()
var2 = np.random.randn(4)
print(var2)
print("-----")
var3 = np.random.randn(2, 3)
print(var3)
print("-----")

# ranf()
var4 = np.random.ranf(4)
print(var4)
print("-----")
var5 = np.random.ranf((2, 3))
print(var5)
print("-----")
# randint()
var6 = np.random.randint(low=10, high=50, size=4)
print(var6)
print("-----")
var7 = np.random.randint(low=10, high=50, size=(2, 3))
print(var7)
print("-----")
