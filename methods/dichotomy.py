import numpy as np


def dichotomy_search(func, left_border: float, right_border: float, precision: float):

    middle_x = (left_border + right_border) / 2
    f_left = func(left_border)
    f_right = func(right_border)
    iters_data = np.array([left_border, right_border, middle_x, func(middle_x)])
    while abs(right_border - left_border) > precision:
        if f_left > f_right:
            if func(middle_x) < f_left:
                left_border = middle_x
                f_left = func(left_border)
                middle_x = (left_border + right_border) / 2
        else:
            if func(middle_x) < f_right:
                right_border = middle_x
                f_right = func(right_border)
                middle_x = (left_border + right_border) / 2

        iters_data = np.append(iters_data, [left_border, right_border, middle_x, func(middle_x)])

    return middle_x, func(middle_x), iters_data.reshape((iters_data.size // 4, 4))
