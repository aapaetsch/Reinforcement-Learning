from utils import rand_in_range, rand_un
import numpy as np
from tiles3 import *
import pickle
import random

memsize = 4096
num_tilings = 8
a = 0.1/num_tilings

lamb = 0.9
gamma = 1
iht = IHT(memsize)
num_actions = 3
w = np.random.rand((memsize))*-0.001
num_actions = 3
z = np.zeros((memsize))
old_action = None
old_state = None


def agent_init():
	global w, iht
	w = np.random.rand((memsize))*-0.001
	iht=IHT(memsize)


def agent_start(state):
	global z, old_state, old_action
	z = np.zeros((memsize))
	action = random.randint(0,2)
	old_action = action
	old_state = state
	return action

def get_tiles(pos,vel):
	one = tiles(iht, num_tilings,[8*pos/(0.5+1.2),8*vel/(0.07+0.07)],[0])
	two = tiles(iht, num_tilings,[8*pos/(0.5+1.2),8*vel/(0.07+0.07)],[1])
	three = tiles(iht, num_tilings,[8*pos/(0.5+1.2),8*vel/(0.07+0.07)],[2])
	return one,two,three

def agent_step(reward, state):
	global old_state,old_action,w,z
	error = reward
	old_til = tiles(iht,num_tilings,[8*old_state[0]/(0.5+1.2),8*old_state[1]/(0.07+0.07)],[old_action])
	error = error-np.sum(w[old_til])
	z[old_til] = 1

	one,two,three = get_tiles(state[0],state[1])
	d0 = np.sum(w[one])
	d1 = np.sum(w[two])
	d2 = np.sum(w[three])
	action = np.argmax((d0,d1,d2))

	til = tiles(iht,num_tilings,[8*state[0]/(0.5+1.2),8*state[1]/(0.07+0.07)],[action])
	error = error+np.sum(w[til])
	w = w+(a*error*z)
	z = gamma*lamb*z
	old_state = state
	old_action = action
	return action


def agent_end(reward):
	global w
	error = reward
	old_til = tiles(iht,num_tilings,[8*old_state[0]/(0.5+1.2),8*old_state[1]/(0.07+0.07)],[old_action])
	error = error-np.sum(w[old_til])
	z[old_til] = 1
	w = w+(a*error*z)
	return

def plot3D():
	pos_step = (0.5+1.2)/50
	vel_step = (0.07+0.07)/50
	x = np.arange(-1.2,0.5*pos_step,pos_step)
	y = np.arange(-0.07,0.07+vel_step,vel_step)
	size_of_array = x.size*y.size
	xa = np.zeros((size_of_array))
	ya = np.zeros((size_of_array))
	za = np.zeros((size_of_array))
	for i in range(x.size):
		for j in range(y.size):
			sz = j+i*y.size
			xa[sz] = x[i]
			ya[sz]= y[j]
			za[sz]= cost(x[i],y[j])
	return np.array((xa,ya,za))

def cost(x,y):
	c = []
	for i in range(num_actions):
		c.append(get_value(x,y,i))
	return -np.max(c)

def get_value(x,y,i):
	if x == 0.5:
		return 0.0
	return np.sum(w[tiles(iht,num_tilings,[8*x/(0.5+1.2),8*y/(0.07+0.07)],[i])])



def agent_cleanup():
	return

def agent_message(in_message):
	if (in_message == '3dplot'):
		return plot3D()

	return ""
