# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import statements
import random
import operator
import matplotlib.pyplot

# lists 
agents =[] #this is an empty list

#Make a y and x variable (randomly generated) without creating separate variables.
#this code appends random integers between 0 and 99 to the list [agents] created above. 
agents.append([random.randint(0,99),random.randint(0,99)])

print (agents)

# Move x0 randomly
# the (x0,y0) list is agents[0]. x0 is agents[0][0] and y0 is agents[0][1]

if random.random() < 0.5:
    agents[0][0]+= 1
else:
    agents[0][0]-= 1

print(agents[0][0])


# Move y0 randomly

if random.random() < 0.5: 
    agents[0][1]+= 1
else: 
    agents[0][1]-= 1

print(agents[0][1])

    
# Move x0 randomly
    
if random.random() < 0.5:
    agents[0][0]+= 1
else:
    agents[0][0]-= 1

print(agents[0][0])

# Move y0 randomly

if random.random() < 0.5: 
    agents[0][1]+= 1
else: 
    agents[0][1]-= 1

print(agents[0][1])

# Create x1 and y1 (randomly generated)

agents.append([random.randint(0,99),random.randint(0,99)])

print(agents)

# Move x1 randomly

if random.random() < 0.5:
    agents[1][0]+= 1
else:
    agents[1][0]-= 1

print(agents[1][0])

# Move y1 randomly

if random.random() < 0.5: 
    agents[1][1]+= 1
else: 
    agents[1][1]-= 1
    
print(agents[1][1])

# Move x1 randomly

if random.random() < 0.5:
    agents[1][0]+= 1
else:
    agents[1][0]-= 1

print(agents[1][0])

# Move y1 randomly

if random.random() < 0.5: 
    agents[1][1]+= 1
else: 
    agents[1][1]-= 1
    
print(agents[1][1])

# calculate the discance between the variables usign the Pythagorian theorem

distance = ((agents[0][0]-agents[1][0])**2 + (agents[0][1] - agents[1][1])**2)**0.5
print (distance)

#let's run an analysis to work out which agent is furthest north (highest y)
print(max(agents, key=operator.itemgetter(1)))

#let's run an analysis to work out which agent is furthest east (highest x)

print(max(agents, key=operator.itemgetter(0)))

#plot the agents using matplotlib.pyplot

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
# colour the agent furthest east a different color
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')

matplotlib.pyplot.show()






# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.