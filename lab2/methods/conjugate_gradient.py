import numpy as np


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


def find_step(x_prev, func):
    return func(x_prev[0], x_prev[1])


def conjugate_gradient(epsilon):
    x_prev = np.array([-50, -50], dtype='float64')
    prev_gradient = grad(x_prev)
    prev_grad_norm = norm(prev_gradient)
    k = 0
    n = 2
    x_k = np.array([-50, -50], dtype='float64')
    beta = alfa = 0
    while True:
        prev_gradient = grad(x_prev)
        prev_grad_norm = norm(prev_gradient)
        if prev_grad_norm <= epsilon:
            return f(x_prev[0], x_prev[1]), k

        gradient = grad(x_k)
        grad_norm = norm(gradient)

        if k == 0:
            step = find_step(x_prev, calculate_step_f)
            x_prev = x_k
            x_k = x_prev - step * prev_gradient

            k += 1
            continue

        step = find_step(x_prev, calculate_step_f)
        x_prev = x_k
        x_k = x_prev - step * prev_gradient

        k += 1


print(conjugate_gradient(0.05))
