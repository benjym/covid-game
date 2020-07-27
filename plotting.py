import numpy as np
import matplotlib.pyplot as plt


def show_world(world, recovery_days, t, nt):
    fig = plt.figure(1)
    plt.ion()  # turn on interactive mode

    fig.add_subplot(2,1,1)
    plt.imshow(
        world,  # show the 2d array `world`
        vmin=-1,  # set the minimum colour
        vmax=recovery_days,  # set the maximum colour
    )
    # plt.colorbar() # add a colour bar

    fig.add_subplot(2,1,2)
    
    N_infected = np.sum(world > 0) # number of infected
    N_recovered = np.sum(world == -1)
    N_dead = np.sum(world == -2)
    
    plt.plot(t, N_infected, 'r.')
    plt.plot(t, N_recovered, '.',color='grey')
    plt.plot(t, N_dead, 'k.')

    # Set limits of graph so it doesn't jump around
    plt.xlim(0,nt)
    # plt.ylim(0,world.shape[0]*world.shape[1])
    
    if t == 0:
        plt.ylabel('Number')
        plt.xlabel('Days')

    plt.pause(0.1)  # wait a bit (0.1 seconds) so we can see the graph
    # plt.show() # not needed in interactive mode
