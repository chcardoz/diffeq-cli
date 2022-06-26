from cProfile import label
from email.policy import default
import click
import numpy as np
from ODESolver import RungeKutta4
from Pendulum import PendulumFull,PendulumSmallAngle
import matplotlib.pyplot as plt

@click.group()
def main():
    '''
    Welcome to the main program of the show, ladies and gentlemen
    '''
    pass

@click.command()
@click.option('-t','--time',nargs=2,type=click.Tuple([int,float]),required=True,show_default=True,default=(2,1e3))
@click.option('--sangle',is_flag=True,show_default=True,default=False,help="Include this flag if you want only the small angle approximation")
def test(time,sangle):
    '''
    A simple test function that I wrote to see what was going on
    '''
    from ODESolver import RungeKutta4
    from Pendulum import PendulumFull,PendulumSmallAngle
    import matplotlib.pyplot as plt
    periods,n = time
    t = periods*2*np.pi
    n = int(n)
    initial_conditions = [1.1*np.pi/2,1.1]
    time_points = np.linspace(0,t,n+1)
    _,(ax1) = plt.subplots(1,1)
    click.echo(f'Welcome to the solution, please check --help to know more about the commands')
    click.echo(f'Simulation time = {t} seconds')
    if sangle:
        click.echo(f'You have chosen to only plot the small angle approximation')
        f1 = PendulumSmallAngle(1,1)
        solver1 = RungeKutta4(f1) 
        solver1.set_initial_conditions(initial_conditions)
        u1,t1 = solver1.solve(time_points)
        ax1.plot(u1[:,0],u1[:,1])
        plt.show()
    else:
        click.echo(f'You have chosen to plot both types of solutions')
        f1 = PendulumSmallAngle(1,1)
        f2 = PendulumFull(1,1)
        solver1 = RungeKutta4(f1)
        solver2 = RungeKutta4(f2)
        solver1.set_initial_conditions(initial_conditions)
        solver2.set_initial_conditions(initial_conditions)
        u1,t1 = solver1.solve(time_points)
        u2,t2 = solver2.solve(time_points)
        ax1.plot(u1[:,0],u1[:,1],marker='.',label="Small angle approximation",linewidth=1,markersize=3)
        ax1.plot(u2[:,0],u2[:,1],color='red',marker='o',label="No approximation",linewidth=1,markersize=3)
        ax1.legend()
        ax1.grid()
        ax1.set_xlabel('$\Theta$')
        ax1.set_ylabel('$\dot{\Theta}$')
        plt.show()

main.add_command(test)