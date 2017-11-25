# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import statements
import random

# lists 
agents =[] #this is an empty list

#Make a y and x variable (randomly generated)
y0 = random.randint(0,100)
x0 = random.randint(0,100)

agents.append([x0,y0])

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
y1 = random.randint(0,100)
x1 = random.randint(0,100)

agents.append([x1,y1])

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







# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.