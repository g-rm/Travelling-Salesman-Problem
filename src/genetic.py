import random

def evalMinDist(dist_matrix, individual):
#fitness function

    score = 0
    n_routes = len(individual) - 1
    for i in range(n_routes):
        j = individual[i]
        k = individual[i+1]
        score += dist_matrix[j][k]
    
    score += dist_matrix[n_routes][0]
    
    #iterable
    return (score), 



def mutate(individual):
    
    i, j = random.sample(range(len(individual)), 2)
    individual[i], individual[j] = individual[j], individual[i]
        
    return individual,
