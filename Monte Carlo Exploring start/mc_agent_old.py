#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
           for use on A3 of Reinforcement learning course University of Alberta Fall 2017
 
"""

from utils import rand_in_range, rand_un
import numpy as np
import pickle

def agent_init():
    global values, policy, e, states, ph, pre
    """
    Hint: Initialize the variables that need to be reset before each run begins
    Returns: nothing
    """
    #initialize the policy array in a smart way
    states = 101
    e = 0.9
    policy = np.ones(states)
    values = np.zeros(states)
    ph = np.zeros(2)
    pre = np.zeros(2)


def policy_create(pre, reward, state):
    global ph, values, policy
    pstate = int(pre[0])
    x = abs(state-pstate)
    problem_head = ph[0]/ph[1]
    pre_value = values[pstate]
    sm = (problem_head*(reward+values[pstate+x])+((1-problem_head)*(0+values[pstate-x])))
    if(float(sm)>pre_value):
        values[pstate] = sm
        policy[pstate] = pre[1]



def agent_start(state):
    global pre
    """
    Hint: Initialize the variavbles that you want to reset before starting a new episode
    Arguments: state: numpy array
    Returns: action: integer
    """
    # pick the first action, don't forget about exploring starts 
    action = 1+int(rand_un()*min(state,99-state+1))
    pre[0] = state
    pre[1] = action
    return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    global pre, policy, ph, e
    if int(state) > int(pre[0]):
        ph[0] += 1
    ph[1] += 1
    policy_create(pre, reward, state)
    
    if rand_un() > e:
        action = 1+int(rand_un()*min(state,99-state+1))
    else:
        action = int(policy[state])
    pre[0] = state
    pre[1] = action
    """
    Arguments: reward: floting point, state: integer
    Returns: action: integer
    """
    # select an action, based on Q
    return action

def agent_end(reward):
    global pre

    """
    Arguments: reward: floating point
    Returns: Nothing
    """
    # do learning and update pi
    policy_create(pre,reward, 100)
    return

def agent_cleanup():
    """
    This function is not used
    """
    # clean up
    return

def agent_message(in_message): # returns string, in_message: string
    global values
    """
    Arguments: in_message: string
    returns: The value function as a string.
    This function is complete. You do not need to add code here.
    """
    # should not need to modify this function. Modify at your own risk
    if (in_message == 'ValueFunction'):
        return pickle.dumps(values, protocol=0)
    else:
        return "I don't know what to return!!"

