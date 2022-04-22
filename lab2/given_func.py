import numpy as np


def f(x, y):   # given func
    return x * x + 2 * y * y + np.exp(x + y)


def df_x(x, y):  # derivative of the given func -- df/dx
    return 2 * x + np.exp(x + y)


def df_y(x, y):  # -- df/dy
    return 4 * y + np.exp(x + y)