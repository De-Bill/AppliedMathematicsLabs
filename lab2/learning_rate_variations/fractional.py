import numpy as np

import lab2.given_func as given


def grad_desc_with_fractional_step(x_start, y_start, learning_rate, precision, epsilon, delta):
    iteration = 0
    print(
        f"iteration: {iteration:.3f}    x:, {x_start:.3f}    y: {y_start:.3f}    f(x,y): {given.f(x_start, y_start):.5f}")
    iteration += 1

    points = np.array([x_start, y_start])
    while True:
        dx, dy = given.df_x(x_start, y_start), given.df_y(x_start, y_start)
        x_next = x_start - learning_rate * dx
        y_next = y_start - learning_rate * dy

        if given.f(x_start, y_start) - given.f(x_next, y_next) > epsilon * learning_rate * (dx ** 2 + dy ** 2):
            x_next = x_start - (learning_rate * delta) * dx
            y_next = y_start - (learning_rate * delta) * dy

        x_start = x_next
        y_start = y_next
        points = np.append(points, [x_start, y_start])

        print(f"iteration: {iteration:.3f}    x:, {x_start:.3f}    y: {y_start:.3f}    f(x,y): {given.f(x_start, y_start):.5f}")
        iteration += 1

        if np.abs(given.df_x(x_start, y_start)) <= precision and np.abs(given.df_y(x_start, y_start)) <= precision:
            break

    return points
