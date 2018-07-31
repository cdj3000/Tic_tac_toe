import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()
plt.xlim(-10,10)
plt.ylim(-10,10)


def animate(i):
	circle=plt.Circle((0,0),i*0.05)
	ax.add_artist(circle)
def init():
	circle=plt.Circle((0,0),0.01)
	ax.add_artist(circle)
ani=animation.FuncAnimation(fig=fig, func=animate, frames=1000, init_func=init, interval=100, blit=False)



plt.show()

