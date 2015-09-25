from __future__ import division
import random
from sys import exit

population_size=10
# toppop=2
best=[]
population=[]
population_prob=[]
children=[]
cf=0
no_queens=8
solved=no_queens-1
to_mutate_or_not_to_mutate=30
iterations=50000000
# generation=0
the_clash=False


#to initialize the initial population
def let_there_be_light():
	p=[]
	while len(p)<no_queens:
		while True:
			i = random.randrange(0,no_queens)
			if i not in p:
				p.append(i)
				break
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


def random_pick(some_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability: break
    return item


def find_cumulative_fitness(population):
	global cf
	cf=0
	for i in population:
		cf+=i[1]


##find_probability uses the fitness of each item and finds each of their probability 
def find_probability(population):
	global population_prob
	population_prob=[]
	for i in population:
		population_prob.append(i[1]/cf)

def fitness(p):
	global the_clash
	f=0
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
			


def mutate_pos_swap(p):
	pos1=random.randrange(0,no_queens)
	pos2=random.randrange(0,no_queens)
	p[pos1],p[pos2]=p[pos2],p[pos1]
	return p



# def mutate(p):
# 	no_of_mutations =random.randrange(1,3)
# 	# print "no of mutations=", no_of_mutations
# 	for i in range(0,no_of_mutations):
# 		# print "MUTATING!"
# 		mutation_point= random.randrange(0,len(p))
# 		# print mutation_point
# 		p[mutation_point]= random.randrange(0,no_queens)
# 		# print p
# 	return p



def crossover(p1,p2):
	global children
	global population
	global to_mutate_or_not_to_mutate
	global generation
	cp=random.randrange(0,len(p1))
	# print "cp=", cp
	child=p1[0:cp]+p2[cp:len(p2)]
	# mutation_probability=100000000000000			#change muatation probability soon
	# random.randrange(0,100)
	if random.randrange(0,100) >= to_mutate_or_not_to_mutate:
		# print "mp1=", mutation_probability
		child=mutate_pos_swap(child)
	fit=fitness(child)
	if fit != -100:
	# fit2=fitness(p2)
		print child, fit
	# print p2, fit2
		children.append([child,fit])
	if fit == solved:
		print "------------------------------------"
		print "Solution:",child 
		print "------------------------------------"
		exit()
	# children.append([p2,fit2])
	if len(children) == population_size:
		population.sort(key=lambda population:population[1], reverse=True)
		best.append(population[0])
		# best.sort(key=lambda best:best[1], reverse=True)
		population=children
		children=[]
		find_cumulative_fitness(population)
		find_probability(population)
		# to_mutate_or_not_to_mutate+=10
		# print "Slave becomes the master"

def main():
	global population
	for i in range(0,population_size):
		temp=let_there_be_light()
		fit=fitness(temp)
		population.append([temp,fit])
	find_cumulative_fitness(population)
	find_probability(population)
	# population.sort(key=lambda population:population[1], reverse=True)
	for i in range(0,iterations):
	# while True:
		p1=random_pick(population,population_prob)[0]
		p2=random_pick(population,population_prob)[0]
		crossover(p1, p2)  ##random_pick is a weighted random item picker.
		# print i, "-------------------------"
		# time.sleep(1)

if __name__ == "__main__":
    main()


