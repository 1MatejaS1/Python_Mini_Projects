import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.tan(x)
y[:-1][np.diff(y) < 0] = np.nan
plt.grid()
plt.xlabel("x")
plt.ylabel("$tan(x)$")
plt.ylim(-10,10)
plt.xlim(-2 * np.pi, 2 * np.pi)
radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
radians = [n * np.pi for n in radian_multiples]
radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']
plt.xticks(radians, radian_labels)

plt.title("$y = tan(x)$", fontsize=14)
plt.plot(x, y)

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.show()
