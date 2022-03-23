import math

import function


def golden_section_search(func: function, left_border: float, right_border: float, precision: float):
    k = (math.sqrt(5) - 1) / 2
    length0 = right_border - left_border  # start length
    length_next = k * length0  #
    a = right_border - length_next
    b = left_border + length_next
    f_a, f_b = func(a), func(b)
    i = 0
    print('------------Golden-Section-Search-------------------')
    print(' N    l_b      r_b      a      b       f_a      f_b')
    print(f"{i:2}    {left_border:.2f}    {right_border:.2f}    {a:.2f}    {b:.2f}    {f_a:.2f}    {f_b:.2f}")
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
        print(f"{i:2}    {left_border:.2f}    {right_border:.2f}    {a:.2f}    {b:.2f}    {f_a:.2f}    {f_b:.2f}")
    m = (a + b) / 2
    return m, func(m)
