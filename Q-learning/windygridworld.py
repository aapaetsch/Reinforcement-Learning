import random
class Gridworld:
	def __init__(self):
		self.world = [['-']*10 for i in range(7)]
		self.wind=[0,0,0,1,1,1,2,2,1,0]
		self.world[3][7] = 'g'
		self.start = [3,0]
		self.goal = [3,7]
		self.position = [3,0]

	def p(self):

		str_repr = ''
		for i in self.world:
			str_repr+='|'
			for j in i:
				str_repr+= j+'|'
			str_repr+='\n'
		for i in self.wind:
			str_repr+=' '+str(i)
		print str_repr

	def starting(self):
		self.world[3][0] = '@'
#0 left and up
#1 up
#2 right and up
#3 left
#4 stay
#5 right
#6 left and down
#7 down
#8 right and down

def AI_dumb(valid):
	s = random.choice(valid)
	if s == 0:
		pass
	elif s == 1:
		pass
	elif s == 2:
		pass
	elif s == 3:
		pass
	elif s == 4:
		pass
	elif s == 5:
		pass
	elif s == 6:
		pass
	elif s == 7:
		pass
	elif s == 8:
		pass
	return 


def main():
	g = Gridworld()
	g.starting()
	g.p()
	while g.position != g.goal:




main()