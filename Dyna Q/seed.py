import numpy as np
import numpy.random as rnd
x = []
for i in range(3):
	np.random.seed(2)
	z = []
	for j in range(4):
		for k in range(3):
			z.append(rnd.uniform())
	x.append(z)

for i in x:
	print i
