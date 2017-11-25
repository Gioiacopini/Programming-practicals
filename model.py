# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import statements
import random

#Make a y and x variable (randomly generated)
y0 = random.randint(0,100)
x0 = random.randint(0,100)

print (x0, y0)

# Move x0 randomly

if random.random() < 0.5:
    x0 = x0 +1
else:
    x0 = x0 - 1

# Move y0 randomly

if random.random() < 0.5: 
    y0 = y0 + 1
else: 
    y0 = y0 -1 
    
print (x0, y0)
    
# Move x0 randomly

if random.random() < 0.5:
    x0 = x0 +1
else:
    x0 = x0 - 1

# Move y0 randomly

if random.random() < 0.5: 
    y0 = y0 + 1
else: 
    y0 = y0 -1 
    
print (x0, y0)

# Create x1 and y1 (randomly generated)
y1 = random.randint(0,100)
x1 = random.randint(0,100)

print (x1, y1)

# Move x1 randomly

if random.random() < 0.5:
    x1 = x1 +1
else:
    x1 = x1 - 1

# Move y1 randomly

if random.random() < 0.5: 
    y1 = y1 + 1
else: 
    y1 = y1 -1 
    
print (x1, y1)
    
# Move x1 randomly

if random.random() < 0.5:
    x1 = x1 +1
else:
    x1 = x1 - 1

# Move x1 randomly
    
if random.random() < 0.5: 
    y1 = y1 + 1
else: 
    y1 = y1 -1 
    
print (x1, y1)


# calculate the discance between the variables usign the Pythagorian theorem

distance = ((x0-x1)**2 + (y0 - y1)**2)**0.5
print (distance)







# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.