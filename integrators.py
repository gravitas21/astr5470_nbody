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

def leapfrog(p,v,delta_t,N_bodies,M):
    """
    leapfrog method for orbital integration
    """
    p_nphalf = np.zeros(p.shape)
    p_npone  = np.zeros(p.shape)
    v_nphalf = np.zeros(v.shape)
    v_npone  = np.zeros(v.shape)
    # positions and velocities at half time step
    p_nphalf = p + v*delta_t/2
    v_nphalf = v
    # velocities and accelerations at half time step
    dpdt, dvdt = Nbody_derivatives(p_nphalf, v_nphalf, N_bodies, M)
    # update position and velocity at full time step
    v_npone = v + dvdt*delta_t
    p_npone = p_nphalf+v_npone*delta_t/2
    return p_npone,v_npone

def hermite(p,v,delta_t,N_bodies,M):
    """
    Hermite integration scheme for orbits
    """
    dvdt, dadt = hermite_derivatives(p,v, N_bodies, M)
    p_pred = p + v*delta_t + 1/2*dvdt*delta_t**2 + 1/6*dadt*delta_t**3
    v_pred = v + dvdt*delta_t + 1/2*dadt*delta_t**2
    dvdt_new, dadt_new = hermite_derivatives(p_pred,v_pred, N_bodies, M)
    ap2 = -6/delta_t**2 * (dvdt-dvdt_new) - 2*(2*dadt+dadt_new)/delta_t
    ap3 = 12/delta_t**3 * (dvdt-dvdt_new) - 6*(dadt+dadt_new)/delta_t**2
    p_new = p_pred + 1/24*delta_t**4 * ap2 + 1/120*delta_t**5 *ap3
    v_new = v_pred + 1/6*delta_t**3 * ap2 + 1/24*delta_t**4 *ap3
    return p_new,v_new

def Nbody_derivatives_twobody(pos, vel, N_bodies, M):
    """
    ODE equations governing our system:
    Gravitational force equations for N-body system, N = 2
    """
    dpdt = vel
    G = 1.0
    dvdt = np.zeros(vel.shape)
    r = np.linalg.norm( pos[1,:]-pos[0,:])
    rhat = (pos[1,:] - pos[0,:])/r
    dvdt[0,:]= G*M[1]/(r*r)*rhat
    dvdt[1,:]= -G*M[0]/(r*r)*rhat
    #print(0,1,pos[0],pos[1],r,M[1],dvdt[0,:])
    #print(1,0,pos[1],pos[0],r,M[0],dvdt[1,:])
    return dpdt, dvdt

def Nbody_derivatives(pos, vel, N_bodies, M):
    """
    ODE equations governing our system:
    Gravitational force equations for N-body system
    """
    dpdt = vel
    G = 1.0
    dvdt = np.zeros(vel.shape)
    for i in range(N_bodies) :
        for j in range(N_bodies) :
            if i == j :
                continue
            r = np.linalg.norm( pos[j]-pos[i])
            mass = M[j]
            rhat = (pos[j] - pos[i])/r
            Fij = G*mass/(r*r)*rhat
            #print(i,j,pos[i],pos[j],r,mass,Fij)
            dvdt[i] += Fij
    return dpdt, dvdt

def total_energy(pos, vel, N_bodies, M):
    """
    Calculation of total energy of the system
    """
    G = 1.0
    totKE = 0.0
    totPE = 0.0
    for i in range(N_bodies) :
        totKE += 0.5*M[i]*np.sum(vel[i]**2)
        for j in range(N_bodies) :
            if i == j :
                continue
            r = np.linalg.norm( pos[j]-pos[i])
            Eij = - G*M[i]*M[j]/r
            #print(i,j,r,Eij)
            totPE += Eij
    totE = totKE + 0.5*totPE
    return totE

def hermite_derivatives(pos, vel, N_bodies, M):
    """
    equations for acceleration and its derivatives for the Hermite scheme
    """
    G = 1.0
    dvdt = np.zeros(vel.shape)
    dadt = np.zeros(vel.shape)
    for i in range(N_bodies) :
        for j in range(N_bodies) :
            if i == j :
                continue
            r = np.linalg.norm( pos[j]-pos[i])
            v = np.linalg.norm( vel[j]-vel[i])
            rvdot = np.dot(pos[j]-pos[i],vel[j]-vel[i])
            mass = M[j]
            rhat = (pos[j] - pos[i])/r
            Fij = G*mass/(r*r)*rhat
            aij = G*mass*( (vel[j]-vel[i])/(r**3) - 3/(r**5)*rvdot*(pos[j]-pos[i]))
            #print(i,j,pos[i],pos[j],r,mass,Fij)
            dvdt[i] += Fij
            dadt[i] += aij
    return dvdt, dadt
