import matplotlib.pyplot as plt
import numpy as np
def Wave_Eqn(x, y):
    L = 1
    n_x = 1
    n_y = 2
    Wave_Eqn = (2/L)*(np.sin((np.pi*n_x*x)/L))*(np.sin((np.pi*n_y*y)/L))
    return Wave_Ewn

fig = plt.figure()
e = 200 #points between min and max
x = np.linspace(0,1,e) #1D array 0 to 1
y = np.linspace(0,1,e) #1D array 0 to 1
X, Y = np.meshgrid(x, y) #mesh from x and y
Z = func(X, Y) #Z as a function of x and y

ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, Z)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z");

plt.contour(X, Y, Z) #contour plot of the same data
