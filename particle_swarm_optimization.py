'''
Marco Costante
MSc student in Artificial Intelligence
@ Alma Mater Studiorum, University of Bologna
July, 2021
'''

import random
import matplotlib.pyplot as plt

''' Visualization '''
fig = plt.figure()
ax = fig.add_subplot()
fig.show()

class Particle:
    def __init__(self, bounds, initial_fitness):
        self.particle_position = []  # particle position
        self.particle_velocity = []  # particle velocity
        self.local_best_particle_position = []  # best position of the particle

        '''initial_fitness is equal to -inf for maximization problems, +inf for minimization problems'''
        self.fitness_local_best_particle_position = initial_fitness  # initial objective function value of the best particle position
        self.fitness_particle_position = initial_fitness  # objective function value of the particle position
  
        for i in range(nv):
            '''Initialize random velocity and random position within specified bounds'''
            self.particle_position.append(random.uniform(bounds[i][0], bounds[i][1]))  # generate random initial position
            self.particle_velocity.append(random.uniform(-1, 1))  # generate random initial velocity
  
    def evaluate(self, objective_function, mm):
        '''Compute the value of the objective function at the current position'''
        self.fitness_particle_position = objective_function(self.particle_position)

        '''Check if the current position is better than the previous one, if so updates the best position and the best fitness'''
        if mm == -1: #minimazation problems
            if self.fitness_particle_position < self.fitness_local_best_particle_position:
                self.local_best_particle_position = self.particle_position #update the local best
                self.fitness_local_best_particle_position = self.fitness_particle_position #update the fitness of the local best
        if mm == 1: #maximization problems
            if self.fitness_particle_position > self.fitness_local_best_particle_position:
                self.local_best_particle_position = self.particle_position #update the local best
                self.fitness_local_best_particle_position = self.fitness_particle_position #update the fitness of the local best

    def update_velocity(self, global_best_particle_position):
        '''Hyperparameters'''
        w = 0.75  # inertia constant
        c1 = 1  # cognitive constant
        c2 = 2  # social constant
        for i in range(nv):
            r1 = random.random()
            r2 = random.random()
            
            '''Cognitive velocity is based on the individual behaviour, while the social velocity is based on the swarm behaviour'''
            cognitive_velocity = c1 * r1 * (self.local_best_particle_position[i] - self.particle_position[i])
            social_velocity = c2 * r2 * (global_best_particle_position[i] - self.particle_position[i])

            self.particle_velocity[i] = w * self.particle_velocity[i] + cognitive_velocity + social_velocity
    
    def update_position(self, bounds):
        for i in range(nv):
            self.particle_position[i] = self.particle_position[i] + self.particle_velocity[i]

            '''If the position it's out of the user-defined boundaries, we can push the particle in'''

            #check and repair to satisfy the upper bounds
            if self.particle_position[i] > bounds[i][1]:
                self.particle_position[i] = bounds[i][1]
            #check and repair to satisfy the lower bounds
            if self.particle_position[i] < bounds[i][0]:
                self.particle_position[i] = bounds[i][0]


def optimize(objective_function, bounds, particle_size, iterations, mm):
    '''Discrimination between minimization and maximization problem'''
    if mm == -1:
        initial_fitness = float("inf") #for minimization problem
    if mm == 1:
        initial_fitness = -float("inf") #for maximization problem

    global nv
    nv = 2
    
    fitness_global_best_particle_position = initial_fitness
    global_best_particle_position = []

    '''Initialization of the swarm'''
    swarm_particle = []
    for i in range(particle_size):
        swarm_particle.append(Particle(bounds, initial_fitness))
    
    '''List used to record the best fitness in each iteration'''
    A = []

    '''Optimization loop'''
    for i in range(iterations):
        '''Evaluate the fitness of each particle and updates the individual best position'''
        for j in range(particle_size):
            swarm_particle[j].evaluate(objective_function, mm)

            '''Check if the current particle it's the best of the swarm, if so, update best position and best fitness of the swarm'''
            if mm == -1:
                if swarm_particle[j].fitness_particle_position < fitness_global_best_particle_position:
                    global_best_particle_position = list(swarm_particle[j].particle_position)
                    fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)
            if mm == 1:
                if swarm_particle[j].fitness_particle_position > fitness_global_best_particle_position:
                    global_best_particle_position = list(swarm_particle[j].particle_position)
                    fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)
        
        '''Update positions and velocities of the swarm'''
        for j in range(particle_size):
            swarm_particle[j].update_velocity(global_best_particle_position)
            swarm_particle[j].update_position(bounds)
        
        A.append(fitness_global_best_particle_position) #record the best fitness

        '''Visualization'''
        ax.plot(A, color='r')
        fig.canvas.draw()
        ax.set_xlim(left=max(0, i - iterations), right = i + 3)

    print('Optimal solution: ', global_best_particle_position)
    print('Objective function value: ', fitness_global_best_particle_position)
    plt.show()