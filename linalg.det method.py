#linalg.det Method
import numpy as np

#Example 1
matrix = np.array([[2, 1], [3, 4]])
det = np.linalg.det(matrix)
print("Matrix:\n", matrix)
print("Determinant of the matrix:", det)

#Example 2
matrix = np.array([[1, 4, 3], [3, 3, 6], [2, 1, 2]])
det = np.linalg.det(matrix)
print("Matrix:\n", matrix)
print("Determinant of the matrix:", det)

#Example 3
matrix = np.array([[1, 3, 3, 6], [2, 4, 5, 6], [5, 7, 8, 9], [2, 1, 7, 9]])
det = np.linalg.det(matrix)
print("Matrix:\n", matrix)
print("Determinant of the matrix:", det)
