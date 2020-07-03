import matplotlib.pyplot as plt
import numpy as np
max_steps = 1000

optimal_action = np.zeros(max_steps)
optimal_action2 = np.zeros(max_steps)

with open('RL_EXP_OUT.dat','r') as f:
	file = list(f)
	for i in range(len(file)):
		optimal_action[i] = file[i]

with open('RL_EXP_OUT2.dat','r') as a:
	file2 = list(a)
	for i in range(len(file2)):
		optimal_action2[i] = file2[i]
print optimal_action2
print optimal_action


		


plt.plot(optimal_action*100, Label='Q1 = 0, epsilon = 0.1')
plt.plot(optimal_action2*100, Label='Q1 = 5, epsilon = 0')
plt.ylim(0,100)
   
plt.legend()

plt.xlabel('Number of Runs')
plt.ylabel('% Optimal Action')

plt.savefig("Optimal_Action_Graph.png")