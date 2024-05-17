#Flatten Method
import numpy as np

#Example 1
matrix = np.array([[1, 2, 3], [4, 5, 6]])
flatten = matrix.flatten()
print("Original matrix:\n", matrix)
print("Flattened array (row-major order):", flatten)

#Example 2
matrix = np.array([[1, 4, 2], [4, 8, 1], [3, 5, 9]])
flatten = matrix.flatten()
print("Original matrix:\n", matrix)
print("Flattened array (row-major order):", flatten)

#Example 3
matrix = np.array([[8, 4, 6], [3, 5, 2]])
flattened_column = matrix.flatten("F")
print("Original matrix:\n", matrix)
print("Flattened array (column):", flattened_column)  # Output: [1 4 2 5 3 6]
