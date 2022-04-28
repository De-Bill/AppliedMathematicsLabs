import time
import numpy as np
import matplotlib.pyplot as plt

import lab2.given_func as given
from lab1.methods.golden_ratio import golden_ratio_search


# arguments
precision = 0.05
x_start, y_start = -50, -50

iteration = 0
while True:
    dx, dy = given.df_x(x_start, y_start), given.df_y(x_start, y_start)

    def f_lr(lr):
        return given.f(x_start - lr * dx, y_start - lr * dy)
    learning_rate = golden_ratio_search(f_lr, 0, 0.5, 0.05)[0]

    x_start = x_start - learning_rate * dx
    y_start = y_start - learning_rate * dy

    print(f"iteration: {iteration:.3f}    x:, {x_start:.3f}    y: {y_start:.3f}    f(x,y): {given.f(x_start, y_start):.5f}")
    iteration += 1

    if np.abs(dx) <= precision and np.abs(dy) <= precision:
        break
