# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import statements
import random
import operator
import matplotlib.pyplot

#This states how many agents we want to create
num_of_agents = 10
num_of_iterations = 100

# lists 
agents =[] #this is an empty list

# randomly generate agents. This is a loop that creates 10 random coordinates. 

for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

#this code appends random integers between 0 and 99 to the list [agents] created above. 
agents.append([random.randint(0,99),random.randint(0,99)])

print (agents)

# this loop moves all 10 points 100 times. the (%99) at the end of the code makes the agents stay in the 100x100 plane (Tarus Method).
for j in range(num_of_iterations):
    for i in range(num_of_agents):
    
        if random.random() < 0.5: 
            agents[i][0]+= 1 % 99
        else: 
            agents[i][0]-= 1 % 99
    
        if random.random() < 0.5: 
            agents[i][1]+= 1 % 99
        else: 
            agents[i][1]-= 1 % 99

print(agents)

# calculate the discance between the variables usign the Pythagorian theorem

#distance = ((agents[0][0]-agents[1][0])**2 + (agents[0][1] - agents[1][1])**2)**0.5
#print (distance)

#let's run an analysis to work out which agent is furthest north (highest y)
print(max(agents, key=operator.itemgetter(1)))

#let's run an analysis to work out which agent is furthest east (highest x)

print(max(agents, key=operator.itemgetter(0)))

#plot the agents using matplotlib.pyplot

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    # colour the agent furthest east a different color
    #m = max(agents, key=operator.itemgetter(1))
    #matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()






# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.