#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 16:11:55 2017

@author: gioia
"""
#import statements
import random

#create the agent class
class Agent:
    def __init__ (self, environment, agents):
        self.x = random.randint(0,99)
        self.y = random.randint (0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
        

    def move (self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 99
        else:
            self.x = (self.x - 1) % 99

        if random.random() < 0.5:
            self.y = (self.y + 1) % 99
        else:
            self.y = (self.y - 1) % 99
        #print(self.x, self.y)
    
    def eat (self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x]-=10
            self.store+=10
        if 0<self.environment[self.y][self.x]<10:
            self.store+=self.environment[self.y][self.x]
            self.environment[self.y][self.x]-=self.environment[self.y][self.x]
        if self.store > 1000:
            self.environment[self.y][self.x]+=self.store
            self.store = 0 
            
            #print(self.store)
        
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2)**0.5)

    def share_with_neighbours (self, neighborhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighborhood:
                sum = self.store + agent.store
                ave = sum/2
                self.store = ave 
                agent.store = ave
                #print("sharing "+str(dist) + " " + str(ave))
