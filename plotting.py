import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

def custom_colormap(incubation_days,recovery_days):
    cmap = ListedColormap(['black','gray','white','coral','red'],name='covid')
    boundaries = [-2.5,-1.5,-0.5,0.5,incubation_days+0.5,recovery_days+0.5]
    norm = BoundaryNorm(boundaries, cmap.N, clip=True)
    return cmap, norm

def show_world(world, recovery_days, t, nt, cmap, norm,incubation_days):
    fig = plt.figure(1)
    plt.ion()  # turn on interactive mode

    fig.add_subplot(2,1,1)
    plt.imshow(
        world,  # show the 2d array `world`
        # vmin=-4,  # set the minimum colour
        # vmax=recovery_days,  # set the maximum colour
        # cmap='Dark2' # set the colour map
        cmap=cmap,
        norm=norm
    )
    if t == 0:
        cb = plt.colorbar(ticks=[-2,-1,0,incubation_days,recovery_days]) # add a colour bar
        cb.set_ticklabels(['Dead','Recovered','Healthy','Incubating','Sick'])

    fig.add_subplot(2,1,2)
    
    N_total = world.shape[0]*world.shape[1]
    N_infected = np.sum(world > 0) # number of infected
    N_recovered = np.sum(world == -1)
    N_dead = np.sum(world == -2)
    
    plt.plot(t, 100.*N_infected/N_total, 'r.', label='Infected')
    plt.plot(t, 100.*(N_recovered)/N_total, '.',color='grey',label='Recovered')
    plt.plot(t, 100.*(N_dead)/N_total, 'k.', label='Dead')

    # Set limits of graph so it doesn't jump around
    plt.xlim(0,nt)
    plt.ylim(0,100)
    
    if t == 0:
        plt.ylabel('Percentage')
        plt.xlabel('Days')
        plt.legend()

    plt.pause(0.1)  # wait a bit (0.1 seconds) so we can see the graph
    # plt.show() # not needed in interactive mode


