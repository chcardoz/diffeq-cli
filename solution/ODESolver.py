import numpy as np
from tqdm import tqdm

class ODESolver():
    """Superclass to solve ordinary differential equations 
    """
    def __init__(self,f) -> None:
        """Constructor
        
        f: Right hand side function of the ODE
        """
        self.f = f

    def set_initial_conditions(self,U0) -> None:
        """
        """
        if isinstance(U0,(int,float)):
            self.num_of_eqns = 1
            U0 = float(U0)
        else:
            U0 = np.asarray(U0)
            self.num_of_eqns = U0.size
        self.U0 = U0

    def solve(self,time_array):
        """
        """
        self.t = np.asarray(time_array)
        nt = self.t.size #Number of points in time array
        self.u = np.zeros((nt,self.num_of_eqns)) #Solution array initialized as an array of zeros
        self.u[0,:] = self.U0
        #Integrate
        for it in tqdm(range(nt - 1),ascii=True):
            self.it = it
            self.u[it+1] = self.step()

        return self.u,self.t

    def step(self):
        """Step through the solution one time step. Needs to implemented by any derivatives
        """
        raise NotImplementedError

class RungeKutta4(ODESolver):
    '''
    Runge Kutta with 4 K's implementation of the step method from the general ODE solver class 
    '''
    def step(self):
        u,f,it,t = self.u,self.f,self.it,self.t
        dt = t[it+1] - t[it]
        dt2 = dt / 2
        K1 = dt * f(u[it,:],t[it])
        K2 = dt * f(u[it,:]+0.5*K1,t[it]+dt2)
        K3 = dt * f(u[it,:]+0.5*K2,t[it]+dt2)
        K4 = dt * f(u[it,:]+K3,t[it]+dt) 
        return u[it,:]+(1/6)*(K1+2*K2+2*K3+K4)        