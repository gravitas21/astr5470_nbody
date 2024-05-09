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

# Save integration results in output file
def save_orbits(outfile,times,names,M,positions,velocities):
    """
    Save the orbital positions and velocities to output file
    """
    with open(outfile,'w') as f:
        labels = []
        for name,mass in zip(names,M):
            labels.append(name+'_'+str(mass))
        print(labels)
        f.write("#"+",".join(str(label) for label in labels)+"\n")
        for ind,pos in enumerate(positions):
            #print("#t = {} \n".format(times[ind]))
            f.write("#t = {} \n".format(times[ind]))
            for p,v in zip(pos,velocities[ind]):
                posvel = list(p)+list(v)
                f.write(",".join(str(item) for item in posvel)+"\n")
                #print(p,v)
    print("Saved orbits to {}".format(outfile))
