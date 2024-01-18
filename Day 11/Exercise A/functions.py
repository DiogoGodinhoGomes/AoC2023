import numpy as np

def get_and_expand_universe(filename):
    universe = []

    with open(filename) as file:
        for line in file:
            universe.append(list(line.strip()))

    rows = []
    cols = []

    for row in range(len(universe)):
        if '#' not in universe[row]:
            rows.append(row)

    for col in range(len(universe)):
        if '#' not in np.array(universe)[:,col]:
            cols.append(col)

    for i in sorted(rows, reverse = True):
        universe.insert(i, ['.'] * len(universe[0]))

    for i in sorted(cols, reverse = True):
        for j in range(len(universe)):
            universe[j].insert(i, '.')
    
    return universe

def get_sum_shortest_distances(universe):
    galaxies = []

    for i, row in enumerate(universe):
        for j, spot in enumerate(row):
            if spot == '#':
                galaxies.append((i, j))

    total = 0

    for i, g_one in enumerate(galaxies[:-1]):
        for j, g_two in enumerate(galaxies[i + 1:]):
            total += abs(g_one[0] - g_two[0]) + abs(g_one[1] - g_two[1])

    return total