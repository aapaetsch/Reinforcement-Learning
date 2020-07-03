#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
           for use on A3 of Reinforcement learning course University of Alberta Fall 2017
 
"""
'''
Aidan Paetsch
paetsch@ualberta.ca
Cmpt 366
Assignment:3
Question:2
Part:2 
'''
from utils import rand_in_range, rand_un
import numpy as np
import pickle


def agent_init():
    global pi, Q, ep
    """
    Hint: Initialize the variables that need to be reset before each run begins
    Returns: nothing
    """
    #initialize the policy array in a smart way
    states = 101
    pi = np.zeros(states,dtype=np.int8)#policy array
    Q = np.zeros((states,states))
    for s in range(states):
        pi[s] = min(s,states-1-s)
        Q[100][s] = 1
    ep = np.zeros((100,2),dtype=np.int32)#2D array for episodes



def agent_start(state):
    global pi, ep
    """
    Hint: Initialize the variavbles that you want to reset before starting a new episode
    Arguments: state: numpy array
    Returns: action: integer
    """
    # pick the first action, don't forget about exploring starts 
    action = pi[int(state[0])]
    ep[0][0] = int(state[0])
    return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    global ep
    """
    Arguments: reward: floting point, state: integer
    Returns: action: integer
    """
    # select an action, based on Q
    action = pi[state[0]]
    if int(state[0]) > ep[0][0]:
        x = 1
    else:
        x = 0
    ep[ep[0][0]][x]+=1
    ep[0][0]=int(state[0])
    return action

def agent_end(reward):
    global pi,ep,Q
    """
    Arguments: reward: floating point
    Returns: Nothing
    """
    # do learning and update pi
    if reward > 0:
        x = 1
    else:
        x = 0
    ep[ep[0][0]][x]+=1
    for state in range(1,100):
        count = ep[state][0]+ep[state][1]
        action = int(pi[state])
        prev = Q[state-action][pi[state-action]]
        newv = Q[state+action][pi[state+action]]
        sm = prev*ep[state][0]+newv*ep[state][1]
        if count !=0:
            Q[state][action]=(sm+0.0)/count
    for state in range(1,100):
        action = np.argmax(Q[state])
        if action!=0:
            pi[state] = action
        
    return

def agent_cleanup():
    """
    This function is not used
    """
    # clean up
    return

def agent_message(in_message): # returns string, in_message: string
    global Q
    """
    Arguments: in_message: string
    returns: The value function as a string.
    This function is complete. You do not need to add code here.
    """
    # should not need to modify this function. Modify at your own risk
    if (in_message == 'ValueFunction'):
        return pickle.dumps(np.max(Q,axis=1), protocol=0)
    else:
        return "I don't know what to return!!"

