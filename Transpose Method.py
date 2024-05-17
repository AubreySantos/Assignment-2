#Transpose Method
import numpy as np

#Example 1
vector = np.array([1, 4, 7])
transposedv = vector.T
print("Original vector:\n", vector)
print("Transposed vector (as a column matrix):\n", transposedv)

#Example 2
matrix = np.array([[5, 3, 8], [9, 2, 7], [4, 8, 6]])
transposed_matrix = matrix.T
print("Original matrix:\n", matrix)
print("Transposed matrix:\n", transposed_matrix)

#Example 3
matrix = np.array([[1, 2], [4, 5]])
transposed_matrix = matrix.T
print("Original matrix:\n", matrix)
print("Transposed matrix:\n", transposed_matrix)
