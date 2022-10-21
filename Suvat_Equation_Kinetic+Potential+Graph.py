import matplotlib.pyplot as plt
import numpy as np
def SuvatEqn():
    m = int(input("Enter the mass: ")) #user input vary accordingly
    v0 = int(input("Enter the initial velocity: ")) #user input vary accordingly
    g = 9.81
    t = np.linspace(0,(2*v0)/g)
    y_t = v0*t - (0.5 * g * ((t**2)))
    v = v0 -g*t
    P = m*g*y_t
    K = (1/2)*m*(v**2)
    energy_Sum = P+K
    data = np.zeros((len(t),5))
    data[:,0] = t
    data[:,1] = y_t
    data[:,2] = v
    data[:,3] = P
    data[:,4] = K
    plt.plot(t,P, label = "Potential Energy")
    plt.plot(t,K, label = "Kinetic Energy")
    plt.plot(t,energy_Sum, label = "Energy Sum")
    plt.xlabel("Time [Seconds]", fontsize=14)
    plt.ylabel("Energy [Joules]", fontsize=14)
    max_value = np.max(energy_Sum)
    plt.ylim(0,1.3*max_value)
    plt.title("Kinetic and Potential Energy as a function of time", fontsize=19)
    plt.legend(loc="upper center")
    
SuvatEqn()
