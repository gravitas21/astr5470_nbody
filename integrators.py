# Importing libraries
import numpy as np
import matplotlib.pyplot as plt

# Define integrators
def rk4(p,v,delta_t,N_bodies,M):
    """
    RK4 algorithm for integration
    """
    k1p, k1v = Nbody_derivatives(p, v, N_bodies, M)
    k2p, k2v = Nbody_derivatives(p+k1p*0.5*delta_t, v+k1v*0.5*delta_t, N_bodies, M)
    k3p, k3v = Nbody_derivatives(p+k2p*0.5*delta_t, v+k2v*0.5*delta_t, N_bodies, M)
    k4p, k4v = Nbody_derivatives(p+k3p*delta_t, v+k3v*delta_t, N_bodies, M)
    return p+delta_t*(k1p+2*(k2p+k3p)+k4p)/6, v+delta_t*(k1v+2*(k2v+k3v)+k4v)/6

def euler(p,v,delta_t,N_bodies,M):
    """
    Euler algorithm for integration
    """
    dpdt, dvdt = Nbody_derivatives(p, v, N_bodies, M)
    p, v = p + dpdt*delta_t, v + dvdt*delta_t
    return p, v

def Nbody_derivatives(pos, vel, N_bodies,M):
    """
    ODE equations governing our system:
    Gravitational force equations for N-body system
    """
    dpdt = vel
    G = 1.0
    dvdt = np.zeros(vel.shape)
    r = np.linalg.norm( pos[1,:]-pos[0,:])
    rhat = (pos[1,:] - pos[0,:])/r
    dvdt[0,:]= G*M[1]/(r*r)*rhat
    dvdt[1,:]= -G*M[0]/(r*r)*rhat
    return dpdt, dvdt
