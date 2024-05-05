# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math
import integrators as intg
import argparse
from setup import read_input_file

#TODO
## Document the code in README and create a Github wiki page
## Create input routines
## Implement the integrators
## Create output routines
## Implement three non-trivial tests

# Defining main function
def main():
    print("Namaste!")
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

    ## Read the input file: input.txt
    N_bodies,tend,delta_t,pos,vel = read_input_file(inputfile)
    print(N_bodies,tend,delta_t,pos,vel)

# Using the special variable
# __name__
if __name__=="__main__":
    main()
