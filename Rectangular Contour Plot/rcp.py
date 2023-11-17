import numpy as np
import matplotlib.pyplot as plt

def func(x, y):
    return np.sin(x)**2 + np.cos(y)**2

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)

x,y = np.meshgrid(x, y)
z = func(x, y)

plt.contour(x, y, z, cmap="gist_rainbow_r")
plt.show()