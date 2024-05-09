# Importing libraries
import numpy as np
import argparse
from integrators import rk4,euler,leapfrog,Nbody_derivatives

# Read command-line arguments
def read_command_line():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description ='Run n-body integration for particles in input file using specified algorithm')
    # Add an argument for each input
    parser.add_argument('--init', type=str)
    parser.add_argument('--out', type=str)
    parser.add_argument('--alg', type=str)
    # Parse the command-line arguments
    args = parser.parse_args()
    # Use the command-line arguments in your script
    inputfile  = args.init
    outputfile = args.out
    algorithm  = args.alg
    return inputfile,outputfile,algorithm

# Read initial_conditions
def read_input_file(file):
    with open(file,'r') as f:
        lines = f.readlines()
        N_bodies,tend,delta_t,tframe = lines[0][:-1].split(',')
        N_bodies = int(N_bodies)
        tend = float(tend)
        delta_t = float(delta_t)
        tframe = float(tframe)
        M = np.zeros(N_bodies)
        pos = np.zeros((N_bodies,3))
        vel = np.zeros((N_bodies,3))
        M = np.array([float(x) for x in lines[1][:-1].split(',')])
        pos[:,0] = lines[2][:-1].split(',')
        pos[:,1] = lines[3][:-1].split(',')
        pos[:,2] = lines[4][:-1].split(',')
        vel[:,0] = lines[5][:-1].split(',')
        vel[:,1] = lines[6][:-1].split(',')
        vel[:,2] = lines[7][:-1].split(',')
        names = lines[8][:-1].split(',')
    return N_bodies,M,pos,vel,tend,delta_t,tframe,names

# Setup the N-body integration
def run_Nbody(N_bodies,M,pos,vel,tend,delta_t,tframe,integrator):
    t = 0
    tnext = tframe
    positions = []
    velocities = []
    times = []
    while t<tend :
        while t < tnext :
            #delta_t = min(delta_t,tnext-t)
            ## Evolve the N-body system based on user choice of integrator
            if integrator=="euler":
                pos, vel = euler(pos,vel,delta_t,N_bodies,M)
            elif integrator== "rk4":
                pos, vel = rk4(pos,vel,delta_t,N_bodies,M)
            elif integrator=="leapfrog":
                pos, vel = leapfrog(pos,vel,delta_t,N_bodies,M)
            else:
                print("please specify either rk4 or euler only")
                exit()
            t += delta_t
            #print(t,delta_t)
            #exit()
        positions.append(pos.copy())
        velocities.append(vel.copy())
        times.append(tnext)
        tnext += tframe
    return positions, velocities, times
