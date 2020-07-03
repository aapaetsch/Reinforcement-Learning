#!/usr/bin/env python

"""
 Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian, Zach Holland
 Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
"""

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
   	V = np.load('DynaQ2.npy')
   	plt.xlabel('alpha-value')
   	plt.ylabel('average steps per episode')
   	alpha = [0.03125,0.0625,0.125,0.25,0.5,1.0]

   	plt.plot(alpha,V,'-o')

   	plt.savefig('DynaQ2.png')
  	plt.show()

