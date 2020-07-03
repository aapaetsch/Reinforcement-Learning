from rl_glue import *
RLGlue("windygrid_env","windygrid_agent")

import numpy as np
import pickle

if __name__=="__main__":
	num_episodes = 170
	max_steps = 8000
	movements = []
	for i in [4,8,9]:
		RL_agent_message(str(i))
		RL_init()
		RL_episode(0)
		steps = np.asarray([RL_num_steps()])
		while steps[-1]<max_steps:
			RL_episode(0)
			steps = np.append(steps,[RL_num_steps()+steps[-1]])
		RL_cleanup()
		movements.append(steps)
	np.save("WindyGridWorld",movements)

