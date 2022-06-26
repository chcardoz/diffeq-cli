from cProfile import label
import click
import numpy as np
from ODESolver import RungeKutta4
from Pendulum import Pendulum
import matplotlib.pyplot as plt

@click.group()
def main():
    '''
    Welcome to the main program of the show, ladies and gentlemen
    '''
    pass

@click.command()
@click.option('-t','--time',nargs=2,type=click.Tuple([int,float]),required=True,show_default=True,default=(2,1e3))
def test(time):
    '''
    A simple test function that I wrote to see what was going on
    '''
    periods,n = time
    t = periods*2*np.pi
    n = int(n)
    click.echo(f'Welcome to the solution, please check --help to know more about the commands')
    click.echo(f'Simulation time = {t} seconds')
    f = Pendulum(1,9.8)
    initial_conditions = [100,10]
    time_points = np.linspace(0,t,n+1)
    fig,(ax1) = plt.subplots(1,1)
    solver = RungeKutta4(f)
    solver.set_initial_conditions(initial_conditions)
    u,t = solver.solve(time_points)
    ax1.plot(u[:,0],u[:,1],label="Phase potrait")
    ax1.set_xlabel("U0")
    ax1.set_ylabel("U1")
    plt.show()

main.add_command(test)