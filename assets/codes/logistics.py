# exercise 3.2.4
# you can run this using GoogleColab or any other Python compiler
import numpy as np
import matplotlib.pyplot as plt

yrs = np.linspace(1790, 1950, 17)
pop = [3.929, 5.308, 7.240, 9.638, 12.866, 17.069,  23.192,
       31.433, 38.558, 50.156, 62.948,  75.996,  91.972, 105.711,
       122.775, 131.669, 150.697]
P0 = 3.929
a = 0.0313395
b = 0.000158863
population = lambda t: a / (b  + (a / P0 - b) * np.exp( - a * (t - 1790)))
t = np.linspace(1790, 2025, 200)
plt.plot(t, population(t), color = 'red')
plt.scatter(yrs, pop)
plt.show()
abs_errs = np.abs(pop - population(yrs))
plt.scatter(yrs, abs_errs, label = 'absolute error (mil)')
rel_errs = np.abs(pop - population(yrs)) / pop * 100
plt.scatter(yrs, rel_errs, label = 'relative error (%)')
plt.legend()
plt.show()