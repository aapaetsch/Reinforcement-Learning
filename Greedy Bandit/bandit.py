import numpy as np

class Bandit:
	def __init__(self):
		self.arm_values = np.random.normal(0,1,10)
		self.k = np.zeros(10)
		self.est_values = np.zeros(10)

	def get_reward(self, action):
		noise = np.random.normal(0,1)
		reward = self.arm_values[action] + noise 
		return reward

	def choose_eps_greedy(self, epsilon):
		rand_num = np.random.random()
		if epsilon > rand_num:
			return np.random.randint(10)
		else:
			return np.argmax(self.est_values)

	def update_est(self, action, reward):
		self.k[action] += 1
		alpha = 0.1
		self.est_values[action] += alpha * (reward - self.est_values[action])

def experiment(bandit, Npulls, epsilon):
	history = []
	for i in range(Npulls):
		action = bandit.choose_eps_greedy(epsilon)
		R = bandit.get_reward(action)
		bandit.update_est(action, R)
		history.append(R)
	return np.array(history)

Nexp = 2000
Npulls = 1000
avg_outcome_eps0p0 = np.zeros(Npulls)
avg_outcome_eps0p1 = np.zeros(Npulls)

for i in range(Nexp):
	bandit = Bandit()
	avg_outcome_eps0p0 += experiment(bandit, Npulls, 0.0)

	bandit = Bandit() 
	avg_outcome_eps0p1 += experiment(bandit,Npulls,0.1)

avg_outcome_eps0p0 /= np.float(Nexp)
avg_outcome_eps0p1 /= np.float(Nexp)

import matplotlib.pyplot as plt

plt.plot(avg_outcome_eps0p0, label="eps = 0.0")
plt.plot(avg_outcome_eps0p1, label="eps = 0.1")
plt.ylim(0,2.2)
plt.legend()
plt.show()