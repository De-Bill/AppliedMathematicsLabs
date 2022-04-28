import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

import given_func as given
from learning_rate_variations.const import grad_desc_with_const_lr
from learning_rate_variations.fractional import grad_desc_with_fractional_step
from learning_rate_variations.fibonacci import grad_desc_with_fibonacci_step
from learning_rate_variations.golden_ratio import grad_desc_with_golden_ratio_step
from methods.conjugate_gradient import conjugate_gradient


def plot_function(function):
    X, Y = np.meshgrid(np.linspace(-7, 7, 100),
                       np.linspace(-7, 7, 100))

    plt.figure(figsize=(16, 10))

    axis = plt.subplot(projection='3d')

    zs = np.array([function(x, y) for [x, y] in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    axis.plot_surface(X, Y, Z, cmap=cm.coolwarm, zorder=2)

    axis.set_zlim(-5, 40)
    axis.view_init(elev=60)
    plt.show()


x = np.linspace(-1.8, 1.8, 50)
y = np.linspace(-1.8, 1.8, 50)
X, Y = np.meshgrid(x, y)
F = given.f(X, Y)

x_start, y_start = 1, 1
precision = 0.06
points = conjugate_gradient(x_start=x_start, y_start=y_start, epsilon=precision)

ax = plt.subplots()[1]

ax.scatter(points[0:len(points):2], points[1:len(points):2], marker='*', color='red')
ax.plot(points[0:len(points):2], points[1:len(points):2])
ax.contour(X, Y, F, 40)

plt.show()

plot_function(given.f)
