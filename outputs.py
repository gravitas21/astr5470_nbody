# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

# Define plotting functions
def plot_orbit_xyplane(positions,names,test=False):
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
    if not test:
        plt.savefig("bound_orbit_xy.jpeg",bbox_inches='tight')
    else:
        plt.savefig('test_saved_orbits.jpg',bbox_inches='tight')
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

# Read saved orbital parameters from outputfile
def read_saved_orbits(outfile):
    """
    Reads the saved orbital positions and velocities from output file
    """
    with open(outfile,'r') as f:
        print("Reading saved orbits from",outfile)
        lines = f.readlines()
        names = []
        masses = []
        times = []
        ## Read the names and masses of all particles
        firstline = lines[0]
        labels = firstline[1:-1].split(',')
        for label in labels:
            name,mass = label.split('_')
            names.append(name)
            masses.append(float(mass))
        N_bodies = len(labels)
        print("Number of particles",N_bodies)
        print("Names of particles",names)
        print("Masses of particles",masses)
        ## Determine the number of snapshots
        snaps = 0
        for ind,line in enumerate(lines):
            if ind == 0:
                continue
            else:
                if line[0] == '#':
                    time = float(line[1:].split('=')[-1])
                    times.append(time)
                    snaps += 1
        print("Number of snapshots",snaps)
        positions = np.zeros((snaps,N_bodies,3))
        velocities = np.zeros((snaps,N_bodies,3))
        snapcounter = 0
        counter = 0
        for ind,line in enumerate(lines):
            if ind == 0:
                continue
            else:
                if line[0] == '#':
                    continue
                else:
                    print(snapcounter,counter,'-->',line)
                    posvel = np.array([float(p) for p in line[:-1].split(',')])
                    print(posvel[0:3],posvel[3:6])
                    positions[snapcounter,counter,:] = posvel[0:3]
                    velocities[snapcounter,counter,:] = posvel[3:6]
                    counter += 1
            if counter > N_bodies - 1:
                counter = 0
                snapcounter += 1
                #exit()
        #print(N_bodies,names,masses,times)
        #print(positions)
        return N_bodies,names,masses,positions,velocities
