from utils import rand_in_range, rand_un
import numpy as np

def agent_init():
	global Q, e, a, old_state, old_action, model, g, n, visited
	Q = np.zeros((9,6,4))
	e = 0.1
	a = None
	g = 0.95
	model = np.zeros((9,6,4,3),dtype=np.int32)
	old_action = 0
	old_state = np.zeros(2, dtype=np.int32)
	visited = []
	n = None

	
def agent_start(state):
	global old_action, old_state
	#chose an action
	action = action_select(state)
	#setting old state and action
	old_action = action
	old_state[0] = state[0]
	old_state[1] = state[1]
	#adding to visited
	visited.append([[state[0],state[1]], action])
	return action

def action_select(s):
	if rand_un() < e:
		#explore
		return rand_in_range(4)
	else:
		#decide action based on policy
		return np.random.choice(np.where(Q[s[0]][s[1]]==np.amax(Q[s[0]][s[1]]))[0])

def agent_step(reward, state):
	global old_action, old_state, Q, old_action,a
	# chose action e greedy
	action = action_select(state)
	old0,old1 = old_state[0], old_state[1]
	gamma_Q = g*np.amax(Q[state[0]][state[1]])
	#updating Q
	Q[old0][old1][old_action]+= a*(reward+gamma_Q-Q[old0][old1][old_action])
	#updating the model
	model[old0][old1][old_action] = np.array([state[0],state[1],int(reward)])
	if n != 0:
		for i in range(n):
			rs = visited[rand_in_range(len(visited))]
			xyr = model[rs[0][0]][rs[0][1]][rs[1]]
			Q[rs[0][0]][rs[0][1]][rs[1]] += a*(xyr[2]+(g*np.amax(Q[xyr[0]][xyr[1]]))-Q[rs[0][0]][rs[0][1]][rs[1]])
	#updating old action and state
	old_action = action
	old_state[0] = state[0]
	old_state[1] = state[1]
	#updating visited if not already visited
	visit = [[state[0],state[1]],action]
	if visit not in visited:
		visited.append(visit)
	# update old action and state
	return action

def agent_end(reward):
	global a
	old0 = old_state[0]
	old1 = old_state[1]
	Q[old0][old1][old_action]+= a*(reward-Q[old0][old1][old_action])
	model[old0][old1][old_action][2] = int(reward)
	return

def agent_cleanup():
	return

def agent_message(in_message):
	global n, a
	n,a = in_message
	return ""