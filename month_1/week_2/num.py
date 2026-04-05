import numpy as np

# ar = np.array([1,2,3])
# ar = np.arange(1,12,2)
# ar = np.zeros((12,10), dtype=int)
# ar = np.ones((12,10), dtype=int)
# ar = np.zeros((5, 5), dtype=int)
# ar[0:2, 0:2] = 1
# ar[(ar.shape[0])//2, (ar.shape[1])//2] = 1
# ar[3:, 3:] = 1
# ar[4, 4//2] = 1

# ar[0::2, 0::2]=1
# ar[1::2, 1::2]=1


# ar = np.array([10, 5, 20, 3, 15])
# mask = ar >=20
# print(mask)

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(a + b)
# print(a * b)
# print(a ** 2)


# matrix = np.ones((3, 3))
# row = np.array([1, 2, 3])
# result = matrix + row
# print(result)

# ar = np.arange(12)
# ar = ar.reshape(2,6)
# auto_matrix = ar.reshape(3,-1)
# print(auto_matrix.transpose())

# ar = np.arange(12)

# copy_ar = ar.ravel()
# copy_ar = copy_ar **2
# print(copy_ar, ar)


# A = np.array([[1, 2], 
#               [3, 4]])
# B = np.array([[5, 6], 
#               [7, 8]])

# result = np.dot(A, B)

# det = np.linalg.det(A)
# inv = np.linalg.inv(A)
# print(inv)
# print(result)


# data = np.loadtxt('test_x.csv', delimiter=",")
# ex = np.sin(data)
# np.savetxt('result_sin.csv', ex, delimiter=',', fmt="%.5f")
# print(ex)


import numpy as np

# 1. Five random numbers between 0 and 1
# uniform_data = np.random.rand(1)
# # 2. A 3x3 matrix of "Normal" numbers (Bell curve)
# # Most numbers will be near 0; few will be above 2 or below -2
# normal_data = np.random.randn(1000)

# # 3. Simulating a dice roll (10 rolls)
# dice_rolls = np.random.randint(1, 7, size=10)
# print(normal_data)

np.random.seed(42)
print(np.random.rand(3))

np.random.seed(42)
print(np.random.rand(3))