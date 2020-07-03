import numpy as np
import matplotlib.pyplot as plt
if __name__=='__main__':
	
	V = np.load('rmse2.npy')
	plt.plot(V[1:],label='Agent 2')
	V=np.load('rmse3.npy')
	plt.plot(V[1:],label = 'Agent 3')
	V = np.load('rmse1.npy')
	plt.plot(V[1:],label='Agent 1')
	plt.xlabel('episodes')
	plt.ylabel('RMSE')
	plt.legend()
	plt.savefig('RMSE Graph.png')
	plt.show()
	