from integrators import rk4,euler,leapfrog,hermite,total_energy
from outputs import read_saved_orbits,plot_orbit_xyplane
import matplotlib.pyplot as plt
import numpy as np

def test_time_reversal(integrator):
    """
    Tests the time reversal symmetry of the specified N-body integrator
    Evolves the orbit forward in time, and then in reverse
    Plots the orbit to test whether time reversal symmetry is preserved.
    """
    t0 = 0
    dt = 0.1
    t1 = 100
    N_bodies = 2
    M = np.array([1.0,3e-6])
    p = np.array([[0.0,0.0,0.0],[1.0,0.0,0.0]])
    v = np.array([[0.0,0.0,0.0],[0.0,1.0,0.0]])
    t = t0
    revt = t1
    positions = []
    velocities = []
    times = []
    revtimes = []
    while t <= t1:
        if integrator == 'rk4':
            p, v = rk4(p,v,dt,N_bodies,M)
        elif integrator == 'euler':
            p, v = euler(p,v,dt,N_bodies,M)
        elif integrator == 'leapfrog':
            p, v = leapfrog(p,v,dt,N_bodies,M)
        elif integrator == 'hermite':
            p, v = hermite(p,v,dt,N_bodies,M)
        positions.append(p.copy())
        velocities.append(v.copy())
        times.append(t)
        t += dt
    rev_positions = []
    rev_velocities = []
    while revt >= t0:
        if integrator == 'rk4':
            p, v = rk4(p,v,-dt,N_bodies,M)
        elif integrator == 'euler':
            p, v = euler(p,v,-dt,N_bodies,M)
        elif integrator == 'leapfrog':
            p,v = leapfrog(p,v,-dt,N_bodies,M)
        elif integrator == 'hermite':
            p,v = hermite(p,v,-dt,N_bodies,M)
        rev_positions.append(p.copy())
        rev_velocities.append(v.copy())
        revtimes.append(revt)
        revt -= dt

    fig, ax = plt.subplots(1, 1)
    for ind,pos in enumerate(positions):
        if ind == 0:
            ax.scatter(pos[0,0], pos[0,1], color='cyan', marker='o', label = "Sun")
            ax.scatter(pos[1,0], pos[1,1], color='red', marker='o', label = "Earth")
        else:
            ax.scatter(pos[0,0], pos[0,1], color='cyan', marker='o')
            ax.scatter(pos[1,0], pos[1,1], color='red', marker='o')
    for ind,pos in enumerate(rev_positions):
        if ind == 0:
            ax.scatter(pos[0,0], pos[0,1], color='cyan', marker='o', label = "Sun")
            ax.scatter(pos[1,0], pos[1,1], color='orange', marker='x', label = "Earth_reverse")
        else:
            ax.scatter(pos[0,0], pos[0,1], color='cyan', marker='o')
            ax.scatter(pos[1,0], pos[1,1], color='orange', marker='x')
    plt.legend(loc = 'upper right')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Orbital Plane from the Top")
    plt.savefig("time_reversal_symmetry_{}.jpeg".format(integrator))
    plt.show()
test_time_reversal(integrator='rk4')
test_time_reversal(integrator='euler')
test_time_reversal(integrator='leapfrog')
test_time_reversal(integrator='hermite')

def test_saved_orbits(outfile):
    """
    Test if function to read the saved orbits gives orbits that match the calculated ones
    """
    ## Read the saved orbits
    N_bodies,names,masses,positions,velocities,times = read_saved_orbits(outfile)
    ## Plot the orbits
    plot_orbit_xyplane(positions,names,test=True)
test_saved_orbits(outfile='output.txt')

def test_total_energy(outfile):
    """
    Test if the total energy of the system is conserved.
    """
    ## Read the saved orbits
    N_bodies,names,masses,positions,velocities,times = read_saved_orbits(outfile)
    total_energies = np.zeros(len(times))
    for ind,time in enumerate(times):
        totE = total_energy(positions[ind], velocities[ind], N_bodies, masses)
        total_energies[ind] = totE
        print(totE)
    plt.figure()
    plt.plot(times,total_energies)
    plt.xlabel('time [arb.units]')
    plt.ylabel('total energy of planetary system [arb.units]')
    plt.ylim(0,totE*3)
    plt.savefig('test_total_energy.jpg',bbox_inches='tight')
test_total_energy(outfile='output.txt')
