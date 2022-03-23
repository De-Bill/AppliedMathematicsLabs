import array

import function


def get_fibonacci_numbers(n):
    if n in {0, 1}:
        return n
    nums = array.array('i', [0, 1, 1])
    for i in range(2, n):
        nums.append(nums[i] + nums[i - 1])
    return nums


def fibonacci_search(func : function, left_border, right_border, precision, n_iters):
    fib_nums = get_fibonacci_numbers(n_iters)
    a = left_border + fib_nums[n_iters - 2] / fib_nums[n_iters] * (right_border - left_border)
    b = left_border + fib_nums[n_iters - 1] / fib_nums[n_iters] * (right_border - left_border)
    f_a, f_b = func(a), func(b)
    print('--------------Fibonacci-Search-----------------------')
    print(' N    l_b      r_b      a      b       f_a      f_b')
    print(f"{0:2}    {left_border:.2f}    {right_border:.2f}    {a:.2f}    {b:.2f}    {f_a:.2f}    {f_b:.2f}")
    for k in range(1, n_iters - 1):
        if f_a >= f_b:
            left_border = a
            a, b = b, left_border + (fib_nums[n_iters - k - 1] / fib_nums[n_iters - k]) * (right_border - left_border)
            f_a, f_b = f_b, func(b)
        else:
            right_border = b
            b, a = a, left_border + (fib_nums[n_iters - k - 2] / fib_nums[n_iters - k]) * (right_border - left_border)
            f_b, f_a = f_a, func(a)
        print(f"{k:2}    {left_border:.2f}    {right_border:.2f}    {a:.2f}    {b:.2f}    {f_a:.2f}    {f_b:.2f}")
        if right_border - left_border < precision:
            m = (a + b) / 2
            return m, func(m)
    m = (a + b) / 2
    return m, func(m)
