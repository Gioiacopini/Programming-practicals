#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:16:25 2017

@author: gioia
"""

import random 

#use capital letter for name of the class because of PascalCasing

class Stores:
    def __init__ (self, stores):#init is the initalizer of the class
        self.x = (95,12,67,64,54,47,53,29)
        self.y = (30,51,80,9,9,51,36,95)
        self.stores = stores
        
        
class Customers:
    def __init__ (self, customers):
        self.x = (random.randint(0,100))
        self.y = (random.randint(0,100))
        self.customers = customers
    
    def move (self):
        if random.random()< 0.5:
            self.x = (self.x + 1) %99
        else:
            self.x = (self.x - 1) %99        
        
        if random.random()< 0.5:
             self.y = (self.y + 1) %99
        else:
             self.y = (self.y - 1) %99
             
             
#calculate discance between customers and stores
#def distance_from_store(customer0, store0):
    #return(((customer0[0]-store0[0])**2)+ ((customer0[1]-store0[1])**2)**0.5)
    
#for customer0 in customers:
    #for store0 in stores:
        #distance = distance_from_store(customer0, store0)
        #distances.append([distance])
        #print(distances)
    