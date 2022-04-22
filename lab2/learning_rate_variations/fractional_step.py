import time
import numpy as np
import matplotlib.pyplot as plt

import lab2.given_func as given


# arguments
n_iterations = 20
x_start = 0
y_start = 0
learning_rate = 0.1
epsilon = 0.1
delta = 0.95

for i in range(n_iterations):
    x_next = x_start - learning_rate * given.df_x(x_start, y_start)
    y_next = y_start - learning_rate * given.df_y(x_start, y_start)
    if given.f(x_start, y_start) - given.f(x_next, y_next) > epsilon * learning_rate * (given.df_x(x_start) ** 2):
        x_next = delta * x_start
        y_next = delta * x_start

    x_start = x_next
    y_start = y_next

    print(f"iteration: {i:.3f}    x:, {x_start:.3f}    y: {y_start:.3f}    f(x,y): {given.f(x_start, y_start):.5f}")
