# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math
import integrators as intg
from setup import read_input_file,read_command_line,run_Nbody
from plots import plot_orbit_xyplane

#TODO
## Document the code in README and create a Github wiki page
## Implement the integrators
## Create output routines
## Implement three non-trivial tests

# Defining main function
def main():
    ## Greet the user in Nepali!
    print("Namaste!")

    ## Read command line arguments
    inputfile,outputfile,integrator = read_command_line()

    ## Read the input file: input.txt
    N_bodies,M,pos,vel,tend,delta_t,tframe = read_input_file(inputfile)
    print(N_bodies,M,pos.shape,vel.shape,tend,delta_t,tframe)

    ## Run the N-body integration
    positions, velocities, times = run_Nbody(N_bodies,M,pos,vel,tend,delta_t,tframe,integrator)
    print(positions)

    ## Plot the orbit
    plot_orbit_xyplane(positions)

# Using the special variable
# __name__
if __name__=="__main__":
    main()
