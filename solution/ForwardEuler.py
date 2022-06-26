import ODESolver

class ForwardEuler(ODESolver):
    def step(self):
        u,f,it,t = self.u,self.f,self.it,self.t
        dt = t[it+1] - t[it]
        return u[it,:]+dt*f(u[it,:],t[it])