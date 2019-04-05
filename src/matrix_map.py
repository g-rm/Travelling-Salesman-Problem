import numpy as np
import random
import sys

def initialize_map(min_dist, N):
    
    map = np.zeros((N,N))
    vector = []
    for i in range(0,N):
        for j in range(0, i):
            randomic = random.randint(min_dist,100)
            map[i][j] = randomic
            map[j][i] = map[i][j]
                
    return map
    

if __name__ == "__main__":
    
    map = initialize_map(min_dist=10, N=12)
    print(map)
