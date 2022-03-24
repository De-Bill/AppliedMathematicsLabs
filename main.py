import numpy as np
import pandas as pd
import openpyxl

from methods.fibonacci import fibonacci_search
from methods.golden_ratio import golden_ratio_search


def function(x):
    return np.sin(x) - np.log(x * x) - 1


print('------------Golden-Section-Search-------------------')
gr = golden_ratio_search(function, 1, 7, 0.01)
df_gr = pd.DataFrame(data=gr[2], columns=['left_border', 'right_border', 'a', 'b', 'f(a)', 'f(b)'])
print(df_gr)

print('--------------Fibonacci-Search-----------------------')
fib = fibonacci_search(function, 1, 7, 0.01, 20)
df_fib = pd.DataFrame(data=fib[2], columns=['left_border', 'right_border', 'a', 'b', 'f(a)', 'f(b)'])
print(df_fib)

with pd.ExcelWriter("AppliedMathsTest.xlsx") as writer:
    df_gr.to_excel(writer, sheet_name='GoldenRatio')
    df_fib.to_excel(writer, sheet_name='Fibonacci')

