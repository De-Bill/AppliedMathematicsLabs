import numpy as np


def parabola_search(func, left_border: float, right_border: float, precision: float):
    middle = (right_border + left_border) / 2
    iters_data = np.array([left_border, right_border, middle, func(middle)])
    i = 0
    while True:
        i+=1
        mas1 = [pow(left_border, 2), left_border, 1]
        mas2 = [pow(middle, 2), middle, 1]
        mas3 = [pow(right_border, 2), right_border, 1]
        a_matrix = np.array([mas1, mas2, mas3])
        result = [func(left_border), func(middle), func(right_border)]
        a, b, c = np.linalg.solve(a_matrix, result)
        minimum = - (b / (2 * a))
        if abs(right_border - left_border) < precision:
            return minimum, func(minimum), iters_data.reshape((iters_data.size // 4, 4))
        if func(right_border) > func(minimum) and func(right_border) > func(left_border):
            if (i == 1):
                iters_data = np.array([left_border, right_border, middle, func(middle)])
            else:
                iters_data = np.append(iters_data, [left_border, right_border, minimum, func(minimum)])
            right_border = middle
            middle = (right_border + left_border) / 2
        else:
            if (i == 1):
                iters_data = np.array([left_border, right_border, middle, func(middle)])
            else:
                iters_data = np.append(iters_data, [left_border, right_border, minimum, func(minimum)])
            left_border = middle
            middle = (right_border + left_border) / 2

    return minimum, func(minimum), iters_data.reshape((iters_data.size // 4, 4))