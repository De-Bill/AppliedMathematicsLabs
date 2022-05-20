import numpy as np


def csc(A):
    n = A.shape[0]
    data, row_index, indptr = np.array([]), np.array([], dtype=np.int_), np.array([0], dtype=np.int_)

    column_count = 0
    for j in range(n):
        for i in range(n):
            if A[i, j] != 0:
                data = np.append(data, A[i, j])
                row_index = np.append(row_index, i)
                column_count += 1
        indptr = np.append(indptr, column_count)

    return data, row_index, indptr


def csc_eye(n):
    data, row_index, indptr = np.array([1] * n), np.array(range(0, n)), np.array(range(0, n + 1))
    return data, row_index, indptr


def csc_inv(data, row_index, indptr):
    n = len(indptr) - 1
    A = np.zeros((n, n))
    for j in range(n):
        for i in range(indptr[j], indptr[j + 1]):
            A[row_index[i], j] = data[i]

    return A
