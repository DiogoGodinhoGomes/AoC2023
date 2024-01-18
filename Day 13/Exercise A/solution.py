import numpy as np
import functions as fc

maps = fc.get_maps("code.txt")

total = 0

for i in maps:
    rows = fc.get_sym_axis(i)
    
    cols = fc.get_sym_axis(np.array(i).transpose().tolist())
    
    assert(rows == 0 or cols == 0)
    
    total += 100 * rows + cols

print(total)