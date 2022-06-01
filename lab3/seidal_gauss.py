import numpy as np

def foo(A, B):
   matrixA = np.copy(A)
   y = np.copy(B)
   n = A.shape[0]
   x = np.zeros(A.shape[0])

   for i in range(n):
      x[i] = y[i] / matrixA[i][i]
   while True:
      x_last = x.copy()
      for i in range(n):
         s = y[i]
         for j in range(n):
            if i == j:
               continue
            s += (-1) * x[j] * matrixA[i][j]
         x[i] = s / matrixA[i][i]
      if break_condition(x_last, x):
         break
   print(x[0])


def break_condition(x1: list[float], x2: list[float]): # check precision
   bools = [False for x in range(len(x1))]

   for i in range(len(x1)):
      bools[i] = abs(x2[i] - x1[i]) < 10 ** (-2)

   print(x2)
   return all(bools)


