import numpy as np

# matrix_border = np.ones((10, 10), dtype=int)
# matrix_border[1:-1 , 1:-1] = 0
# print(matrix_border)


# 2 Checker Board Pattren

# checker_boared = np.ones((8,8) , dtype=int)
# checker_boared[0::2, 1::2]=0
# checker_boared[1::2, 0::2]=0
# print(checker_boared)


# Normalize Matrix

# mat = np.random.randint(10, 100, (5,5))
# mat_min = np.min(mat)
# mat_max = np.min(mat)

# mat_normalize = (mat- mat_min)/(mat+mat_max)
# print(mat)
# print(mat_normalize)


# A = np.array([
#     [3, 4],
#     [1, 2],
#     [5, 12]
# ])

# row_rooms = np.linalg.norm(A, axis=1, keepdims=True)
# A_normalized = A/row_rooms
# print(A_normalized)


# arr = np.random.randint(10,100, (10,10))
# max_indices = np.argmax(arr, axis=1)
# arr[np.arange(arr.shape[0]), max_indices] = -1
# print(arr)


# arr = np.random.randint(1,100,(10,10))
# arr[arr %2 ==0] = -1
# arr[arr >50] = 999
# print(arr)


# arr = np.random.randint(1,100,(100,50))
# row_sum = np.sum(arr, axis=0)
# print(row_sum.shape)


# unique = np.unique_counts(arr)
# print(unique)


A = np.array([
    [1,2],
    [3,4],
    [1,2],
    [5,6],
    [3,4]
])

remove_duplicate = np.unique(A, axis=0)
print(remove_duplicate)