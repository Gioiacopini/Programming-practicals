#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:26:31 2017

@author: gioia


"""
import random
import matplotlib.pyplot

#create stores that are set in a location 

stores=[]
customers = []
distances =[]

num_of_stores = 8
num_of_customers = 50
num_of_iterations= 100

stores.append([95, 30])
stores.append([12, 51])
stores.append([67, 80])
stores.append([64, 9])
stores.append([54, 9])
stores.append([47, 51])
stores.append([53, 36])
stores.append([29, 95])


#for i in range (num_of_stores):
    #stores.append([random.randint(0,100),random.randint(0,100)])
print (stores)

#generate customers 

for i in range (num_of_customers):
    customers.append([random.randint(0,100),random.randint(0,100)])
#print (customers)

#make customer move randomply without wandering off the plane

for j in range(num_of_iterations):
    for i in range(num_of_customers):
        if random.random()< 0.5:
            customers[i][0]= (customers[i][0] + 1) %99
        else:
            customers[i][0]= (customers[i][0] - 1) %99        
        
        if random.random()< 0.5:
             customers[i][1]= (customers[i][1] + 1) %99
        else:
             customers[i][1]= (customers[i][1] - 1) %99
             
#calculate discance between customers and stores
def distance_from_store(customer0, store0):
    return(((customer0[0]-store0[0])**2)+ ((customer0[1]-store0[1])**2)**0.5)
    
for customer0 in customers:
    for store0 in stores:
        distance = distance_from_store(customer0, store0)
        distances.append([distance])
        #print(distances)


#plot 

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_stores):
    matplotlib.pyplot.scatter(stores[i][0],stores[i][1], color='blue')
for i in range (num_of_customers):
    matplotlib.pyplot.scatter(customers[i][0],customers[i][1], color='tan')
# colour the the customer closest to a shop a different colour
matplotlib.pyplot.show()
