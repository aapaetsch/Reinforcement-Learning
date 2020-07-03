from utils import rand_in_range, rand_un
import numpy as np
total_states = 1000
w = None
g = 1
a = 0.1
old_state = None
p = None

def agent_init():
	global w
	w = np.zeros(10)


def agent_start(state):
	global old_state
	old_state = state - 1
	action = action_rand()
	return action

def agent_step(reward, state):
	global old_state
	#update weight
	w_update(reward,state-1,False)
	old_state= state-1
	action = action_rand()
	return action

def agent_end(reward):
	global p
	w_update(reward,0,True)

	return

def w_update(r,state,isterminal):
	global w 

	if isterminal: 
		x = 0
	else: 
		x = w[state/100]
	y = w[old_state/100]
	w[old_state/100] += a*(r+g*x-y)

def action_rand():
	action = rand_in_range(200)-99
	if action == 0:
		action = -100
	return action

def agent_cleanup():
	return

def agent_message(in_message):
	global v
	if in_message == 'value':
		
		return w


	return ""

#tile(iht,num_tilings, [(state/num_states)/tile_width])