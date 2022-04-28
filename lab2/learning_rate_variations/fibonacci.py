import numpy as np

import lab2.given_func as given
from lab1.methods.fibonacci import fibonacci_search


def grad_desc_with_fibonacci_step(x_start, y_start, precision, n_iterations_for_fibonacci):
    iteration = 0
    print(
        f"iteration: {iteration}    x:, {x_start:.3f}    y: {y_start:.3f}    f(x,y): {given.f(x_start, y_start):.5f}")
    iteration += 1

    points = np.array([x_start, y_start])
    while True:
        dx, dy = given.df_x(x_start, y_start), given.df_y(x_start, y_start)

        def f_lr(lr):
            return given.f(x_start - lr * dx, y_start - lr * dy)

        learning_rate = fibonacci_search(f_lr, 0, 0.5, 0.05, n_iterations_for_fibonacci)[0]

        x_start = x_start - learning_rate * dx
        y_start = y_start - learning_rate * dy
        points = np.append(points, [x_start, y_start])

        print(f"iteration: {iteration}    x:, {x_start:.3f}    y: {y_start:.3f}    f(x,y): {given.f(x_start, y_start):.5f}")
        iteration += 1

        if np.abs(dx) <= precision and np.abs(dy) <= precision:
            break

    return points
