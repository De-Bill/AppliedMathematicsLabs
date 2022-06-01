from random import choice
import numpy as np

def gen_diagonal_saturated_matrix(n, k):
    A_k = np.zeros(shape=(n, n))
    a_ij = [-1, -2, -3, -4]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            randomIJ = choice(a_ij)
            A_k[i, j] += randomIJ + 10 ** (-k)

    for i in range(n):
        sum = 0
        for j in range(n):
            if i == j:
                continue
            sum += A_k[i, j]
        A_k[i, i] = sum

    return A_k