import numpy as np
import matplotlib.pyplot as plt

import given_func as given
from learning_rate_variations.const import grad_desc_with_const_lr
from learning_rate_variations.fractional import grad_desc_with_fractional_step
from learning_rate_variations.fibonacci import grad_desc_with_fibonacci_step
from learning_rate_variations.golden_ratio import grad_desc_with_golden_ratio_step

x = np.linspace(-1.8, 1.8, 50)
y = np.linspace(-1.8, 1.8, 50)
X, Y = np.meshgrid(x, y)
F = given.f(X, Y)

x_start, y_start = 1, 1
precision = 0.06
points = grad_desc_with_fractional_step(x_start, y_start, 0.2, precision, 0.1, 0.95)

ax = plt.subplots()[1]
for i in range(0, points.size, 2):
    ax.scatter(points[i], points[i+1])
plt.contour(X, Y, F, 40)
plt.show()
