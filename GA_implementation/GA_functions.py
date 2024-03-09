# Author : Eng. Sayed Salem

import numpy as np
import matplotlib.pyplot as plt

def fitness(population, equation):
    '''
    Calculate the fitness function for each solution in the given population and the input equation
    '''
    return np.sum(population * equation, axis=1)

#
def parents_selection(fitness_values, population, number_parents):
    '''
    Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    '''
    # create an empty array to save the selected parents !!
    parents = np.empty(shape=(number_parents, population.shape[1]))
    for idx in range(number_parents):
        max_idx = np.argmax(fitness_values)  # get the maxmimum value
        parents[idx, :] = population[max_idx, :]
        fitness_values[max_idx] = float('-inf')  # assign the selected value with a very minimum number !!

    return parents


def crossover(parents, offspring_size):
    '''
    Creating an offsping from every consecutive parents for the next generation.
    '''
    offspring = np.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually, it is at the center.
    crossover_point = int(offspring_size[1] / 2)

    number_parents = parents.shape[0]
    for idx in range(offspring_size[0]):
        parent_idx1 = idx
        parent_idx2 = (idx + 1) % number_parents
        offspring[idx, :crossover_point] = parents[parent_idx1, :crossover_point]
        offspring[idx, crossover_point:] = parents[parent_idx2, crossover_point:]
    return offspring

def mutation(offspring, num_mutation):
    '''
    Making a mutation to the offspring  of the next generation .
    '''
    mutation_step = int(offspring.shape[1] / num_mutation)

    for idx in range(offspring.shape[0]):
        mutation_step -= 1  ## cuz of zero based numpy arrays !!
        for mutation_idx in range(mutation_step, offspring.shape[1], num_mutation):
            offspring[idx][mutation_idx] += numpy.random.uniform(-1.0, 1.0, 1)
    return offspring


def output_results(output):
    plt.plot(output)
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.show()


import numpy



def select_mating_pool(pop, fitness, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))  ## return something like that ((array([idx]),) where idx is the max fitness index
        max_fitness_idx = max_fitness_idx[0][0]  ## so index [0][0] will return just idx
        parents[parent_num, :] = pop[max_fitness_idx, :]
        print(f"Parent No. {parent_num} : {max_fitness_idx}")
        fitness[max_fitness_idx] = -99999999999
    return parents



