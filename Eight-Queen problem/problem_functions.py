import numpy as np
import matplotlib.pyplot as plt


def init_population(samples):
    return np.random.randint(8, size=(samples, 8))


def calc_penalty(sample):
    penalty = np.zeros(shape=len(sample))

    for i in range(len(sample)):
        for j in range(len(sample)):
            if i == j:
                continue
            dist = abs(i - j)
            if sample[i] == sample[j]:
                penalty[i] -= 1
            elif abs(sample[i] - sample[j]) == dist:
                penalty[i] -= 1
    return np.sum(penalty)


def fitness(population):
    fitness_values=[]
    for sample in range(population.shape[0]):
        fitness_values.append(calc_penalty(population[sample]))
    return fitness_values


p = np.array([ [4 ,0 ,7 ,3 ,1 ,6, 2 ,5]])
print(fitness(p))

def parents_selection(population, fitness_values, number_parents):
    tmp = abs(np.min(fitness_values)) + 1
    probs = fitness_values + tmp
    probs = probs / probs.sum()
    N = len(fitness_values)
    indices = np.arange(N)
    choices = np.random.choice(a=indices, size=number_parents, p=probs)
    parents = population[choices, :]
    return parents


def crossover(parents, offspring_size, pc):
    '''
    Creating an offsping from every consecutive parents for the next generation.
    '''
    offspring = np.empty(offspring_size)

    random_number = np.random.random()
    if random_number <= pc:
        #The point at which crossover takes place between two parents. Usually, it is at the center.
        crossover_point = int(offspring_size[1] / 2)

        number_parents = parents.shape[0]
        for idx in range(offspring_size[0]):
            parent_idx1 = idx
            parent_idx2 = (idx + 1) % number_parents
            offspring[idx, :crossover_point] = parents[parent_idx1, :crossover_point]
            offspring[idx, crossover_point:] = parents[parent_idx2, crossover_point:]
    else:
        for idx in range(offspring_size[0]):
            offspring[idx] = parents[idx]
    return offspring


def mutation(offspring, num_mutation=1):
    '''
    Making a mutation to the offspring  of the next generation .
    '''
    mutation_step = int(offspring.shape[1] / num_mutation)

    for idx in range(offspring.shape[0]):
        mutation_step -= 1  ## cuz of zero based numpy arrays !!
        for mutation_idx in range(mutation_step, offspring.shape[1], num_mutation):
            offspring[idx][mutation_idx] = np.random.randint(8)
    return offspring

def output_results(output):
    plt.plot(output)
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.show()




