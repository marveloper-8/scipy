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

import numpy as np
from scipy.sparse.csgraph import connected_components, dijkstra
from scipy.sparse import csr_matrix

a = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])
b = csr_matrix(a)

print(connected_components(b))
print(dijkstra(b, return_predecessors=True, indices=0))
