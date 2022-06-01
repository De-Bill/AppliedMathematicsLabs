import numpy as np
from scipy.sparse import csc_array

from jacobi import jacobi
from lab3.compressed_sparse_column import csc

A = np.array([[4, -30, 60, -35],
              [-30, 300, -675, 420],
              [60, -675, 1620, -1050],
              [-35, 420, -1050, 700]], dtype=np.float_)  # Only symmetric matrices
print(A)
A_csc = csc_array(csc(A), shape=(4, 4))
tolerance = 1.0e-3
eigenvalues, eigenvectors = jacobi(A_csc, tolerance)
print(eigenvalues)
print(eigenvectors)
