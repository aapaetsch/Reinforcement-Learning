from rl_glue import *
RLGlue("DynaQ_env","DynaQ_agent")

import numpy as np
import pickle
import time
if __name__=="__main__":
	num_episodes = 50
	num_runs = 10
	#list of planning steps
	alpha = [0.03125,0.0625,0.125,0.25,0.5,1.0]
	steps = np.zeros((6,1,num_episodes,num_runs))
	n = 5
	for x in range(6):
		#setting random seed for each set of runs
		
		for i in range(num_runs):
			np.random.seed(i)
			RL_init()
			#passing planning steps to agent
			RL_agent_message([5,alpha[x]])
			for j in range(num_episodes):
				RL_episode(0)
				#updating steps for episode
				steps[x][0][j][i] = RL_num_steps()

				#if(j%10 == 0):
					#print 'Run: {}| Episodes: {} | steps: {}'.format(i,j,steps[x][j][i])
	a = np.mean(np.mean(steps,3),2)


	np.save('DynaQ2', a)