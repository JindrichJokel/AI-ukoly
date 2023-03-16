import random
import numpy as np
import matplotlib.pyplot as plt
from deap import algorithms, base, creator, tools

# Define the fitness function
def evaluateTerrain(individual):
    terrain = [0.5]
    terrain.extend(individual)
    return sum(terrain),  # Return a tuple to comply with the DEAP framework
t = [1.0, 0.5, 0.35, 0.1, 0.6, 0.3, 0.2, 0.1, 0.6]
# Define the toolbox
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)
toolbox = base.Toolbox()
toolbox.register("attr", random.uniform, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr, n=len(t)-2)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evaluateTerrain)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

# Define the parameters
population_size = 100
generations = 50
crossover_probability = 0.5
mutation_probability = 0.2

# Generate the initial population
population = toolbox.population(n=population_size)

# Start the evolution process
for generation in range(generations):
    offspring = algorithms.varAnd(population, toolbox, cxpb=crossover_probability, mutpb=mutation_probability)
    fits = toolbox.map(toolbox.evaluate, offspring)
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = fit
    population = toolbox.select(offspring, k=len(population))

# Get the best individual
best_individual = tools.selBest(population, k=1)[0]

# Generate the terrain map

terrain = [0.5] + list(best_individual) + [0.5]
fig, ax = plt.subplots()
x = range(len(t))
sea = [0.5 for i in range(len(t))]
ax.fill_between(x, sea, color="turquoise")
ax.fill_between(x, terrain, color="sandybrown")
ax.axis("off")
plt.show()