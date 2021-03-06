#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian
  Purpose: for use of Rienforcement learning course University of Alberta Fall 2017
  Last Modified by: Andrew Jacobsen, Victor Silva, Mohammad M. Ajallooeian
  Last Modified on: 16/9/2017

  Experiment runs 2000 runs, each 1000 steps, of an n-armed bandit problem
"""
'''
Aidan Paetsch
1460103
W1_exp
'''

from rl_glue import *  # Required for RL-Glue
RLGlue("w1_env", "w1_agent")

import numpy as np
import sys

def getOptimal():
    return int(RL_env_message("optimal"))
def set_mode():
    RL_agent_message('mode')
def set_env_mode():
    RL_env_message("mode")

def save_results(data, data_size, filename): # data: floating point, data_size: integer, filename: string
    with open(filename, "w") as data_file:
        for i in range(data_size):
            data_file.write("{0}\n".format(data[i]))

if __name__ == "__main__":
    num_runs = 2000
    max_steps = 1000

    # array to store the results of each step
    optimal_action = np.zeros(max_steps)
    optimal_action2 = np.zeros(max_steps)
    for k in range(num_runs):
        RL_init()
        RL_start()
        for i in range(max_steps):
            # RL_step returns (reward, state, action, is_terminal); we need only the
            # action in this problem
            action = RL_step()[2]
            optim = getOptimal()
            if action == optim:
                optimal_action[i] += 1
            '''
            check if action taken was optimal

            you need to get the optimal action; see the news/notices
            announcement on eClass for how to implement this
            '''
            # update your optimal action statistic here
        RL_cleanup()
    print "\nHalf way"
    for k in range(num_runs):
        set_mode()
        RL_init()
        RL_start()
        for i in range(max_steps):
            set_mode()
            action = RL_step()[2]
            optim = getOptimal()
            if action == optim:
                optimal_action2[i]+=1
        RL_cleanup()

    save_results(optimal_action / num_runs, max_steps, "RL_EXP_OUT.dat")
    save_results(optimal_action2 / num_runs, max_steps, "RL_EXP_OUT2.dat")
    print "\nDone"
