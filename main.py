#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from helpers import *
from plotting import *

# States:
#   - 0 is Healthy
#   - 1 is Infected
#   - 2 is Recovered

# System parameters
nx = 50 # number of cells across
ny = 50 # number of cells up/down
nt = 10 # number of time steps to simulate

# Covid parameters
infection_rate = 0.1 # chance of spreading infection to a new cell

if __name__ == '__main__':
    for t in range(nt):
        world = infect_neighbours(world)
        show_world(world)
