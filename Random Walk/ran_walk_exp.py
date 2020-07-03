from rl_glue import *
from rndmwalk_policy_evaluation import *
agent = input('Enter the agent number: ')
RLGlue("ran_walk_env","ran_walk_agent%s"%str(agent))

import numpy as np
import pickle
import time
import math

if __name__=="__main__":
	num_episodes = 2000
	num_runs = 10
	t_states = 1000
	#list of planning steps
	V = np.zeros((num_runs,t_states))
	rmse = np.zeros(num_episodes)
	G=np.load("TrueValueFunction.npy")
	if agent == 3:
		a1 = np.sum(G[1:101])/100
		a2 = np.sum(G[101:201])/100
		a3 = np.sum(G[201:301])/100
		a4 = np.sum(G[301:401])/100
		a5 = np.sum(G[401:501])/100
		a6 = np.sum(G[501:601])/100
		a7 = np.sum(G[601:701])/100
		a8 = np.sum(G[701:801])/100
		a9 = np.sum(G[801:901])/100
		a10 = np.sum(G[901:1001])/100
		a = np.array([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10])
	for x in range(num_runs):
		#setting random seed for each set of runs
		np.random.seed(x)
		RL_init()
		for i in range(num_episodes):
			if i %100 == 0:#included as to show where in the runs the program is
				print x,i
			#passing planning steps to agent
			RL_episode(0)
			vector = RL_agent_message('value')
			if agent == 3:
				rmse[i] += np.sqrt(np.mean(np.power(a-vector,2)))

			else:

				rmse[i] += np.sqrt(np.mean(np.power(G[1:]-vector,2)))
		vector = RL_agent_message('value')
		for i in range(len(vector)):
			V[x][i] = vector[i]

	for i in range(t_states):
		rmse[i] = float(rmse[i]) /num_runs
	np.save('rmse%s'%str(agent),rmse)