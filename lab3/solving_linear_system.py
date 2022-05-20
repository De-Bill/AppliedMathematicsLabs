import numpy as np
from scipy.sparse import csc_array


def lu_solve(L : csc_array, U : csc_array, b):
    y = forward_substitution(L, b)
    return backward_substitution(U, y)


def forward_substitution(L : csc_array, b):
    # Get number of rows
    n = L.shape[0]

    # Allocating space for the solution vector
    y = np.zeros_like(b, dtype=np.float_)

    # Here we perform the forward-substitution.
    # Initializing with the first row.
    y[0] = b[0] / L[0, 0]  # == b[0] / 1

    # Looping over rows from the top down,
    # starting with the second to last row, because  the
    # first row solve was completed in the last step.
    for i in range(1, n):
        s = 0
        for j in range(i):
            s += L[i, j] * y[j]
        y[i] = (b[i] - s) / L[i, i]

    return y


def backward_substitution(U : csc_array, y):
    # Number of rows
    n = U.shape[0]

    # Allocating space for the solution vector
    x = np.zeros_like(y, dtype=np.float_)

    # Here we perform the back-substitution.
    # Initializing with the last row.
    x[-1] = y[-1] / U[-1, -1]

    # Looping over rows in reverse (from the bottom up),
    # starting with the second to last row, because the
    # last row solve was completed in the last step.
    for i in range(n-2, -1, -1):
        s = 0
        for j in range(i, n):
            s += U[i, j] * x[j]
        x[i] = (y[i] - s) / U[i, i]

    return x
