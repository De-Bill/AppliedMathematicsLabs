import numpy as np
import pprint

import scipy
from scipy import linalg

from lab3.compressed_sparse_column import csc
from lu_decomposition import lu_decomposition
from solving_linear_system import *
from matrix_inverse import *
from seidal_gauss import *
from l3_t4_testing import *


# Decomposition check
A = np.array([[7, 0, 0, 2], [3, 8, 0, 0], [0, 0, 4, 0], [0, 0, 0, 6]], dtype=np.float_)
data, col_ind, indptr = csc(A)
L, U = lu_decomposition(csc_array((data, col_ind, indptr), shape=(4, 4)))

print("A:")
pprint.pprint(A)

print("L:")
pprint.pprint(L.toarray())

print("U:")
pprint.pprint(U.toarray())

print("First decomposition is correct: ", np.allclose(A, L.toarray() @ U.toarray()))

# Solving linear system check
A = np.array([[1, 5, 5], [6, 9, 22], [32, 5, 5]])
b = np.array([1, 2, 7])
data, col_ind, indptr = csc(A)
L, U = lu_decomposition(csc_array((data, col_ind, indptr), shape=(3, 3)))
print("Second decomposition is correct: ", np.allclose(A, L.toarray() @ U.toarray()))
x = lu_solve(L, U, b)
print("x:")
print(x)
x_correct = scipy.linalg.solve(A, b)
print("x_correct:")
print(x_correct)
print('Solving system is correct:', np.allclose(x, x_correct))

# Matrix inverse check
A = np.array([[2, -1, 0], [-1, 2, -1.], [0, -1, 2.]])
data, col_ind, indptr = csc(A)
L, U = lu_decomposition(csc_array((data, col_ind, indptr), shape=(3, 3)))
inv = lu_inverse(L, U)
print(inv.toarray())
print('Inverse matrix is correct:', np.allclose(inv.toarray(), np.linalg.inv(A)))

matrixA = np.array([[7, 3, -1, 2],
   [3, 8, 1, -4],
   [-1, 1, 4, -1],
   [2, -4, -1, 6]], dtype='float64')

y = np.array([5, 6, 7, 8], dtype='float64')

print("Zeidel method")
foo(matrixA, y) # Zeidel method

print("t4")
y =[10, 20, 30, 40]
print(gen_diagonal_saturated_matrix(4, 20))
print("--------------------------------------------")
foo(gen_diagonal_saturated_matrix(4, 20), y)



