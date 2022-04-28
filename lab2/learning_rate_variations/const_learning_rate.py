import time
import numpy as np
import matplotlib.pyplot as plt

import lab2.given_func as given


# arguments
n_iterations = 5
x_start = -50
y_start = -50
learning_rate = 0.05

for i in range(n_iterations):
    x_start = x_start - learning_rate * given.df_x(x_start, y_start)
    y_start = y_start - learning_rate * given.df_y(x_start, y_start)

    print(f"iteration: {i:.3f}    x:, {x_start:.3f}    y: {y_start:.3f}    f(x,y): {given.f(x_start, y_start):.5f}")
