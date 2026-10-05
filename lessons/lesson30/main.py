import matplotlib.pyplot as plt
import numpy as np

# from scipy import misc
# from PIL import Image

# create 1-dimensional array
my_array = np.array([1.1, 9.2, 8.1, 4.7])

# access element in a ndarray
my_array[2]

# check the type of array dimension
my_array.ndim

# show rows and columns
my_array.shape

# create 2-dimensional array
array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

# print(f"array_2d has {array_2d.ndim} dimensions")
# print(f"Its shape is {array_2d.shape}")
# print(f"It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns")
# print(array_2d)

# access elements in 2d array
array_2d[0, 0]

# access an entire row and all values
array_2d[1:]

# generating and manipulating ndarrays
vector_a = np.arange(10, 30)

# create an array containing the last three 3 values of vector
arr = vector_a[-3:]

# interval between two values
interval = vector_a[3:6]

# all values except the first 12
except_first_12 = vector_a[12:]

# all even values
even = vector_a[::2]

# reverse order of values
reverse = np.flip(vector_a)

# plot a line graph
x = np.linspace(0, 100, num=9)
y = np.linspace(start=-3, stop=3, num=9)

plt.plot(x, y)
plt.show()
