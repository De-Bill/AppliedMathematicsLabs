import time
import numpy as np
import matplotlib.pyplot as plt


def f(x):   # given func
    return x*x - 5*x + 5


def df(x):  # derivative of the given func
    return 2*x - 5


# arguments
n_iterations = 20
x_start = 0
learning_rate = 0.1
epsilon = 0.1
delta = 0.95

x_plt = np.arange(0, 5.0, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()   # turn on interactive mode
fig_x, ax = plt.subplots()
ax.grid(True)

ax.plot(x_plt, f_plt)
point = ax.scatter(x_start, f(x_start), c='red')

for i in range(n_iterations):
    x_next = x_start - learning_rate * df(x_start)
    if f(x_next) > f(x_start) - epsilon * learning_rate * df(x_start):
        x_next = delta * x_start

    x_start = x_next
    point.set_offsets([x_start, f(x_start)])

    fig_x.canvas.draw()
    fig_x.canvas.flush_events()
    time.sleep(0.02)

plt.ioff()
print(x_start)
ax.scatter(x_start, f(x_start), c='blue')
plt.show()
