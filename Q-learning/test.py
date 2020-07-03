import os
import random
import time


alpha = 0.5
epsilon = 0.1


width = 10
grid = {
	'w' : width,
	'h' : 7
}
action_range = 8
wind = [0]*width
actions = ['w','a','d','x','e','q','z','c','s']

goal = {
	'x' : 7, 'y' : 3
}
wind[6] = 2
wind[8] = 1
wind[5] = 1
wind[4] = 1
wind[3] = 1
wind[7] = 2

agent = {
	'pos' : {
		'x' : 0,
		'y' : 0,
	},
	'oldpos' : {
		'x' : 0,
		'y' : 0,
	},
	'initpos' : {
		'x' : 0,
		'y' : 3,
	},
	'q' : [[[0 for i in range(action_range)] for j in range(grid['w'])] for k in range(grid['h'])], 
	
	
	
	'oldaction' : 0,
	'currentaction' : 0
	
}




def AI_dumb(n):
	return actions[int(random.random()*n)]
	
def agentUpdate(r):
	y = agent['pos']['y']
	x = agent['pos']['x']
	oy = agent['oldpos']['y']
	ox = agent['oldpos']['x']
	a = agent['currentaction']
	oa = agent['oldaction']
	Q = agent['q']
	Q[oy][ox][oa] += alpha*(r + Q[y][x][a] - Q[oy][ox][oa])
	#print(Q[oy][ox])
	
	


	

	

	
def envGetMove(n):
	if n == actions.index('s'):
		return (0, windAction(0))
	if n == actions.index('a'):
		return (-1, windAction(0))
	if n == actions.index('d'):
		return (1, windAction(0))
	if n == actions.index('x'):
		return (0, windAction(1))
	if n == actions.index('w'):
		return (0, windAction(-1))
	if n == actions.index('q'):
		return (-1, windAction(-1))
	if n == actions.index('e'):
		return (1, windAction(-1))
	if n == actions.index('z'):
		return (-1, windAction(1))
	if n == actions.index('c'):
		return (1, windAction(1))
		
def envGetNewPos(n):
	x, y = envGetMove(n)
	nx = agent['pos']['x'] + x
	ny = agent['pos']['y'] + y
	if(nx < 0):
		nx = 0
	elif (nx >= grid['w']):
		nx = grid['w'] - 1
	if(ny < -0):
		ny = 0
	elif (ny >= grid['h']):
		ny = grid['h'] - 1
		
	
	return (nx, ny)
	
		
		
def agentPrint():
	os.system('cls')
	print(bordh)
	for i in range(grid['h']):
		for j in range(grid['w']):
			if j == 0:
				print('+ ', end='')
			if(i == agent['pos']['y'] and j == agent['pos']['x']):
				print('@ ', end='')
			elif(i == goal['y'] and j == goal['x']):
				print('$ ', end='')
			else:
				print('. ', end='')
			if j == grid['w'] - 1:
				print('+ ', end='')
		print()
	print(bordh)
	print(end = '  ')
	for i in range(len(wind)):
		print('%d '%wind[i],end='')
	print()
		
def windAction(y):
	ax = agent['pos']['x']
	return   y - wind[ax]

def agentStart(s):
	agent['pos']['x'] = s['x']
	agent['pos']['y'] = s['y']
	n = agentChoose()
	agent['currentaction'] = n
	return n
	
def agentChoose(rand = False):
	y = agent['pos']['y']
	x = agent['pos']['x']
	A = agent['q'][y][x]
	if(random.random() > epsilon and rand == False):
		return A.index(max(A))
	else:
		return int(random.random()*action_range)
	
def agentStep(s, r):
	agent['oldpos']['x'] = agent['pos']['x']
	agent['oldpos']['y'] = agent['pos']['y']
	agent['pos']['x'] = s['x']
	agent['pos']['y'] = s['y']
	n = agentChoose()
	agent['oldaction'] = agent['currentaction']
	agent['currentaction'] = n
	agentUpdate(r)
	return n

def agentEnd(s, r):
	agent['oldpos']['x'] = agent['pos']['x']
	agent['oldpos']['y'] = agent['pos']['y']
	agent['pos']['x'] = s['x']
	agent['pos']['y'] = s['y']
	agent['oldaction'] = agent['currentaction']
	agent['currentaction'] = 0
	agentUpdate(r)

	
	
	
	
def win(s):
	return s['x'] == goal['x'] and s['y'] == goal['y']

steps = 1
bordh = '+'*((grid['w']+2)*2-1)
def main():
	global steps
	R = -1
	ep = 1
	ss = 0
	qwe = 10
	while 1:
		n = agentStart(agent['initpos'])
		k = 1
		isKey = ep%qwe==0
		if isKey:
			qwe *= 2
		while 1:
			steps = k
			if isKey: agentPrint()
			#n = input('Enter WSAD >> ').lower()
			#if n == '': n = AI_dumb()
			x,y = envGetNewPos(n)
			s = {'x' : x, 'y' : y}
			if win(s):
				agentEnd(s, 0)
				ss += k
				if isKey: 
					agentPrint()
					print('You Won! (eps : {} | steps : {} | avg : {})'.format(ep, k, ss/ep))
					time.sleep(2)
				else:
					print('You Won! (eps : {} | steps : {} | avg : {})'.format(ep, k, ss/ep))
				break
			n = agentStep(s, -1)
			if isKey: 
				print('eps : {} | steps : {}'.format(ep, k))
				time.sleep(0.01)
			k += 1
		ep += 1
	
main()



