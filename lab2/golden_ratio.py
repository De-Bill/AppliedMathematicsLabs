import time
import numpy as np
import matplotlib.pyplot as plt

from lab1.methods.golden_ratio import golden_ratio_search


def f(x, y):   # given func
    return x * x + 2 * y * y + np.exp(x + y)


def df_x(x, y):  # derivative of the given func -- df/dx
    return 2 * x + np.exp(x + y)


def df_y(x, y):  # -- df/dy
    return 4 * y + np.exp(x + y)


# arguments
precision = 0.05
x_start, y_start = 0, 0

while True:
    dx, dy = df_x(x_start, y_start), df_y(x_start, y_start)

    def f_lr(lr):
        return f(x_start - lr * dx, y_start - lr * dy)
    learning_rate = golden_ratio_search(f_lr, 0, 0.5, 0.05)[0]

    x_start = x_start - learning_rate * dx
    y_start = y_start - learning_rate * dy

    if np.abs(dx) <= precision and np.abs(dy) <= precision:
        break

print('x:', x_start, '    y:', y_start, '    f(x,y):', f(x_start, y_start))

