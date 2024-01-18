import numpy as np

def get_and_expand_universe(filename, multiplier):
    universe = []
    
    with open(filename) as file:
        for line in file:
            universe.append(list(line.strip()))
    
    h_dists = [1] * len(universe[0])
    v_dists = [1] * len(universe)
    
    for row in range(len(universe)):
        if '#' not in universe[row]:
            v_dists[row] *= multiplier
    
    for col in range(len(universe)):
        if '#' not in np.array(universe)[:,col]:
            h_dists[col] *= multiplier
    
    return universe, [v_dists, h_dists]

def get_sum_shortest_distances(universe, dists):
    galaxies = []
    
    for i, row in enumerate(universe):
        for j, spot in enumerate(row):
            if spot == '#':
                galaxies.append((i, j))
    
    total = 0
    
    for i, g_one in enumerate(galaxies[:-1]):
        for j, g_two in enumerate(galaxies[i + 1:]):
            for k in range(2):
                temp_min = min(g_one[k], g_two[k])
                temp_max = max(g_one[k], g_two[k])
                
                temp_dist = 0
                
                for i in dists[k][temp_min: temp_max]:
                    temp_dist += i
                
                total += temp_dist
    
    return total