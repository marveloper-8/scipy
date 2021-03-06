# from scipy import constants
# print(constants.liter)

# import scipy
# print(scipy.__version__)

# from scipy import constants
# print(constants.pi)

# print(dir(constants))

# print(constants.yotta)
# print(constants.zetta)
# print(constants.exa)
# print(constants.peta)
# print(constants.tera)
# print(constants.giga)
# print(constants.mega)
# print(constants.kilo)
# print(constants.hecto)
# print(constants.deka)
# print(constants.deci)
# print(constants.centi)
# print(constants.milli)
# print(constants.micro)
# print(constants.nano)
# print(constants.pico)
# print(constants.femto)
# print(constants.atto)
# print(constants.zepto)

# from scipy import constants

# print(constants.kibi)
# print(constants.mebi)
# print(constants.gibi)
# print(constants.tebi)
# print(constants.pebi)
# print(constants.exbi)
# print(constants.zebi)
# print(constants.yobi)

# from scipy import constants

# print(constants.gram)
# print(constants.metric_ton)
# print(constants.grain)
# print(constants.lb)
# print(constants.pound)
# print(constants.oz)
# print(constants.ounce)
# print(constants.stone)
# print(constants.long_ton)
# print(constants.short_ton)
# print(constants.troy_ounce)
# print(constants.troy_pound)
# print(constants.carat)
# print(constants.atomic_mass)
# print(constants.m_u)
# print(constants.u)

# from scipy import constants

# print(constants.degree)
# print(constants.arcmin)
# print(constants.arcminute)
# print(constants.arcsec)
# print(constants.arcsecond)

# from scipy import constants

# print(constants.minute)
# print(constants.hour)
# print(constants.day)
# print(constants.week)
# print(constants.year)
# print(constants.Julian_year)

# from scipy import constants

# print(constants.inch)
# print(constants.foot)
# print(constants.yard)
# print(constants.mile)
# print(constants.mil)
# print(constants.pt)
# print(constants.point)
# print(constants.survey_foot)
# print(constants.survey_mile)
# print(constants.nautical_mile)
# print(constants.fermi)
# print(constants.angstrom)
# print(constants.micron)
# print(constants.au)
# print(constants.astronomical_unit)
# print(constants.light_year)
# print(constants.parsec)

# from scipy import constants

# print(constants.atm)
# print(constants.atmosphere)
# print(constants.bar)
# print(constants.torr)
# print(constants.mmHg)
# print(constants.psi)

# from scipy import constants

# print(constants.hectare)
# print(constants.acre)

# from scipy import constants

# print(constants.liter)
# print(constants.litre)
# print(constants.gallon)
# print(constants.gallon_US)
# print(constants.gallon_imp)
# print(constants.fluid_ounce)
# print(constants.fluid_ounce_US)
# print(constants.fluid_ounce_imp)
# print(constants.barrel)
# print(constants.bbl)

# from scipy import constants

# print(constants.kmh)
# print(constants.mph)
# print(constants.mach)
# print(constants.speed_of_sound)
# print(constants.knot)

# from scipy import constants

# print(constants.zero_Celsius)
# print(constants.degree_Fahrenheit)

# from scipy import constants

# print(constants.eV)
# print(constants.electron_volt)
# print(constants.calorie)
# print(constants.calorie_IT)
# print(constants.erg)
# print(constants.Btu)
# print(constants.Btu_IT)
# print(constants.Btu_th)
# print(constants.ton_TNT)

# from scipy import constants

# print(constants.hp)
# print(constants.horsepower)

# from scipy import constants

# print(constants.dyn)
# print(constants.dyne)
# print(constants.lbf)
# print(constants.pound_force)
# print(constants.kgf)
# print(constants.kilogram_force)

# from scipy.optimize import root
# from math import cos

# def eqn(x):
#     return x + cos(x)

# c = root(eqn, 0)
# print(c.x)
# print(c)

# from scipy.optimize import minimize

# def a(x):
#     return x**2 + x + 2

# b = minimize(a, 0, method='BFGS')
# print(b)

# import numpy as np
# from scipy.sparse import csr_matrix

# a = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
# b = csr_matrix(a).tocsc()
# print(b)

