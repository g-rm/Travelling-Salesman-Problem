import random
from functools import partial
from deap import base, creator, tools, algorithms
import numpy as np
from genetic import *
from matrix_map import *
import matplotlib.pyplot as plt

#%config InlineBackend.figure_format = 'svg'

params = {'figure.figsize': [5, 5],
          'axes.labelsize': 16,
          'axes.titlesize':18,
          'font.size': 16,
          'legend.fontsize': 10,
          'xtick.labelsize': 12,
          'ytick.labelsize': 12
    }

plt.rcParams.update(params)
plt.style.use('seaborn-notebook')



#comma forces tuple
fit = creator.create('FitnessMin', base.Fitness, weights=(-1.0,))
ind = creator.create('Individual', list, fitness=creator.FitnessMin)

#creates distance matrix
n=500
dist_matrix = initialize_map(10, n)

#some toolbox configurations
gen_idx = partial(random.sample, range(n), n)
toolbox = base.Toolbox()

#creates individual function
toolbox.register('individual', tools.initIterate, creator.Individual, gen_idx)

#creates population function
toolbox.register('population', tools.initRepeat, list, toolbox.individual)

#creates fitness function
toolbox.register('evaluate', evalMinDist, dist_matrix)

#creates matching function (toolbox's native)
toolbox.register('mate', tools.cxUniformPartialyMatched, indpb=.5)

#creates mutation function
toolbox.register('mutate', mutate)

#creates selection method
toolbox.register('select', tools.selTournament, tournsize=3)


def main():
    
    #creates population
    pop = toolbox.population(n=25)
    #hall of fame
    hof = tools.HallOfFame(1)
    #statistics
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    
    stats.register('avg' , np.mean)
    stats.register('min', np.min)
    stats.register('max', np.max)
    
    #ea = evolutionary algorithm
    pop, logbook = algorithms.eaSimple(pop, toolbox, cxpb=.8, mutpb=0.2, ngen=800,
                                       stats=stats, halloffame=hof, verbose=True)
    
    return pop, logbook, hof

if __name__ == "__main__":
    pop, log, hof = main()
    print("Best individual is: %s\nwith fitness: %s" % (hof[0], hof[0].fitness))
    
    gen, avg, min_, max_ = log.select("gen", "avg", "min", "max")
    plt.plot(gen, avg, label="average", linewidth=3)
    plt.plot(gen, min_, label="minimum", linewidth=3)
    plt.plot(gen, max_, label="maximum", linewidth=3)
    plt.title('Salesman Routes Distance')
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.savefig("../assets/evolution")
