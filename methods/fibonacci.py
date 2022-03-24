import numpy as np


def get_fibonacci_numbers(n):
    if n in {0, 1}:
        return n
    nums = np.array([0, 1, 1])
    for i in range(2, n):
        nums = np.append(nums, nums[i] + nums[i - 1])
    return nums


def fibonacci_search(func, left_border: float, right_border: float, precision: float, n_iters: int):
    fib_nums = get_fibonacci_numbers(n_iters)
    a = left_border + fib_nums[n_iters - 2] / fib_nums[n_iters] * (right_border - left_border)
    b = left_border + fib_nums[n_iters - 1] / fib_nums[n_iters] * (right_border - left_border)
    f_a, f_b = func(a), func(b)

    iters_data = np.array([left_border, right_border, a, b, f_a, f_b])
    for k in range(1, n_iters - 1):
        if f_a >= f_b:
            left_border = a
            a, b = b, left_border + (fib_nums[n_iters - k - 1] / fib_nums[n_iters - k]) * (right_border - left_border)
            f_a, f_b = f_b, func(b)
        else:
            right_border = b
            b, a = a, left_border + (fib_nums[n_iters - k - 2] / fib_nums[n_iters - k]) * (right_border - left_border)
            f_b, f_a = f_a, func(a)
        iters_data = np.append(iters_data, [left_border, right_border, a, b, f_a, f_b])
        if right_border - left_border < precision:
            m = (a + b) / 2
            return m, func(m), iters_data.reshape((iters_data.size // 6, 6))
    m = (a + b) / 2
    return m, func(m), iters_data.reshape((iters_data.size // 6, 6))
