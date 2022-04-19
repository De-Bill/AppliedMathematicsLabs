import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from methods.brent import brent
from methods.fibonacci import fibonacci_search
from methods.golden_ratio import golden_ratio_search
from methods.dichotomy import dichotomy_search
from methods.parabola import parabola_search


def function(x):
    return np.sin(x) - np.log(x * x) - 1


def test_function_1(x):
    return np.log2(x) * np.cos(x) + 4


def test_function_2(x):
    return np.power(x, 5) + np.power(x, 4) + np.power(x, 2) - 1


def test_function_3(x):
    return np.sin(x) * np.power(x, 2)


precisions = np.linspace(0.00001, 0.1, 100)


def plot_figure(method, color, n_iter=0, label="", func=None):
    if func is None:
        func = function

    iterations = np.array([])
    for precision in precisions:
        if n_iter == 0:
            func_res = np.array(method(func, 1, 7, precision)[2])
        else:
            func_res = np.array(method(func, 1, 7, precision, n_iter)[2])
        iterations = np.append(iterations, func_res.shape[0])

    plt.plot(precisions, iterations, color=color, label=label)


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

print('---------------Brent-Method-----------------------')
br = brent(function, 1, 7, 0.01)
df_br = pd.DataFrame(data=br[2],
                     columns=['left_border', 'right_border', 'x1', 'x2', 'x3', 'parabola_top', 'f_x1', 'f_x2', 'f_x3',
                              'f_top'])
print(df_br)
print(df_br["parabola_top"], df_br["f_top"])

with pd.ExcelWriter("AppliedMathsTest.xlsx") as writer:
    df_dich.to_excel(writer, sheet_name='Dichotomy')
    df_gr.to_excel(writer, sheet_name='GoldenRatio')
    df_fib.to_excel(writer, sheet_name='Fibonacci')
    df_par.to_excel(writer, sheet_name='Parabola')
    df_br.to_excel(writer, sheet_name='Brent')


plt.xlabel("precision")
plt.ylabel("iteration")

plot_figure(dichotomy_search, "blue", label='dichotomy', func=function)
plot_figure(golden_ratio_search, "red", label='golden_ratio', func=function)
plot_figure(fibonacci_search, "green", label='fibonacci', n_iter=20, func=function)
plot_figure(parabola_search, "purple", label='parabola', func=function)
plot_figure(brent, "orange", label='brent', func=function)

plt.legend()
plt.show()
