# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

# Define plotting functions
def plot_orbit_xyplane(positions,names):
    """
    Plot the orbit in X-Y plane
    """
    colors = np.array(['red','orange','yellow','green','cyan','blue','purple'])
    fig, ax = plt.subplots(1, 1)
    for ind,pos in enumerate(positions):
        if ind == 0:
            for pid,name in enumerate(names):
                ax.scatter(pos[pid,0], pos[pid,1], color=colors[pid], marker='o', label = names[pid])
        else:
            for pid,name in enumerate(names):
                ax.scatter(pos[pid,0], pos[pid,1], color=colors[pid], marker='o')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Your planetary system from the top")
    plt.savefig("bound_orbit_xy.jpeg")
    plt.show()