# b = csr_matrix(a)
# b.sum_duplicates()
# print(b)

# b = csr_matrix(a)
# b.eliminate_zeros()
# print(b)

# print(csr_matrix(a).count_nonzero())

# print(csr_matrix(a).data)

# a = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
# print(csr_matrix(a))

# import numpy as np
# from scipy.sparse.csgraph import connected_components, dijkstra, floyd_warshall, bellman_ford, depth_first_order, breadth_first_order
# from scipy.sparse import csr_matrix

# a = np.array([
#     [0, 1, 2],
#     [1, 0, 0],
#     [2, 0, 0]
# ])
# c = np.array([
#     [0, -1, 2],
#     [1, 0, 0],
#     [2, 0, 0]
# ])
# e = np.array([
#     [0, 1, 0, 1],
#     [1, 1, 1, 1],
#     [2, 1, 1, 0],
#     [0, 1, 0, 1]
# ])

# b = csr_matrix(a)
# d = csr_matrix(c)
# f = csr_matrix(e)

# print(connected_components(b))
# print(dijkstra(b, return_predecessors=True, indices=0))
# print(floyd_warshall(b, return_predecessors=True))
# print(bellman_ford(d, return_predecessors=True, indices=0))
# print(depth_first_order(f, 1))
# print(breadth_first_order(f, 1))

# import numpy as np
# from scipy.spatial import Delaunay
# import matplotlib.pyplot as plt

# a = np.array([
#     [2, 4],
#     [3, 4],
#     [3, 0],
#     [2, 2],
#     [4, 1]
# ])

# simplices = Delaunay(a).simplices

# plt.triplot(a[:, 0], a[:, 1], simplices)
# plt.scatter(a[:, 0], a[:, 1], color='r')

# plt.show()

# import numpy as np
# from scipy.spatial import ConvexHull
# import matplotlib.pyplot as plt

# a = np.array([
#     [2, 4],
#     [3, 4],
#     [3, 0],
#     [2, 2],
#     [4, 1],
#     [1, 2],
#     [5, 0],
#     [3, 1],
#     [1, 2],
#     [0, 2]
# ])

# hull = ConvexHull(a)
# hull_points = hull.simplices

# plt.scatter(a[:, 0], a[:,1])
# for simplex in hull_points:
#     plt.plot(a[simplex, 0], a[simplex, 1], 'k-')

# plt.show()

# from scipy.spatial import KDTree

# a = [(1, -1), (2, 3), (-2, 3), (2, -3)]
# kdtree = KDTree(a)
# b = kdtree.query((1, 1))
# print(b)

# from scipy.spatial.distance import euclidean, cityblock, cosine, hamming

# c = (1, 0)
# d = (10, 2)
# e = euclidean(c, d)
# print(e)

# f = cityblock(c, d)
# print(f)

# g = cosine(c, d)
# print(g)

# h = (True, False, True)
# i = (False, True, True)

# j = hamming(h, i)
# print(j)

# from scipy import io
# import numpy as np

# a = np.arange(10)
# io.savemat('a.mat', {"vec": a})
# b = io.loadmat('a.mat')
# print(b)
# print(b['vec'])

# c = io.loadmat('a.mat', squeeze_me=True)
# print(c['vec'])

# from scipy.interpolate import interp1d, UnivariateSpline, Rbf
# import numpy as np
# a = np.arange(10)
# b = 2 * a + 1
# e = a ** 2 + np.sin(a) + 1

# c = interp1d(a, b)
# d = c(np.arange(2.1, 3, 0.1))
# print(d)

# f = UnivariateSpline(a, e)
# g = f(np.arange(2.1, 3, 0.1))
# print(g)

# h = Rbf(a, e)
# i = h(np.arange(2.1, 3, 0.1))
# print(i)

import numpy as np
from scipy.stats import ttest_ind, kstest, describe, skew, kurtosis, normaltest

a = np.random.normal(size=100)
b = np.random.normal(size=100)
c = ttest_ind(a, b)
print(c)

# d = ttest_ind(a, b).pvalue
# print(d)

d = kstest(a, 'norm')
print(d)

e = describe(a)
print(e)

print(skew(a))
print(kurtosis(a))

print(normaltest(a))