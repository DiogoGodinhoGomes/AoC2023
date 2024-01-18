import functions as fc

landmap = []
new_landmap = []

with open("code.txt") as file:
    for line in file:
        landmap.append(list(line.strip()))
        
        new_landmap.append(['.'] * len(landmap[-1]))

xi, yi = fc.check_for_start(landmap)

if xi != -1 and yi != -1:    
    paths = fc.get_init_paths(xi, yi, landmap)
    
    fc.get_full_paths(xi, yi, landmap, new_landmap, paths)
    
    index = fc.find_index(paths[0], new_landmap)
    
    if paths[0][index][2] == 'N' or paths[0][index][2] == 'E':
        choice = 0
    else:
        choice = 1
    
    fc.paint_inner(index, paths[choice], new_landmap)
    
    count = 0
    
    for row in new_landmap:
        for elem in row:
            if elem == 'I':
                count += 1
    
    print(count)