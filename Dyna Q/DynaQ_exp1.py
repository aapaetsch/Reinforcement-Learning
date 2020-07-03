from rl_glue import *
RLGlue("DynaQ_env","DynaQ_agent")

import numpy as np
import pickle
import time
if __name__=="__main__":
	num_episodes = 50
	num_runs = 10
	#list of planning steps
	n = [0,5,50]
	steps = np.zeros((3,num_episodes,num_runs))
	for x in range(3):
		#setting random seed for each set of runs
		
		for i in range(num_runs):
			np.random.seed(i)
			RL_init()
			#passing planning steps to agent
			RL_agent_message([n[x],0.5])
			for j in range(num_episodes):
				RL_episode(0)
				#updating steps for episode
				steps[x][j][i] = RL_num_steps()

				# if(j%10 == 0):
					# print 'Run: {}| Episodes: {} | steps: {}'.format(i,j,steps[x][j][i])
	np.save('DynaQ', np.mean(steps,2))