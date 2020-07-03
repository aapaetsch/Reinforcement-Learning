from utils import rand_in_range, rand_un
import numpy as np
from tiles3 import tiles, IHT
total_states = 1000
w = None
a = 0.01/50
tile_width = 0.2
old_vector = None
old_state = None
num_tilings = 50
iht = None

def agent_init():
	global w, iht
	w = np.zeros(total_states)
	iht = IHT(total_states)

def agent_start(state):
	global old_vector,old_state
	old_vector = get_vector(state-1)
	old_state = state-1
	action = action_rand()
	return action

def agent_step(reward, state):
	global old_vector,old_state
	#update weight
	s = state-1
	w_update(reward,s,False)
	old_state = s
	action = action_rand()
	return action

def agent_end(reward):
	w_update(reward,0,True)
	return


def w_update(reward,s,is_terminal):
	global w, old_vector
	vector = get_vector(s)
	if is_terminal:
		x = 0.0
	else:
		x = np.dot(vector,w)
	y = np.dot(old_vector,w)
	w = w+(old_vector*(a*(reward+x-y)))
	old_vector = vector

def get_vector(state):
	#print state
	t = tiles(iht,num_tilings,[float(state)/200])
	vector = np.zeros(total_states)
	for i in t:
		vector[i] = 1.0
	return vector

def action_rand():
	action = rand_in_range(200)-99
	if action == 0:
		action = -100
	return action

def agent_cleanup():
	return

def agent_message(in_message):
	if in_message == 'value':
		return w
	return ""

#tile(iht,num_tilings, [(state/num_states)/tile_width])