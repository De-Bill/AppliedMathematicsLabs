import numpy as np
from scipy.sparse import csc_array


def lu_decomposition(A : csc_array):
    """Performs an LU Decomposition of A (which must be square)
    into A = PLU. The function returns P, L and U."""
    n = len(A.indptr) - 1

    U = csc_array.copy(A)
    L = csc_array(np.eye(n))
    # Loop over rows
    for i in range(n):
        # Eliminate entries below i with row operations
        # on U and reverse the row operations to
        # manipulate L
        factor = np.array([])
        for j in range(i + 1, n):
            f = U[j, i] / U[i, i]
            factor = np.append(factor, f)
            L[j, i] = f
            for k in range(n):
                U[j, k] -= f * U[i, k]
    # Loop over rows
    return L, U
