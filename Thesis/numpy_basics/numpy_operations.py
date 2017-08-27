import numpy as np


matrix_a = np.array([[1, 3, 5], [4, 5, 6], [-1, 0, 9]])
matrix_b = np.array([1, 5, 6]).T

matrix_C = np.matmul(np.matmul(matrix_a, matrix_a), matrix_b)
matrix_D = np.matmul(np.linalg.matrix_power(matrix_a, 2), matrix_b)
print matrix_C
print matrix_D


