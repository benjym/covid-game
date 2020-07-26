import numpy as np
import matplotlib.pyplot as plt

def show_world(world):
    plt.ion() # turn on interactive mode
    plt.imshow(world)
    plt.colorbar()
    plt.pause(0.1) # wait a bit so we can see the graph
    # plt.show() # not needed in interactive mode
