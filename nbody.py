# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math
import integrators as intg

from setup import read_input_file,read_command_line

#TODO
## Document the code in README and create a Github wiki page
## Create input routines
## Implement the integrators
## Create output routines
## Implement three non-trivial tests

# Defining main function
def main():
    ## Greet the user!
    print("Namaste!")
    ## Read command line arguments
    inputfile,outputfile,algorithm = read_command_line()
    ## Read the input file: input.txt
    N_bodies,tend,delta_t,pos,vel = read_input_file(inputfile)
    print(N_bodies,tend,delta_t,pos,vel)

# Using the special variable
# __name__
if __name__=="__main__":
    main()
