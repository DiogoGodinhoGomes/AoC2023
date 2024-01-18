import functions as fc

universe, dists = fc.get_and_expand_universe("code.txt", int(1e6))

total = fc.get_sum_shortest_distances(universe, dists)

print(total)