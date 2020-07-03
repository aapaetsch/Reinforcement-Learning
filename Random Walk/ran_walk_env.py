from utils import rand_norm, rand_in_range, rand_un
import numpy as np
import os
import time
current_state = None

def env_init():
	global current_state
	current_state = 0

def env_start():
	global current_state
	current_state = 500
	return current_state

def env_step(action):
	global current_state
	reward = 0.0
	new_state = current_state+action
	is_terminal = False
	if (new_state >1000):
		is_terminal = True
		reward = 1.0
	elif (new_state < 1):
		is_terminal = True
		reward = -1.0
	current_state = new_state
	result = {'reward':reward,'state':current_state,'isTerminal':is_terminal}
	return result

def env_cleanup():
	return

def env_message(in_message):
	return ""