import functions as fc

maps = fc.get_maps("code.txt")

axes, total = fc.get_axes_total(maps)

new_axes = fc.get_new_axes(maps)

new_total = 0

for i, elem in enumerate(new_axes):
    for v in elem:
        if v not in axes[i]:
            new_total += v

for i, elem in enumerate(axes):
    assert(len(elem) == 1)
    
    assert(len(new_axes[i]) == 2)

print(total, "\t", new_total)