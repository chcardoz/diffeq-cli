import click
import numpy as np
from DiffEqs import exponentialDecay

@click.group()
def main():
    '''
    Welcome to the main program of the show, ladies and gentlemen
    '''
    pass

@click.command()
@click.option('-t','--time',nargs=2,type=click.Tuple([int,float]),required=True,show_default=True,default=(3,0.5))
def test(time):
    '''
    A simple test function that I wrote to see what was going on
    '''
    t, dt = time
    click.echo(f'Welcome to the solution, please check --help to know more about the commands')
    click.echo(f'Simulation time = {t} seconds\nSimulation time step = {dt} seconds')

main.add_command(test)