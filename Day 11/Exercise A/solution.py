import functions as fc

universe = fc.get_and_expand_universe("code.txt")

total = fc.get_sum_shortest_distances(universe)

print(total)