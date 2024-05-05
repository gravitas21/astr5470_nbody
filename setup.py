# Importing libraries
import numpy as np

# Read initial_conditions
def read_input_file(file):
    with open(file,'r') as f:
        lines = f.readlines()
        N_bodies,tend,delta_t = lines[0][:-1].split(',')
        N_bodies = int(N_bodies)
        M = np.zeros(N_bodies)
        pos = np.zeros((N_bodies,3))
        vel = np.zeros((N_bodies,3))
        M = lines[1][:-1].split(',')
        pos[:,0] = lines[2][:-1].split(',')
        pos[:,1] = lines[3][:-1].split(',')
        pos[:,2] = lines[4][:-1].split(',')
        vel[:,0] = lines[5][:-1].split(',')
        vel[:,1] = lines[6][:-1].split(',')
        vel[:,2] = lines[7][:-1].split(',')
    return N_bodies,tend,delta_t,pos,vel
