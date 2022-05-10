import numpy as np


def lu_decomposition(A):
    """Performs an LU Decomposition of A (which must be square)
    into A = PLU. The function returns P, L and U."""
    n = len(A)

    P = np.eye(n)
    U = np.copy(A)
    L = np.eye(n)

    # Loop over rows
    for i in range(n):
        # Eliminate entries below i with row operations
        # on U and reverse the row operations to
        # manipulate L
        for k in range(i, n):
            if ~np.isclose(U[i, i], 0.0):
                break
            U[[k, k + 1]] = U[[k + 1, k]]
            P[[k, k + 1]] = P[[k + 1, k]]
        factor = np.array([])
        for j in range(i + 1, n):
            f = U[j, i] / U[i, i]
            factor = np.append(factor, f)
            L[j, i] = f
            for k in range(n):
                U[j, k] -= f * U[i, k]

    return P, L, U
