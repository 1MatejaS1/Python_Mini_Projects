import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

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

fs = 1 /(np.mean(np.diff(data_X)))
from scipy.signal import butter,filtfilt
# Filter requirements.
cutoff = .25      # desired cutoff frequency of the filter, Hz ,
order = 10

def butter_lowpass_filter(data, cutoff, fs, order):
    normal_cutoff = cutoff / 2.3 #Nyquest limit
    # Get the filter coefficients
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y
  
slope, intercept, r_value, p_value, std_err = linregress(data[:,0],data[:,1])
coef = np.polyfit(data[:,0],data[:,1],1)
poly1d_fn = np.poly1d(coef)
plt.plot(data[:,0],data[:,1], 'yo', data[:,0], poly1d_fn(data[:,0]), '--k')
plt.xlabel("Time in seconds")

plt.ylabel("Pressure in hPa")
plt.plot(y, label='Lowpass Filter')
plt.legend(loc="lower left")





