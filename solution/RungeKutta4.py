import ODESolver

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