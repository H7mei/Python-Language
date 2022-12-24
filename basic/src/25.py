# NumPy
import numpy as np

list_height = [1.73, 1.69, 1.78, 1.75, 1.78, 1.67, 1.89]
list_width = [1.65, 1.87, 1.79, 1.86, 1.60, 1.60, 1.70]

bmi = np.array(list_height) / np.array(list_width) ** 2
print(bmi)

# numPy: remarks
# 1. Numpy arrays: contains only one type of data.

python_list = [1, 2, 3, 4, 5]
numpy_array = np.array([1, 2, 3, 4, 5])

# its will concatenate
print(python_list + python_list)

# but if
print(numpy_array + numpy_array)

# Numpy Subsetting
print(bmi[0:2])  # indexing 0 to 2
print(bmi > 3)  # boolean

# 2 dimensional array (matrix)
np_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(np_2d[0, 1])  # indexing 0 to 1
print(np_2d[1, :])  # indexing 1 to all
print(np_2d[:, 1])  # indexing all to 1
