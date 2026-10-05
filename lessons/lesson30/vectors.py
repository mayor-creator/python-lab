import numpy as np

# vectors of an array values
v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])

# print(v1 + v2)
# print(v1 * v2)

# python list
list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]
# print(list1 + list2)
# this will produce an error message
# print(list1 * list2)

# broadcasting
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# scalar operates on an element
# print(array_2d + 10)
# print(array_2d * 5)

# matrix multiplication
a1 = np.array([[1, 3], [0, 1], [6, 2], [9, 7]])
b1 = np.array([[4, 1, 3], [5, 8, 5]])

c = np.matmul(a1, b1)
print(c)
