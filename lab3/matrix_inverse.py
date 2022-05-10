import numpy as np

from lab3.solving_linear_system import forward_substitution, backward_substitution


def lu_inverse(P, L, U):
    n = P.shape[0]
    b = np.eye(n)
    A_inversed = np.zeros((n, n))
    for i in range(n):
        y = forward_substitution(L, P @ b[i])
        A_inversed[i] = backward_substitution(U, y)
    return A_inversed
