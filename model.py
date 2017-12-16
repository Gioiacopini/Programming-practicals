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

#create variables 
num_of_agents = 10
num_of_iterations = 50
neighborhood = 20
store = 0

#create empty lists in which items will be appointed later in the code
agents =[] 
environment=[]

#randomly create agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
    
#read data 
file = open("in.txt", newline='')

reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
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
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color="blue")
    #colour the agent furthest east a different color
    #m = max(agents, key=operator.itemgetter(1))
    #matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()

#write a csv file 
file2 = open("environmentout.csv", "w", newline = "")
writer = csv.writer(file2)

for row in environment:
    writer.writerow(row)

file2.close

#write a file that writes the total stored by all the agents on a line.
#this code gets the model to append the data to the file other than clearing it each time

for agent in agents:
    total_store = store + agents[i].store

file3 = open("totalstorebyagent.csv", "a", newline="")
file3.write(str(total_store)+ "\n")

file3.close()

file.close()

