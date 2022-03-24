import numpy as np


def dichotomy_search(func, left_border: float, right_border: float, precision: float):

    middlex = (left_border + right_border) / 2
    left = func(left_border)
    right = func(right_border)
    i = 0
    iters_data = np.array([left_border, right_border, middlex, func(middlex)])
    while abs(right_border - left_border) > precision:
        i+=1
        if left > right:
            if func(middlex) < left:
                left_border = middlex
                left = func(left_border)
                middlex = (left_border + right_border) / 2
        else:
            if func(middlex) < right:
                right_border = middlex
                right = func(right_border)
                middlex = (left_border + right_border) / 2

        iters_data = np.append(iters_data, [left_border, right_border, middlex, func(middlex)])

    return middlex, func(middlex), iters_data.reshape((iters_data.size // 4, 4))
