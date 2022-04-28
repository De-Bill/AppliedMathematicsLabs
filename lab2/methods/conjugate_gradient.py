import numpy as np


def f(x, y):  # given func
    return x * x + 2 * y * y + 2 * x * y


def square_form_f():
    return 2 * np.array([[1, 1], [1, 2]], dtype='float64')  # double square form


def calculate_step(gradient, d_k, square_form=square_form_f):
    return - (gradient.T @ d_k) / (d_k.T @ square_form() @ d_k)


def calculate_beta(gradient, d_k, square_form=square_form_f):
    return (gradient.T @ square_form() @ d_k) / (d_k.T @ square_form() @ d_k)


def df_x(x, y):  # derivative of the given func -- df/dx
    return 2 * x + 2 * y


def df_y(x, y):  # -- df/dy
    return 4 * y + 2 * x


def grad_f(x):
    return np.array([df_x(x[0], x[1]), df_y(x[0], x[1])])


def conjugate_gradient(epsilon):
    k = 0
    x_k = np.array([-1000, -1200], dtype='float64')

    alpha_k = 0
    while True:
        gradient = grad_f(x_k)
        grad_norm = np.linalg.norm(gradient)

        print(
            f"iteration: {k}    x:, {x_k[0]:.3f}    y: {x_k[1]:.3f}    f(x,y): {f(x_k[0], x_k[1]):.5f}")

        if grad_norm <= epsilon:
            return f(x_k[0], x_k[1]), k

        if k == 0:
            alpha_k = -gradient
            step = calculate_step(gradient, alpha_k)
            x_k += step * alpha_k
            k += 1
            continue

        beta_k = calculate_beta(gradient, alpha_k)
        alpha_k = -gradient + beta_k * alpha_k

        step = calculate_step(gradient, alpha_k)
        x_k += step * alpha_k

        k += 1


print(conjugate_gradient(0.0001))
