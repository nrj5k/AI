from __future__ import division
import random
from sys import exit
import math
import time

population_size=10
# toppop=2
best=[]
no_queens=8
solved=no_queens-1
iterations=5000
# generation=0
the_clash=False


T=35
T_min=0.000000000000001
cooling_factor=0.05
c=[]
fit=0



def let_there_be_light():
	p=[]
	while len(p)<no_queens:
		while True:
			i = random.randrange(0,no_queens)
			if i not in p:
				p.append(i)
				break
	return p


def neighbor(p):
	pos1=random.randrange(0,no_queens)
	pos2=random.randrange(0,no_queens)
	p[pos1],p[pos2]=p[pos2],p[pos1]
	return p

def clash_checker(Q1,Q2):
	global the_clash
	#print Q1, Q2
	if Q1==Q2:
		return 0
	#print Q1[0]-Q1[1]
	#print Q2[0]-Q2[1]
	if Q1[0]-Q1[1]==Q2[0]-Q2[1] or Q1[0]+Q1[1]== Q2[0]+Q2[1]:
		#print "Diagonal" , Q1, Q2
		the_clash=True
		return 0 
	elif Q1[1]==Q2[1]:
		the_clash=True
		return 0
	# elif Q1[0] == Q2[0]:
	# 	return -4
	else :
		return 0


def fitness(p):
	global the_clash
	f=0
	the_clash=False
	for i in p:
		if i in p[p.index(i)+1:len(p)]:
			return -100
	for i in range(0,len(p)-1):
		for j in range(i,len(p)):
			f+=clash_checker( [i,p[i]] , [j,p[j]] )
		if the_clash == False:
			#print "no clash"
			f+=1
		else:
			the_clash=False
	return f
			
def acceptance_probability(fit_new,fit,T):
	return math.e**((fit_new-fit)/T)



def main():
	global population
	global T, T_min, cooling_factor
	global c,fit
	c=let_there_be_light()
	fit=fitness(c)
	print c,fitness(c)
	while T> T_min:
		# print c, fit
		for i in range(0,iterations):
			c_new=neighbor(c)
			# fit_new=fitness(c_new)
			
			if fitness(c_new) > fitness(c):
				c=c_new

			elif acceptance_probability(fitness(c), fitness(c_new), T)  > random.random():
				c=c_new
				# fit=fit_new
				# time.sleep(1)
				print T, c_new,fitness(c_new)
			# print i,c,fit,T
		T = T - cooling_factor
		if fitness(c) == solved:
			print "Solution:" , c, fitness(c)
			exit()



if __name__ == "__main__":
    main()
