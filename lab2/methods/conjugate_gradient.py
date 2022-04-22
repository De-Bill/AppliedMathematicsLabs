import numpy as np
from lab2.given_func import grad as gradient


def norm(x):
    return np.sqrt(np.power(x[0], 2) + np.power(x[1], 2))


def conjugate_gradient(epsilon):
    start = [0, 0]
    start_grad = gradient(start)

    k = 0

    x_k = [0, 0]
    result = [0, 0]
    while True:
        grad = gradient(x_k)

        if norm(grad) < epsilon:
            return result

        elif k == 0:
            p_0 = -gradient(start)


def ConjGrad(a, b, x):
    r = (b - np.dot(np.array(a), x))
    p = r
    rsold = np.dot(r.T, r)

    for i in range(len(b)):
        a_p = np.dot(a, p)
        alpha = rsold / np.dot(p.T, a_p)
        x = x + (alpha * p)
        r = r - (alpha * a_p)
        rsnew = np.dot(r.T, r)
        if np.sqrt(rsnew) < (10 ** -5):
            break
        p = r + ((rsnew / rsold) * p)
        rsold = rsnew
    return p


print(ConjGrad(np.array))