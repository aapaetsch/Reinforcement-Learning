#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian
  Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
 
  agent does *no* learning, selects actions randomly from the set of legal actions
 
"""
'''
Aidan Paetsch
1460103
W1_agent
'''

from utils import rand_in_range, rand_un
import numpy as np

last_action = None # last_action: NumPy array

num_actions = 10
first_run = True

def agent_init():
    global last_action, est_values, e
    last_action = np.zeros(1,dtype='int32') # generates a NumPy array with size 1 equal to zero
    if first_run == False:
        est_values = np.full(num_actions,5.0)
        e = 0
    else:
        e = 0.1
        est_values = np.zeros(num_actions)

def agent_start(this_observation): # returns NumPy array, this_observation: NumPy array
    global last_action
    last_action[0] = rand_in_range(num_actions)

    local_action = np.zeros(1,dtype='int32')
    local_action[0] = rand_in_range(num_actions)

    return local_action


def agent_step(reward, this_observation): # returns NumPy array, reward: floating point, this_observation: NumPy array
    global last_action, e, est_values, first_run, local_action
    local_action = np.zeros(1,dtype='int32')

    if np.random.random() > e:
        value = np.amax(est_values)
        maxi = np.where(est_values== value)[0]
        maxi = np.random.choice(maxi)
        local_action[0] = maxi

    else:
        local_action[0] = rand_in_range(10)

    est_values[last_action[0]] = est_values[last_action[0]]+0.1 * (reward - est_values[last_action[0]])
    last_action = local_action
    # might do some learning here
    return last_action

def agent_end(reward): # reward: floating point
    # final learning update at end of episode
    return

def agent_cleanup():
    # clean up
    est_values=np.zeros(num_actions)
    last_action = np.zeros(1,dtype='int32')
    local_action = np.zeros(1,dtype='int32')
    return

def agent_message(inMessage): # returns string, inMessage: string
    # might be useful to get information from the agent
    global first_run
    if inMessage == "what is your name?":
        return "my name is skeleton_agent!"
    elif inMessage == 'mode':
        first_run = False

    # else
    return "I don't know how to respond to your message"
