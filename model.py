# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import statements
import random
import operator
import matplotlib.pyplot

import agentframework

#definition declaration of functions

def distance_between(agent0, agent1):
    return (((agent0.x-agent0.x)**2) + ((agent1.y-agent1.y)**2)**0.5)

#This states how many agents we want to create
num_of_agents = 10
num_of_iterations = 100

# lists 
agents =[] #this is an empty list

# randomly make agents

for i in range(num_of_agents):
    agents.append(agentframework.Agent())

#move agents 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
    

#plot the agents using matplotlib.pyplot
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    # colour the agent furthest east a different color
    #m = max(agents, key=operator.itemgetter(1))
    #matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()


