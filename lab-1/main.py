import numpy as np
import pandas as pd

from methods.fibonacci import fibonacci_search
from methods.golden_ratio import golden_ratio_search
from methods.dichotomy import dichotomy_search
from methods.parabola import parabola_search


def function(x):
    return np.sin(x) - np.log(x * x) - 1


print('--------------Dichotomy-Search-----------------------')
dich = dichotomy_search(function, 1, 7, 0.01)
df_dich = pd.DataFrame(data=dich[2], columns=['left_border', 'right_border', 'middle', 'f(middle)'])
print(df_dich)

print('------------Golden-Section-Search-------------------')
gr = golden_ratio_search(function, 1, 7, 0.01)
df_gr = pd.DataFrame(data=gr[2], columns=['left_border', 'right_border', 'a', 'b', 'f(a)', 'f(b)'])
print(df_gr)

print('--------------Fibonacci-Search-----------------------')
fib = fibonacci_search(function, 1, 7, 0.01, 20)
df_fib = pd.DataFrame(data=fib[2], columns=['left_border', 'right_border', 'a', 'b', 'f(a)', 'f(b)'])
print(df_fib)

print('---------------Parabola-Method-----------------------')
par = parabola_search(function, 1, 7, 0.01)
df_par = pd.DataFrame(data=par[2], columns=['left_border', 'right_border', 'middle', 'f(middle)'])
print(df_par)

with pd.ExcelWriter("../AppliedMathsTest.xlsx") as writer:
    df_dich.to_excel(writer, sheet_name='Dichotomy')
    df_gr.to_excel(writer, sheet_name='GoldenRatio')
    df_fib.to_excel(writer, sheet_name='Fibonacci')
    df_par.to_excel(writer, sheet_name='Parabola')

