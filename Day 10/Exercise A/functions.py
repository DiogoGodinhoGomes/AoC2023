def check_for_start(landmap):
    count = 0
    
    landmap_len = len(landmap)
    
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

def get_init_paths(landmap, x, y):
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