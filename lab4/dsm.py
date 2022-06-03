from random import choice

import numpy as np


def gen_dsm(n, k):
    A = np.zeros((n, n), dtype='float64')
    a_ij = [-1, -2, -3, -4]

    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue

            randomIJ = choice(a_ij)
            A[i, j] = randomIJ
            A[j, i] = randomIJ

    for i in range(n):
        sum = 0
        for j in range(n):
            if i == j:
                continue

            sum += A[i, j]
        A[i, i] = sum + 10 ** (-k)

    return A
