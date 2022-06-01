import numpy as np


def getHilbertMatrix(n):
    H_arr = np.zeros((n, n), dtype='float64')

    for i in range(n):
        for j in range(n):
            H_arr[i][j] = 1 / (i + j + 1)

    return H_arr
