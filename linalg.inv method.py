#linalg.inv Method
import numpy as np

#Example 1
matrix = np.array([[5, 4], [1, 2]])
inverse = np.linalg.inv(matrix)
print("Original matrix:\n", matrix)
print("Inverse of the matrix:\n", inverse)

#Example 2
matrix = np.array([[5, 4, 1], [1, 2, 4], [3, 6, 2]])
inverse = np.linalg.inv(matrix)
print("Original matrix:\n", matrix)
print("Inverse of the matrix:\n", inverse)


#Example 3
singular_matrix = np.array([[3, 8, 1], [-4, 1, 1], [-4, 1 ,1]])

try:
  inverse = np.linalg.inv(singular_matrix)
  print("Singular matrix:\n", singular_matrix)
  print("Inverse:\n", inverse)
except np.linalg.LinAlgError:
  print("Singular matrix (error):\n", singular_matrix)
  print("Inverse: Not possible (singular matrix)")

