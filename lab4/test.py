import time

import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg
from scipy.sparse import csc_array

from jacobi import jacobi
from lab3.compressed_sparse_column import csc
from lab3.hilbert import getHilbertMatrix
from dsm import gen_dsm

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

#test diagonal matrices
print("##############")
A = gen_dsm(4, 10)
print(f"A:\n{A}")
A_csc = csc_array(csc(A), shape=(4, 4))
tolerance = 1.0e-3
eigenvalues, eigenvectors = jacobi(A_csc, tolerance)

C = scipy.linalg.eig(A)
print(f"scipy values:\n{C[0]}")
print(f"scipy vectors:\n{C[1]}")
print(f"eigenvalues:\n{eigenvalues}")
print(f'eigenvectors:\n{eigenvectors}')


#test diagonal matrices
print("##############")
A = getHilbertMatrix(4)
print(f"A:\n{A}")
A_csc = csc_array(csc(A), shape=(4, 4))
tolerance = 1.0e-3
eigenvalues, eigenvectors = jacobi(A_csc, tolerance)

C = scipy.linalg.eig(A)
print(f"scipy values:\n{C[0]}")
print(f"scipy vectors:\n{C[1]}")
print(f"eigenvalues:\n{eigenvalues}")
print(f'eigenvectors:\n{eigenvectors}')



#test dsm
lengths = np.linspace(3, 30, 28)

items = {}
times = []
for i in lengths:
    start = time.time()
    print(f"{int(i)}/{int(lengths[len(lengths) - 1])}")
    A = gen_dsm(int(i), 10)
    A_csc = csc_array(csc(A), shape=(int(i), int(i)))
    tolerance = 1.0e-3
    eigenvalues, eigenvectors = jacobi(A_csc, tolerance)
    times.append(time.time() - start)
    items[int(i)] = time.time() - start

for i, j in items.items():
    print(f"shape: {i}, time: {j}")

plt.plot(lengths, times, color='blue')

#test hilbert
lengths = np.linspace(3, 30, 28)
items = {}
times = []
for i in lengths:
    start = time.time()
    print(f"{int(i)}/{int(lengths[len(lengths) - 1])}")
    A = getHilbertMatrix(int(i))
    A_csc = csc_array(csc(A), shape=(int(i), int(i)))
    tolerance = 1.0e-3
    eigenvalues, eigenvectors = jacobi(A_csc, tolerance)
    times.append(time.time() - start)
    items[int(i)] = time.time() - start

for i, j in items.items():
    print(f"shape: {i}, time: {j}")

plt.plot(lengths, times, color='orange')
plt.show()
