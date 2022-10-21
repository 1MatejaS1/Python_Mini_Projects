import numpy as np
import matplotlib.pyplot as plt
filename1 = 'eee123.csv' #import your file here :)
filename2 = 'gain.csv' #import your file here :)
data1 = np.genfromtxt(filename1, delimiter =',', skip_header =0)
data1_X = data1[:,0]
data1_Y = data1[:,3]
data2 = np.genfromtxt(filename2, delimiter =',', skip_header =0)
data2_X = data2[:,0]
data2_Y = data2[:,3]
fig = plt.figure()
ax = fig.gca()
ax.set_xticks(np.arange(0, 61, 5))
ax.set_yticks(np.arange(0, 101., 5))

plt.plot(data1[:,0], data1[:,3], 'r', label = '-100 gain')
plt.plot(data1[:,0], data1[:,3], 'rX', label = 'measured -100 gain')
plt.plot(21.8, 70.7, 'go', label = '-100 gain bandwidth')
plt.axhline(y=70.7, color='g', linestyle='dotted')
plt.axvline(x=21.8, color='g', linestyle='dotted')

plt.plot(data2[:,0], data2[:,3], 'b', label = '-50 gain')
plt.plot(data2[:,0], data2[:,3], 'bX', label = 'measured -50 gain')
plt.plot(47.75, 35.35, 'mo', label = '-50 gain bandwidth')
plt.axhline(y=35.35, color='m', linestyle='dotted')
plt.axvline(x=47.75, color='m', linestyle='dotted')

plt.xlabel("Input frequency in kHz", fontsize=14)

plt.ylabel("Measured Gain", fontsize=14)

plt.title("Inverting Amplifier Gain with frequency", fontsize=19)

plt.legend(loc="upper right")

plt.grid()
plt.show()
plt.savefig('Graph.png')
