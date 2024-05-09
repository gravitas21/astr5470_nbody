# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from setup import read_input_file,read_command_line,run_Nbody
from outputs import plot_orbit_xyplane,save_orbits

#TODO
## Document the code in README and create a Github wiki page
## Create output routines
## Implement two non-trivial tests

# Defining main function
def main():
    """
    Main function to run the astr_nbody code
    Calls other functions to do each step
    """
    ## Greet the user in Nepali!
    print("Namaste!")

    ## Read command line arguments
    inputfile,outputfile,integrator = read_command_line()

    ## Read the input file: input.txt
    N_bodies,M,pos,vel,tend,delta_t,tframe,names = read_input_file(inputfile)
    print("Initial parameters:\n",N_bodies,M,pos.shape,vel.shape,tend,delta_t,tframe)

    ## Run the N-body integration
    positions, velocities, times = run_Nbody(N_bodies,M,pos,vel,tend,delta_t,tframe,integrator)
    #print(positions)

    ## Plot the orbits
    plot_orbit_xyplane(positions,names)

    ## Save the orbits
    save_orbits(outputfile,times,names,M,positions,velocities)

# Using the special variable
# __name__
if __name__=="__main__":
    main()
