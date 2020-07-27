# coding: utf-8

import matplotlib.pyplot as plt
import helpers as hlp
import plotting as plot

# States:
# - 0 is Healthy
# - N is Infected for N days
# - -1 is Recovered
# - -2 is Dead :(

# System parameters
nx = 50  # number of cells across
ny = 50  # number of cells up/down
nt = 10  # number of days to simulate

# Covid parameters
infection_rate = 0.5  # chance of spreading infection to a new cell
encounters_per_day = 9 # meet 4 people per day
recovery_days = 3 # how many days before recovery
death = 0.01 # how many people die from COVID
travel_rate = 0.5 # how often people travel to new areas
travel_radius = 10 # how many cells far people can travel

world = hlp.generate_world_with_single_infection(nx, ny)

for t in range(nt):
    world = hlp.infect_neighbours(world, infection_rate,encounters_per_day,travel_rate)
    world = hlp.recover_over_time(world, recovery_days,death)
    world = hlp.infect_travel(world,travel_rate,t,encounters_per_day,travel_radius,infection_rate)
    plot.show_world(world, recovery_days, t, nt)

plt.pause(2) # wait a bit