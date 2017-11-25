# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import statements
import matplotlib.pyplot
import agentframework
import csv
import random

num_of_agents = 10
num_of_iterations = 100
neighborhood = 20
store = 0

# lists 
agents =[] #this is an empty list
environment=[]

# randomly make agents

for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    
#read data 

file = open("in.txt", newline='')

reader= csv.reader(file, quoting=csv.QUOTE.NONNUMERIC)
for row in reader:
#for each row in the file we create an empty row list
    rowlist=[]
#for each item in the rows we append the items to the rowlist
    for item in row:
        rowlist.append(item)
#we append the rowlist into the environment
    environment.append(rowlist)

#make agents move, eat and interact with neighbours
for j in range(num_of_iterations):
#randomise the way agents are picked for the iterations
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighborhood)

#plot the agents and environment using matplotlib.pyplot
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    # colour the agent furthest east a different color
    #m = max(agents, key=operator.itemgetter(1))
    #matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()


