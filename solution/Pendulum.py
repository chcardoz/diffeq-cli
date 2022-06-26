import numpy as np

class Pendulum:
    """
    Class to define the differential equation with a call method

        Parameters:
        l [float] : The length of the bob from center. 
        g [float] : The gravitational constant of the planet you are on. 
    """
    def __init__(self,l,g) -> None:
        self.l,self.g = l,g

    def __call__(self, u,t):
        u0, u1 = u
        l,g = self.l,self.g
        return np.array([u1,-(g/l)*np.sin(u0)])