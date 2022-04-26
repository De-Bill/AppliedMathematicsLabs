import numpy as np
from lab2.given_func import grad as gradient


def f(x, y):  # given func
    return x * x + 2 * y * y + 2 * x * y


def calculate_step_f(x_coeff, y_coeff):
    #return (2*np.power(x_coeff, 2) + 5*x_coeff*y_coeff + 3*np.power(y_coeff, 2) + 4*x_coeff + 6*y_coeff)/(8*np.power(x_coeff, 2)  + 24*x_coeff*y_coeff + 18*np.power(y_coeff, 2))
    return (x_coeff + y_coeff) / \
           (4 * x_coeff + 6 * y_coeff)


def df_x(x, y):  # derivative of the given func -- df/dx
    return 2 * x + 2 * y


def df_y(x, y):  # -- df/dy
    return 4 * y + 2 * x


def grad(x):
    return np.array([df_x(x[0], x[1]), df_y(x[0], x[1])])


def norm(x):  # vector_length
    return np.sqrt(np.power(x[0], 2) + np.power(x[1], 2))


def conjugate_gradient(epsilon):
    start = [0, 0]
    start_grad = gradient(start)

    k = 0
    x_k = np.array([0, 0], dtype='float64')
    beta = alfa = 0
    while True:
        prev_gradient = grad(x_prev)
        prev_grad_norm = norm(prev_gradient)
        if prev_grad_norm <= epsilon:
            return f(x_k[0], x_k[1])

        gradient = grad(x_k)
        grad_norm = norm(gradient)


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