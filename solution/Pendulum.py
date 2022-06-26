import numpy as np

class PendulumFull:
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

class PendulumSmallAngle:
    """
    Same class as before, but this time there is small angle approximation for non trigonometric functions
    """
    def __init__(self,l,g):
        self.l,self.g = l,g

    def __call__(self,u,t):
        u0,u1 = u
        l,g = self.l,self.g
        return np.array([u1,-(g/l)*u0])