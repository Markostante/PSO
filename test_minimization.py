'''
Marco Costante
MSc student in Artificial Intelligence
@ Alma Mater Studiorum, University of Bologna
July, 2021
'''

''' Examples of minimization of some test functions, with their specific domains and tuned hyperparameters. '''

import particle_swarm_optimization as pso
import test_functions as ts

''' Non-convex function characterized by a nearly flat outer region, and a large hole at the centre. The function has many local minima. '''
def min_ackley():             
    boundaries = [(-3.2768, 3.2768), (-32.768, 32.768)] 
    
    pso.optimize(ts.ackley, boundaries, particle_size = 1500, iterations = 1500, mm = -1)
    print("Expected global minimum: F(x) = 0, at x = [0, 0]")

''' A multimodal function with sharp peaks at the corners of the input domain. '''    
def min_beale():
    boundaries = [(-4.5, 4.5), (-4.5, 4.5)]
    
    pso.optimize(ts.beale, boundaries, particle_size = 1500, iterations = 400, mm = -1)
    print("Expected global minimum: F(x) = 0, at x = [3, 0.5]")

''' Function that has many local minima, all of which lie in a ridge. '''
def min_bukin():
    #Boundaries restricted from [(-15,-5),(-3,3)] to reduce computational time
    boundaries = [(-12, -8),(-2, 2)] 
    
    pso.optimize(ts.bukin, boundaries, particle_size = 2500, iterations = 2400, mm = -1)
    print("Expected global minimum: F(x) = 0, at x = [-10, 1]")

''' Function with many local minima. '''
def min_levi():
    boundaries = [(-10, 10), (-10, 10)] 
    
    pso.optimize(ts.levi, boundaries, particle_size = 700, iterations = 500, mm = -1)
    print("Expected global minimum: F(x) = 0, at x = [1, 1]")

''' Plate-shaped function, search with asymmetric domains. '''
def min_cormick():
    boundaries = [(-1.5, 4), (-3, 4)]
    
    pso.optimize(ts.cormick, boundaries, particle_size = 500, iterations = 500, mm = -1)
    print("Expected global minimum: F(x) = -1.9132, at x = [-0.54719, -1.54719]")

''' Function with many local minima and a large domain. '''
def min_schaffer():
    boundaries = [(-100, 100), (-100, 100)]
    
    pso.optimize(ts.schaffer, boundaries, particle_size = 1500, iterations = 1000, mm = -1)
    print("Expected global minimum: F(x) = 0, at x = [0, 0]")