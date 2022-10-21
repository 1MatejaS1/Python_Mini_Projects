import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import linregress
import numpy as np

x=np.array([10,22,32,43])
y=np.array([1.14,2.48,3.64,5.80])

slope, intercept, r_value, p_value, stderr = linregress(x, y)

plt.plot(x, y, 'o', label='Calculated Values')

m, b = np.polyfit(x, y, 1)

plt.plot(x, m*x + b, label='Fitted line')

plt.title('Acceleration as a product of incline angle')
plt.ylabel('Acceleration in meters per second squared')
plt.xlabel('Angles of incline in degrees')
plt.legend()
