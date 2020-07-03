from utils import rand_norm, rand_in_range, rand_un
import numpy as np
import os
import time
current_state = None
world = None
wind = None

def env_init():
	global current_state, world, block, goal, step
	current_state = np.zeros(2,dtype=np.uint32)
	world = np.array([9,6],dtype=np.uint32)
	block = [[2,1],[2,2],[2,3],[5,4],[7,0],[7,1],[7,2]]#blocks in the world
	goal = np.array([8,0], dtype=np.uint32)
	step = 0

def env_start():
	global current_state, world
	current_state[0] = 0
	current_state[1] = 2
	return current_state

def get_move(move):
	if move == 0:#W
		return (0,-1)
	elif move == 1:#a
		return (-1,0)
	elif move == 2:#d
		return (1,0)
	elif move == 3:#x
		return (0,1)

def get_state(move):
	x,y = get_move(move)
	x = x+current_state[0]
	y = y+current_state[1]
	if [x,y] in block:
		return current_state[0],current_state[1]
	else:
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
	reward = 0
	is_terminal = False
	if (current_state == goal).all():
		is_terminal = True
		reward = 1
	result = {'reward':reward,'state':current_state,'isTerminal':is_terminal}
	return result

def env_cleanup():
	return

def env_message(in_message):
	return ""