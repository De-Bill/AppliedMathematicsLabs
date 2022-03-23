import math

import matplotlib as mpl

from methods.fibonacci import fibonacci_search
from methods.golden_section import golden_section_search


def function(x):
    return math.sin(x) - math.log(x * x) - 1


print('Minimum(GS) =', golden_section_search(function, 1, 7, 0.01))
print('Minimum(FS) =', fibonacci_search(function, 1, 7, 0.01, 20))
