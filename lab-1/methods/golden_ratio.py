import numpy as np


def golden_ratio_search(func, left_border: float, right_border: float, precision: float):
    k = (np.sqrt(5) - 1) / 2

    length0 = right_border - left_border  # start length
    length_next = k * length0  #
    a = right_border - length_next
    b = left_border + length_next
    f_a, f_b = func(a), func(b)
    i = 0
    iters_data = np.array([left_border, right_border, a, b, f_a, f_b])
    while length_next >= precision:
        i += 1
        length_next = k * length_next
        if f_a >= f_b:
            left_border = a
            a = b
            b = left_border + length_next
            f_a, f_b = f_b, func(b)
        else:
            right_border = b
            b = a
            a = right_border - length_next
            f_a, f_b = func(a), f_a
        iters_data = np.append(iters_data, [left_border, right_border, a, b, f_a, f_b])
    m = (a + b) / 2
    return m, func(m), iters_data.reshape((iters_data.size // 6, 6))
