#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# # Helper functions

# In[11]:


def infect_neighbours(i,j,world):
    x_locs = [i-1,i,i+1]
    y_locs = [j-1,j,j+1]
    for x in x_locs:
        for y in y_locs:
            if world[x,y] == 0:
                if np.random.rand() < infection_rate:
                    world[x,y] = 1
    return world


# # System parameters

# In[18]:


nx = 50 # number of cells across
ny = 50 # number of cells up/down
nt = 10 # number of time steps to simulate

infection_rate = 0.1 # chance of spreading infection to a new cell


# # Set up initial condition
# `world` is an `nx`x`ny` array which stores the value of everyone's state
# 
# States:
#   - `0` &mdash; Healthy
#   - `1` &mdash; Infected
#   - `2` &mdash; Recovered

# In[19]:


world = np.zeros([nx,ny]) # zero everywhere
world[nx//2,ny//2] = 1 # infect the person in the middle


# In[20]:


for t in range(nt):
    for i in range(1,nx-1): # ignore edges for now
        for j in range(1,ny-1): # ignore edges for now
            if world[i,j] == 1: # if infected
                world = infect_neighbours(i,j,world)
    plt.imshow(world)
    plt.show()


# In[ ]:




