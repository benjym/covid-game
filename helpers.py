import numpy as np

def generate_world_with_single_infection(nx,ny):
    """
    Make an nx x ny grid, zero everywhere, with an infected person at the centre.
    """
    world = np.zeros([nx,ny]) # zero everywhere
    world[nx//2,ny//2] = 1 # infect the person in the middle
    return world

def infect_neighbours(world,infection_rate):
    """
    For every infected person, infect all of their neighbours with a given infection rate.
    """
    nx,ny = world.shape
    for i in range(1,nx-1): # ignore edges for now
        for j in range(1,ny-1): # ignore edges for now
            if world[i,j] == 1: # if infected
                x_locs = [i-1,i,i+1]
                y_locs = [j-1,j,j+1]
                for x in x_locs:
                    for y in y_locs:
                        if world[x,y] == 0:
                            if np.random.rand() < infection_rate:
                                world[x,y] = 1
    return world
