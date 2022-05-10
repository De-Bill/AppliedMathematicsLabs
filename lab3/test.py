import numpy as np
import pprint
import scipy.linalg

from lu_decomposition import lu_decomposition
from solving_linear_system import *
from matrix_inverse import *


A = np.array([[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]], dtype=np.float_)
P, L, U = lu_decomposition(np.copy(A))

print("A:")
pprint.pprint(A)

print("P:")
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)

print("A:")
pprint.pprint(A)

print("PLU:")
pprint.pprint(P @ L @ U)

print("A == PLU?:", np.allclose(A, P @ L @ U))


A = np.array([[1, 5, 5], [6, 9, 22], [32, 5., 5]])
b = np.array([1, 2, 7])
P, L, U = lu_decomposition(A)
x = plu_solve(P, L, U, b)
print("x:")
print(x)
print('Solving system is correct:', np.allclose(x, scipy.linalg.solve(A, b)))

A = np.array([[2, -1, 0],[-1, 2, -1.], [0, -1, 2.]])
P, L, U = lu_decomposition(A)
inv = lu_inverse(P, L, U)
print(inv)
print('Inverse matrix is correct:', np.allclose(inv, np.linalg.inv(A)))