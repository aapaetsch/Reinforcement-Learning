#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
   	V = np.load('DynaQ.npy')
   	plt.xlabel('Episodes')
   	plt.ylabel('steps')
   	n = [0,5,50]
   	for i in range(len(V)):

   		plt.plot(V[i][2:],Label="planning steps = "+str(n[i]))
   	plt.legend()
   	plt.savefig('DynaQ.png')
  	plt.show()

