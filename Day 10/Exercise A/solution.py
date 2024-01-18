import functions as fc

landmap = []

with open("code.txt") as file:
    for line in file:
        landmap.append(list(line.strip()))

xi, yi = fc.check_for_start(landmap)

if xi != -1 and yi != -1:
    paths = fc.get_init_paths(landmap, xi, yi)
    
    loop = False
    
    while not loop:
        for elem in paths:
            x, y, d = elem[-1]
            
            if d != 'X':
                if d == 'W':
                    if x - 1 >= 0:
                        direc = { 'F': 'S', '-': 'W', 'L': 'N'}
                        
                        elem.append([x - 1, y, direc[landmap[y][x - 1]]])
                    else:
                        elem.append([-1, -1, 'X'])
                elif d == 'N':
                    if y - 1 >= 0:
                        direc = { '7': 'W', '|': 'N', 'F': 'E'}
                        
                        elem.append([x, y - 1, direc[landmap[y - 1][x]]])
                    else:
                        elem.append([-1, -1, 'X'])
                elif d == 'E':
                    if x + 1 < len(landmap[y]):
                        direc = { 'J': 'N', '-': 'E', '7': 'S'}
                        
                        elem.append([x + 1, y, direc[landmap[y][x + 1]]])
                    else:
                        elem.append([-1, -1, 'X'])
                elif d == 'S':
                    if y + 1 < len(landmap):
                        direc = { 'L': 'E', '|': 'S', 'J': 'W'}
                        
                        elem.append([x, y + 1, direc[landmap[y + 1][x]]])
                    else:
                        elem.append([-1, -1, 'X'])
        
        if paths[0][-1][0] == paths[1][-1][0] and paths[0][-1][1] == paths[1][-1][1]:
            if paths[0][-1][0] != xi or paths[0][-1][1] != yi:
                loop = True
    
    print("Steps =", len(paths[0]) - 1)