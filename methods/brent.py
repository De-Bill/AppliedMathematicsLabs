import numpy as np
import matplotlib.pyplot as plt


def brent(a, b, epsilon):
    inner_a = a
    inner_b = b
    k = (3 - np.sqrt(5)) / 2
    x = w = v = a + k * (b - a)
    f_x = f_w = f_v = f(x)
    d = e = b - a

    counter = 0
    while True:
        g, e = e, d
        tol = epsilon * (np.abs(x) + 0.01)
        if np.abs(x - (a + b) / 2) + (b - a) / 2 <= 2 * tol:
            break

        u = 0
        if x != w and x != v and w != v and f_x != f_w and f_x != f_v and f_w != f_v:
            u = w - ((np.power(w - x, 2) * (f_w - f_v) - np.power(v - w, 2) * (f_w - f_x)) /
                     (2 * ((w - x) * (f_w - f_v) - (w - v) * (f_w - f_x))))
            if a <= u <= b and np.abs(u - x) < g / 2:

                if u - a < 2 * tol or b - u < 2 * tol:
                    u = x - np.sign(x - (a + b) / 2) * tol

        if u == 0:
            if x < (a + b) / 2:
                u = x + k * (b - x)
                e = b - x
            else:
                u = x - k * (x - a)
                e = x - a

        if np.abs(u - x) < tol:
            u = x + np.sign(u - x) * tol

        d = np.abs(u - x)
        f_u = f(u)

        if f_u <= f_x:
            if u >= x:
                a = x
            else:
                b = x

            v, w, x = w, x, u
            f_v, f_w, f_x = f_w, f_x, f_u

        else:
            if u >= x:
                b = u
            else:
                a = u

            if f_u <= f_w or w == x:
                v, w = w, u
                f_v, f_w = f_w, f_u
            elif f_u <= f_v or v == x or v == w:
                v = u
                f_v = f_u

        print(f'iter {counter}:\n', f'u and f_u: {u}, {f_u}')
        counter += 1
        plt.scatter(u, f_u, marker="x", c="red", s=70)

    x_axis = np.linspace(inner_a + 0.01, inner_b, 1000)
    y_axis = f(x_axis)

    plt.plot(x_axis, y_axis, color="grey")
    plt.xlabel("x")
    plt.ylabel("y = sin(x) - ln(x**2) - 1")
    plt.show()


def f(x):
    return np.sin(x) - np.log(np.power(x, 2)) - 1


brent(0, 8, 0.01)
