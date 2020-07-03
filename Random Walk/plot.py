import numpy as np
import matplotlib.pyplot as plt
if __name__=='__main__':
	V = np.load('TrueValueFunction.npy')
	plt.plot(range(1,1001),V[1:])
	V = np.load('Random_walk.npy')
	plt.plot(V[1:])
	plt.xlabel('State')
	plt.ylabel('Value')
	plt.show()
	