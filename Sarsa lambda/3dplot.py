import os
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 


filename = 'value.npy'
if os.path.exists(filename):
	x,y,z= np.load(filename)

	fig = plt.figure(0)
	fig.suptitle("Cost to go fxn for 1000 episodes")
	ax = fig.add_subplot(111,projection="3d")

	ax.plot_wireframe(x,y,z, cstride=1,rstride=1)
	ax.set_xlabel('Position')
	ax.set_ylabel('Velocity')
	plt.show()