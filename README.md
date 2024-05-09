# astr5470_nbody
This repository consists of a N-body integrator for planetary systems. It was developed as a final project for ASTR 5470 course on Computational Astrophysics. The code reads in orbital positions and velocities for the star and planets, performs the N-body integration using a user-specified algorithm, and returns the time evolution of these parameters for a specified period of time.

## Running the simulation
The user can run the simulation from the command line as follows:

`python3 nbody.py --init 'input.txt' --alg 'rk4' --out 'output.txt'`

Here, `input.txt`, supplied to the `init` argument, is the input file with names, orbital positions and velocities of the particles, timestep, output step (frame rate) and total duration of the simulation.  The argument `alg` specifies which integration algorithm to use and `out` is the name of the output file to store the simulation results.

An example input file is shown below.

```
6,10.0,0.001,0.25
1.0,1.651e-7,2.44e-6,3.0e-6,3.22e-7,9.54e-4
0.0,0.387,0.72,1.0,1.54,5.20
0.0,0.0,0.0,0.0,0.0,0.0
0.0,0.0,0.0,0.0,0.0,0.0
0.0,0.0,0.0,0.0,0.0,0.0
0.0,1.578,1.175,1.0,0.8,0.438
0.0,0.0,0.0,0.0,0.0,0.0
Sun,Mercury,Venus,Earth,Mars,Jupiter
```

The first line specifies the number of particles `N_bodies`, the final time `tend`, the time step `\delta t`, and the frame rate for output `tframe`. The next line specifies the masses `M` of each particle. The following 6 lines specify the initial positions `x`,`y` and `z` of each particle, followed by initial velocities `vx`,`vy` and `vz`. The final line specifies the names of the particles in the planetary system.

We can specify the integrator `alg` to be either `euler`,`rk4`,`leapfrog` or `hermite`. Finally, the output file saves the simulated orbits for further analysis later on. The output file `output.txt` can be read with the `read_saved_orbits` function from `outputs.py` file as follows:

`read_saved_orbits(outfile='output.txt')`

The first line of the output file specifies the names and masses of the particles in the simulation, separated by an underscore `_`. The following blocks store the positions and velocities of each particle for the snapshot specified in `# t = t_snap` line, where `$t_snap$` is the time of the snapshot. An example output file is shown below:

```
#Sun_1.0,Mercury_1.651e-07,Venus_2.44e-06,Earth_3e-06,Mars_3.22e-07,Jupiter_0.000954
#t = 0
0.0,0.0,0.0,0.0,0.0,0.0
0.387,0.0,0.0,0.0,1.578,0.0
0.72,0.0,0.0,0.0,1.175,0.0
1.0,0.0,0.0,0.0,1.0,0.0
1.54,0.0,0.0,0.0,0.8,0.0
5.2,0.0,0.0,0.0,0.438,0.0
```
