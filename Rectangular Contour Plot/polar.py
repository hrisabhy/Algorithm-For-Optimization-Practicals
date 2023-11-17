import numpy as np
import matplotlib.pyplot as plt

radian_arr = np.radians(np.linspace(0, 360, 20))
r_arr = np.arange(0, 1, 0.1)

def func(r, theta):
    return r*np.sin(theta)

r, theta = np.meshgrid(r_arr, radian_arr)
values = func(r, theta)
fig,ax=plt.subplots(subplot_kw=dict(projection='polar'))
ax.contourf(theta,r,values,cmp='Spectral_r')
plt.show()