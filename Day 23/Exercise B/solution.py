import time as tm
import functions as fc

st = tm.time()

mp, sp, fp = fc.get_mapa("code.txt")

nl, nd = fc.get_nodes(mp, sp, fp)

paths = fc.get_possible_paths(nl, nd)

print(fc.get_longest_length(nl, nd, paths))