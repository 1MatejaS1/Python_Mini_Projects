from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def linearfit(temp,m,c):
    return temp*m + c

temp = np.array([0.0, 25.0, 50.0, 75.0, 100.0, 125.0, 150.0, 175.0, 200.0, 225.0, 250.0])
length = np.array([1.1155, 1.1164, 1.117, 1.1172, 1.118, 1.119, 1.1199, 1.121, 1.1213, 1.1223, 1.1223])
error = [0.0003, 0.0003, 0.0003, 0.0003, 0.0003, 0.0003, 0.0003, 0.0015, 0.0012, 0.0011, 0.0011]

popt, pcov = curve_fit(linearfit, temp, length, sigma=error)

fitted_y = linearfit(temp, popt[0], popt[1])

fiterror = np.sqrt(np.diag(pcov))

slope = popt[0]
errorslope = fiterror[0]
intercept = popt[1]
errorinintercept = fiterror[1]

plt.errorbar(temp, length, yerr= error, fmt="none")
plt.plot(temp, length, "o")
plt.plot (temp, fitted_y )
