import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.signal import find_peaks

filename = 'RawData3.csv'
data = np.genfromtxt(filename, delimiter =',', skip_header =1)
data_X = data[:,0]
data_Y = data[:,1]
maximum = max(data_Y)
minimum = min(data_Y)

print('Maximum recorded pressure was', maximum,', while minimum recorded pressure was',minimum,'.')
plt.plot(data[:,0], data[:,1])
plt.xlabel("Time in seconds")

plt.ylabel("Pressure in hPa")

plt.plot(data[:,0], poly1d_fn(data[:,0]), ':b', label="Linear Regression, Whole Data Set")

peaks, _ = find_peaks(y, distance=1)
plt.plot(data[peaks,0],data[peaks,1], "kX")

#perform linear regression with peaks to show error due to steps
slope, intercept, r_value, p_value, std_err = linregress(data[peaks,0],data[peaks,1])
coef = np.polyfit(data[peaks,0],data[peaks,1],1)
poly1d_fn2 = np.poly1d(coef)

plt.plot(data[peaks,0], poly1d_fn2(data[peaks,0]), '-.r', label="Linear Regression, Peaks Only")

plt.legend(loc="lower left")

plt.xlabel("Time in seconds")

plt.ylabel("Pressure in hPa")
