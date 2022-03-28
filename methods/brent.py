import numpy as np


def brent(func, left_border, right_border, epsilon):
    k = (3 - np.sqrt(5)) / 2
    x1 = x2 = x3 = left_border + k * (right_border - left_border)
    f_x1 = f_x2 = f_x3 = func(x1)
    current_length = prev_length = right_border - left_border

    counter = 0
    parabola_top = f_top = 0
    iter_data = np.array([])
    while True:
        g, prev_length = prev_length, current_length
        if np.abs(x1 - (left_border + right_border) / 2) + (right_border - left_border) / 2 <= 2 * epsilon:
            break

        if x1 != x2 and x1 != x3 and x2 != x3 and f_x1 != f_x2 and f_x1 != f_x3 and f_x2 != f_x3:
            parabola_top = x2 - ((np.power(x2 - x1, 2) * (f_x2 - f_x3) - np.power(x3 - x2, 2) * (f_x2 - f_x1)) /
                                 (2 * ((x2 - x1) * (f_x2 - f_x3) - (x2 - x3) * (f_x2 - f_x1))))
            if left_border <= parabola_top <= right_border and np.abs(parabola_top - x1) < g / 2:

                if parabola_top - left_border <= 2 * epsilon or right_border - parabola_top <= 2 * epsilon:
                    parabola_top = x1 - np.sign(x1 - (left_border + right_border) / 2) * epsilon

        else:
            if x1 < (left_border + right_border) / 2:
                parabola_top = x1 + k * (right_border - x1)
                prev_length = right_border - x1
            else:
                parabola_top = x1 - k * (x1 - left_border)
                prev_length = x1 - left_border

        if np.abs(parabola_top - x1) < epsilon:
            parabola_top = x1 + np.sign(parabola_top - x1) * epsilon

        current_length = np.abs(parabola_top - x1)
        f_top = func(parabola_top)

        if f_top <= f_x1:
            if parabola_top >= x1:
                left_border = x1
            else:
                right_border = x1

            x3, x2, x1 = x2, x1, parabola_top
            f_x3, f_x2, f_x1 = f_x2, f_x1, f_top

        else:
            if parabola_top >= x1:
                right_border = parabola_top
            else:
                left_border = parabola_top

            if f_top <= f_x2 or x2 == x1:
                x3, x2 = x2, parabola_top
                f_x3, f_x2 = f_x2, f_top
            elif f_top <= f_x3 or x3 == x1 or x3 == x2:
                x3 = parabola_top
                f_x3 = f_top


        counter += 1
        iter_data = np.append(iter_data, [left_border, right_border, x1, x2, x3, parabola_top, f_x1, f_x2, f_x3, f_top])

    return parabola_top, f_top, iter_data.reshape((iter_data.size // 10, 10))