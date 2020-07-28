# coding: utf-8

import matplotlib.pyplot as plt
import helpers as hlp
import plotting as plot

# States:
# - 0 is Healthy
# - N is Infected for N days
# - -1 is Recovered
# - -4 is Dead :(

# System parameters
nx = 50     # number of cells across
ny = 50     # number of cells up/down
nt = 30    # number of days to simulate

# Covid parameters
infection_rate      = 0.2   # chance of spreading infection to a new cell
encounters_per_day  = 5     # people met per day
recovery_days       = 7     # how many days before recovery
original_death_rate = 0.01  # how many people die from COVID
travel_rate         = 0.5   # how often people travel to new areas
travel_radius       = 10    # how many cells far people can travel
incubation_days     = 3     # How many days you're asymptomatic
total_space         = 1000  # space in hospitals



world = hlp.generate_world_with_single_infection(nx, ny)
cmap,norm = plot.custom_colormap(incubation_days,recovery_days)

for t in range(nt):
    current_death_rate = hlp.hospital(world,recovery_days,original_death_rate,incubation_days,total_space)
    world = hlp.infect_neighbours(world, infection_rate,encounters_per_day,travel_rate)
    world = hlp.recover_over_time(world, recovery_days,current_death_rate)
    world = hlp.infect_travel(world,travel_rate,t,encounters_per_day,travel_radius,infection_rate,incubation_days)
    plot.show_world(world, recovery_days, t, nt, cmap, norm,incubation_days)

plt.pause(2) # wait a bit