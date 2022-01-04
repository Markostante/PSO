'''
Marco Costante
MSc student in Artificial Intelligence
@ Alma Mater Studiorum, University of Bologna
July, 2021
'''

''' Examples of maximization of some test functions, with their specific domains and tuned hyperparameters. '''

import particle_swarm_optimization as pso
import test_functions as ts

''' Plate-shaped function with a global maximum. '''
def max_booth():
    boundaries = [(-10,10), (-10,10)]
    
    pso.optimize(ts.booth, boundaries, particle_size = 1000, iterations = 500, mm = 1)
    print("Expected: F(x) = 2594, at x = [-10, -10]")
    
''' Multimodal and highly complex function. '''
def max_dropwave():
    boundaries = [(-5.12,5.12), (-5.12,5.12)]
    
    pso.optimize(ts.dropwave, boundaries, particle_size = 1000, iterations = 500, mm = 1)
    print("Expected global maximum: F(x) = 1, at x = [0,0]")
    
''' Function with many local maxima and four global maxima. '''
def max_holdertable():
    boundaries = [(-10,10), (-10,10)]
    
    pso.optimize(ts.holdertable, boundaries, particle_size = 500, iterations = 1000, mm = 1)
    print("Expected global maximum: F(x) = 19.2085, at x = [+/- 8.05502, +/- 9.66459]")

''' Simple bowl function with 4 global maxima. '''
def max_bohachevsky():
    boundaries = [(-100,100), (-100,100)]
    
    pso.optimize(ts.bohachevsky, boundaries, particle_size = 500, iterations = 200, mm = 1)
    print("Expected global maximum: F(x) = 30000, at x = [+/- 100, +/- 100]")

''' Plate function with 2 global maxima. '''
def max_matyas():
    boundaries = [(-10,10), (-10,10)]
    
    pso.optimize(ts.matyas, boundaries, particle_size = 500, iterations = 200, mm = 1)
    print("Expected global maximum: F(x) = 100, at x = [-10, 10] or at x = [10, -10]")

''' The function has several local maxima. It is unimodal, and the global maximum has a small area relative to the search space. '''
def max_easom():
    boundaries = [(-100, 100), (-100, 100)]
    
    pso.optimize(ts.easom, boundaries, particle_size = 400, iterations = 250, mm = 1)
    print("Expected global maximum: F(x) = 1, at x = [pi, pi]")