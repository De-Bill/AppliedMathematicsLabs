def foo():
   matrixA = [
      [7, 3, -1, 2],
      [3, 8, 1, -4],
      [-1, 1, 4, -1],
      [2, -4, -1, 6]
   ]

   x = [0, 0, 0, 0]

   y = [5, 6, 7, 8]

   for i in range(4):
      x[i] = y[i] / matrixA[i][i]
   while True:
      x_last = x.copy()
      for i in range(4):
         s = y[i]
         for j in range(4):
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

foo()

