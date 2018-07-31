import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig,ax= plt.subplots()

x_set= np.linspace(1,2000,2000)
ax.set_xlim([-200,200])
ax.set_ylim([0,50000])

def x_to_y(a):
	x=np.array(a)
	return x*x

#ax.plot(x_set, x_to_y(x_set),'+r', markersize=1)
ax.plot(x_set, np.log(x_set), '+r', markersize=1)
plt.show()