import numpy as np

def check_for_start(landmap):
    count = 0
    
    landmap_len = len(landmap[0])
    
    assert(landmap_len > 0)
    
    s_coor = [-1, -1]
    
    for y in range(len(landmap)):
        assert(landmap_len == len(landmap[y]))
        
        for x in range(len(landmap[y])):
            if landmap[y][x] == 'S':
                s_coor = [x, y]
                
                count += 1
    
    if count == 0:
        print("Starting position not found!")
    elif count > 1:
        print("More than a single starting position found!")
    else:
        print("S =", s_coor)
    
    return s_coor[0], s_coor[1]

def get_init_paths(x, y, landmap):
    assert(x >= 0 and y >= 0)
    
    paths = []
    
    if x - 1 >= 0:
        if landmap[y][x - 1] == 'F' or landmap[y][x - 1] == '-' or landmap[y][x - 1] == 'L':
            paths.append([[x, y, 'W']])
    
    if y - 1 >= 0:
        if landmap[y - 1][x] == '7' or landmap[y - 1][x] == '|' or landmap[y - 1][x] == 'F':
            paths.append([[x, y, 'N']])
    
    if x + 1 < len(landmap[y]):
        if landmap[y][x + 1] == 'J' or landmap[y][x + 1] == '-' or landmap[y][x + 1] == '7':
            paths.append([[x, y, 'E']])
    
    if y + 1 < len(landmap):
        if landmap[y + 1][x] == 'L' or landmap[y + 1][x] == '|' or landmap[y + 1][x] == 'J':
            paths.append([[x, y, 'S']])
    
    assert(len(paths) == 2)
    
    return paths

def get_full_paths(xi, yi, landmap, new_landmap, paths):
    steps = 0
    
    loop = False
    
    while not loop:
        for elem in paths:
            x, y, d = elem[-1]
            
            new_landmap[y][x] = 'X'
            
            if d != 'X':
                if d == 'W':
                    if x - 1 >= 0:
                        direc = { 'F': 'S', '-': 'W', 'L': 'N', 'S': ''}
                        
                        elem.append([x - 1, y, direc[landmap[y][x - 1]]])
                    else:
                        elem.append([-1, -1, 'X'])
                elif d == 'N':
                    if y - 1 >= 0:
                        direc = { '7': 'W', '|': 'N', 'F': 'E', 'S': ''}
                        
                        elem.append([x, y - 1, direc[landmap[y - 1][x]]])
                    else:
                        elem.append([-1, -1, 'X'])
                elif d == 'E':
                    if x + 1 < len(landmap[y]):
                        direc = { 'J': 'N', '-': 'E', '7': 'S', 'S': ''}
                        
                        elem.append([x + 1, y, direc[landmap[y][x + 1]]])
                    else:
                        elem.append([-1, -1, 'X'])
                elif d == 'S':
                    if y + 1 < len(landmap):
                        direc = { 'L': 'E', '|': 'S', 'J': 'W', 'S': ''}
                        
                        elem.append([x, y + 1, direc[landmap[y + 1][x]]])
                    else:
                        elem.append([-1, -1, 'X'])
        
        steps += 1
        
        if paths[0][-1][0] == paths[1][-1][0] and paths[0][-1][1] == paths[1][-1][1]:
            if paths[0][-1][0] == xi and paths[0][-1][1] == yi:
                loop = True
                
                new_landmap[paths[0][-1][1]][paths[0][-1][0]] = 'X'
                
                paths[0].pop(-1)
                paths[1].pop(-1)

def find_index(used_path, new_landmap):
    y = 0

    index = -1

    path = np.array(used_path)[:,:2].astype('int32').tolist()

    while index < 0 and y < len(new_landmap):
        x = 0
        
        while index < 0 and x < len(new_landmap[y]):
            if new_landmap[y][x] == 'X':
                index = path.index([x, y])
            
            x += 1
        
        y += 1

    return index

def paint_inner(start_index, used_path, new_landmap):
    for index in range(len(used_path)):
        x, y, curr_d = used_path[(start_index + index) % len(used_path)]
        
        prev_d = used_path[(start_index + index - 1) % len(used_path)][2]
        
        for d in [prev_d, curr_d]:
            if d == 'N':
                i = 1
                
                while x + i < len(new_landmap[y]) and new_landmap[y][x + i] != 'X':
                    new_landmap[y][x + i] = 'I'
                    
                    i += 1
            elif d == 'E':
                i = 1
                
                while y + i < len(new_landmap) and new_landmap[y + i][x] != 'X':
                    new_landmap[y + i][x] = 'I'
                    
                    i += 1
            elif d == 'S':
                i = 1
                
                while x - i >= 0 and new_landmap[y][x - i] != 'X':
                    new_landmap[y][x - i] = 'I'
                    
                    i += 1
            elif d == 'W':
                i = 1
                
                while y - i >= 0 and new_landmap[y - i][x] != 'X':
                    new_landmap[y - i][x] = 'I'
                    
                    i += 1

def write_path(filename, content):
    with open(filename, "w") as file:
        for line in content:
            for char in line:
                file.write(char)
            
            file.write("\n")