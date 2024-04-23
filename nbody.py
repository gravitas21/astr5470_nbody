# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math
import integrators as intg
import argparse

#TODO
## Document the code in README and create a Github wiki page
## Create input routines
## Implement the integrators
## Create output routines
## Implement three non-trivial tests

# Defining main function 
def main(): 
    print("hey there")
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description ='Run n-body integration for particles in input file using specified algorithm')
    # Add an argument for each input 
    parser.add_argument('--init', type=str)
    parser.add_argument('--out', type=str)
    parser.add_argument('--alg', type=str)
    # Parse the command-line arguments
    args = parser.parse_args()
    # Use the command-line arguments in your script
    print(args.init)
    print(args.out)
    print(args.alg)

# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 
