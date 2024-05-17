#Dot Method 
#Example 1

import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
dot_product = np.dot(vector1, vector2)
print("The dot product of vectors:", dot_product)  

#Example 2
matrix = np.array([[1, 2], [3, 4]])
vector = np.array([5, 6])
dot_product = np.dot(matrix, vector)
print("Dot product of matrix and vector:", dot_product)  

#Example 3
matrix = np.array([[1, 2, 2], [3, 4, 4], [5, 2, 6]])
matrix2 = np.array([[5, 6], [3, 4], [5, 1]])
dot_product = np.dot(matrix, matrix2)
print("Dot product of matrix:", dot_product) 

