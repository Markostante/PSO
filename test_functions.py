'''
Marco Costante
MSc student in Artificial Intelligence
@ Alma Mater Studiorum, University of Bologna
July, 2021
'''

''' Test functions for optimization based on: https://en.wikipedia.org/wiki/Test_functions_for_optimization '''

import numpy as np

def ackley(x):
    return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x[0]**2 + x[1]**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x[0]) + np.cos(2 * np.pi * x[1]))) + np.e + 20

def beale(x):
    return (1.5 - x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0]*x[1]**2)**2 + (2.625 - x[0] + x[0]*x[1]**3)**2

def bukin(x):
    return 100*np.sqrt(abs(x[1] - 0.01*x[0]**2)) + 0.01*abs(x[0] + 10)

def levi(x):
    return np.sin(3*np.pi*x[0])**2 + ((x[0] - 1)**2)*(1 + np.sin(3*np.pi*x[1])**2) + ((x[1] - 1)**2)*(1 + np.sin(2*np.pi*x[1])**2)

def eggholder(x):
    return -(x[1] + 47)*np.sin(np.sqrt(abs((x[0]/2) + x[1] + 47))) - x[0]*np.sin(np.sqrt(abs(x[0] - (x[1] + 47))))

def cormick(x):
    return np.sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5*x[0] + 2.5*x[1] + 1

def schaffer(x):
    return 0.5 + (np.sin(x[0]**2 - x[1]**2)**2 - 0.5)/(1 + 0.001*(x[0]**2 + x[1]**2))**2

def booth(x):
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2

def dropwave(x):
    return (1 + np.cos(12*np.sqrt(x[0]**2 + x[1]**2))) / (0.5 * (x[0]**2 + x[1]**2) + 2)

def holdertable(x):
    return abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(abs(1 - (np.sqrt(x[0]**2 + x[1]**2)/np.pi))))

def bohachevsky(x):
    return x[0]**2 + 2*x[1]**2 - 0.3*np.cos(3*np.pi*x[0]) - 0.4*np.cos(4*np.pi*x[1]) + 0.7

def matyas(x):
    return 0.26 * (x[0]**2 + x[1]**2) - 0.48*x[0]*x[1]

def easom(x):
    return -(-np.cos(x[0])*np.cos(x[1])*np.exp(-((x[0] - np.pi)**2 + (x[1] - np.pi)**2)))