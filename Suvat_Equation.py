import numpy as np
def SuvatEqn():
    m = int(input("Enter the mass: "))
    v0 = int(input("Enter the initial velocity: "))
    g = 9.81
    t = []
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
    print(data)

SuvatEqn()
