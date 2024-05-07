# astr5470_nbody
This repository consists of a N-body integrator for planetary systems. It was developed as a final project for ASTR 5470 course on Computational Astrophysics. The code reads in orbital positions and velocities for the star and planets, performs the N-body integration using a user-specified algorithm, and returns the time evolution of these parameters for a specified period of time.

## Running the simulation
The user can run the simulation from the command line as follows:

`python3 nbody.py --init 'input.txt' --alg 'rk4' --out 'output.txt'`

Here, `input.txt`, supplied to the `init` argument, is the input file with names, orbital positions and velocities of the particles, timestep, output step (frame rate) and total duration of the simulation.  The argument `alg` specifies which integration algorithm to use and `out` is the name of the output file to store the simulation results. 
