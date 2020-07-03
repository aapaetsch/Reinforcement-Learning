from utils import rand_in_range, rand_un
import numpy as np
movement = None
old_state = np.zeros(2, dtype=np.uint32)
def agent_init():
	global Q, e, a
	Q = np.zeros((10,7,movement))
	e = 0.1
	a = 0.5

	
def agent_start(state):
	global old_action, old_state
	action =np.argmax(Q[state[0]][state[1]])
	old_action = action
	old_state[0] = state[0]
	old_state[1] = state[1]
	return action

def agent_step(reward, state):
	global old_action, old_state
	if rand_un() < e:
		action = rand_in_range(movement)
	else:
		action = np.argmax(Q[state[0]][state[1]])
	Q[old_state[0]][old_state[1]][old_action] += a*(reward+Q[state[0]][state[1]][action]-Q[old_state[0]][old_state[1]][old_action]) 
	old_state[0] = state[0]
	old_state[1] = state[1]
	old_action = action
	return action

def agent_end(reward):
	return

def agent_cleanup():
	return

def agent_message(in_message):
	global movement
	if (in_message == '4'):
		movement = 4
		return
	elif (in_message == '8'):
		movement = 8
		return
	elif (in_message == '9'):
		movement = 9
		return
	else:
		return "I don't know what to return!!"