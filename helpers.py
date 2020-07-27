import numpy as np


def generate_world_with_single_infection(nx, ny):
    """
    Make an `nx` x `ny` grid, zero everywhere, with an infected person at the centre.
    """
    world = np.zeros([nx, ny])  # zero everywhere
    world[nx // 2, ny // 2] = 1  # infect the person in the middle
    return world


def infect_neighbours(world, infection_rate, encounters_per_day, travel_rate):
    """
    For every infected person, infect all of their neighbours with a given infection rate.
    """
    nx, ny = world.shape
    new_world = world.copy()
    for i in range(1, nx - 1):  # ignore edges for now
        for j in range(1, ny - 1):  # ignore edges for now
            if world[i, j] > 0:  # if infected
                neighbours = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1],
                              [i, j - 1], [i, j + 1], [i + 1, j - 1],
                              [i + 1, j], [i + 1, j + 1]]

                chosen_neighbours = np.random.choice(
                    len(neighbours), encounters_per_day
                )  # pick randomly from the neighbours list

                local_encounters = int(encounters_per_day -
                                       encounters_per_day * travel_rate)
                for n in range(local_encounters):
                    x, y = neighbours[chosen_neighbours[n]]
                    if world[x, y] == 0:
                        if np.random.rand() < infection_rate:
                            new_world[x, y] = 1
    return new_world


def recover_over_time(world, recovery_days, death):

    nx, ny = world.shape  # Get dimensions of array rep world
    new_world = world.copy()  # copy the array rep world

    for i in range(0, nx):  # Loop through entire array
        for j in range(0, ny):

            if world[i, j] > 0:  # If you're already sick
                new_world[i, j] += 1  #  add another day to number of sick days

                if np.random.rand() < death:  # There's a chance of 1% of dying
                    new_world[i, j] = -2  # set to -2 if someone dies

            if world[i, j] == recovery_days:  # If you've been sick for 7 days
                new_world[i, j] = -1  # set to recovered

    return new_world


def infect_travel(world, travel_rate, nt, encounters_per_day, travel_radius,infection_rate):

    nx, ny = world.shape  # get dimensions of the world
    new_world = world.copy()  # recreate world

    for i in range(nx):
        for j in range(ny):
            if new_world[i,j] > 1:  # assuming sick people are travelling too qrtn =0
                a = np.random.randint(
                    np.maximum(1, i - travel_radius),
                    np.minimum(i + travel_radius, nx - 1))
                b = np.random.randint(
                    np.maximum(1, j - travel_radius),
                    np.minimum(j + travel_radius, ny - 1))

                travel_loc = [[a-1, b-1], [a-1, b], [a-1, b+1],
                              [a  , b-1], [a  , b], [a  , b+1],
                              [a+1, b-1], [a+1, b], [a+1, b+1]]

                actual_travel = int(encounters_per_day * travel_rate)
                chosen_travloc = np.random.choice(
                    len(travel_loc), actual_travel)
               
                for loc in chosen_travloc:
                    x, y = travel_loc[loc]

                    if world[x, y] == 0 and np.random.rand() < infection_rate:
                        new_world[x, y] = 1

    return new_world
