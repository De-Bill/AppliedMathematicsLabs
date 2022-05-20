import numpy as np
from scipy.sparse import csc_array

from lab3.solving_linear_system import forward_substitution, backward_substitution


def lu_inverse(L : csc_array, U : csc_array):
    n = L.shape[0]
    b = np.eye(n, dtype=np.float_)
    A_inversed = csc_array((n, n), dtype=np.float_)
    for i in range(n):
        y = forward_substitution(L, b[i])
        A_inversed[i] = backward_substitution(U, y)
    return A_inversed
