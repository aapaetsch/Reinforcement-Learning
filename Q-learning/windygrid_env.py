
from utils import rand_norm, rand_in_range, rand_un
import numpy as np
current_state = None
world = None
wind = None

def env_init():
	global current_state, world, wind, goal
	current_state = np.zeros(2,dtype=np.uint32)
	world = np.array([10,7],dtype=np.uint32)
	wind = np.zeros(10, dtype=np.uint32)
	goal = np.array([7,3], dtype=np.uint32)
	for i in [3,4,5,8]:
		wind[i] = 1
	wind[6] = 2
	wind[7] = 2

def env_start():
	global current_state, world

	current_state[0] = 0
	current_state[1] = 3
	return current_state

def get_move(move):
	if move == 4:#Q = left up
		return (-1,-1)
	elif move == 0:#W
		return (0,-1)
	elif move == 5:#e
		return (1,-1)
	elif move == 1:#a
		return (-1,0)
	elif move == 2:#d
		return (1,0)
	elif move == 6:#z
		return (-1,1)
	elif move == 3:#x
		return (0,1)
	elif move == 7:#c
		return (1,1)
	elif move == 8:#s
		return (0,0)


def get_state(move):
	x,y = get_move(move)
	y = y+wind[current_state[0]]
	x = x+current_state[0]
	y = y+current_state[1]
	if x < 0:
		x = 0
	elif x >= world[0]:
		x = world[0]-1
	if y < 0:
		y = 0
	elif y >=world[1]:
		y = world[1]-1
	return x,y


def env_step(action):
	global current_state
	current_state[0],current_state[1] = get_state(action)
	reward = -1
	is_terminal = False
	if (current_state == goal).all():
		is_terminal = True
		reward = 0
	result = {'reward':reward,'state':current_state,'isTerminal':is_terminal}

	return result

def env_cleanup():
	return

def env_message(in_message):
	return ""