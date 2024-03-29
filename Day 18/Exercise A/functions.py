import copy as cp
from collections import deque

def read_instr(filename):
    instr = []

    with open(filename) as file:
        for line in file:
            instr.append(line.strip().replace("(","").replace(")","").split(" "))
    
    return instr

def get_mapa(instr):
    mapa, pos = deque([ deque(["#"]) ]), [0, 0]

    for elem in instr:
        for i in range(int(elem[1])):
            if elem[0] == "R":
                if pos[1] + 1 >= len(mapa[pos[0]]):
                    for j in range(len(mapa)):
                        mapa[j].append(".")
                
                pos[1] += 1
            elif elem[0] == "D":
                if pos[0] + 1 >= len(mapa):
                    mapa.append(deque(["."] * len(mapa[pos[0]])))
                
                pos[0] += 1
            elif elem[0] == "L":
                if pos[1] - 1 < 0:
                    for j in range(len(mapa)):
                        mapa[j].appendleft(".")
                    
                    pos[1] += 1
                
                pos[1] -= 1
            elif elem[0] == "U":
                if pos[0] - 1 < 0:
                    mapa.appendleft(deque(["."] * len(mapa[pos[0]])))
                    
                    pos[0] += 1
                
                pos[0] -= 1
            else:
                assert(False)
            
            mapa[pos[0]][pos[1]] = "#"
    
    for i in range(len(mapa)):
        mapa[i] = list(mapa[i])
    
    return list(mapa)

def get_initial(mapa):
    pos, d = [0, 0], "N"

    while mapa[pos[0]][pos[1]] != "#" and pos[0] < len(mapa):
        if pos[1] + 1 >= len(mapa[pos[0]]):
            pos[1] = 0
            
            pos[0] += 1
        else:
            pos[1] += 1

    return pos, d

def get_borders(mapa, init_pos, init_d):
    i, pos, d, borders = 0, cp.deepcopy(init_pos), cp.deepcopy(init_d), []

    assert(init_d == "E" or init_d == "S" or init_d == "W" or init_d == "N")

    assert(init_pos[0] >= 0 and init_pos[1] >= 0 and init_pos[0] < len(mapa) and init_pos[1] < len(mapa[init_pos[0]]))

    while i == 0 or pos != init_pos or d != init_d:
        borders.append([pos[0], pos[1], d])
        
        if d == "E":
            if pos[1] + 1 < len(mapa[pos[0]]) and mapa[pos[0]][pos[1] + 1] == "#":
                pos[1] += 1
            elif pos[0] - 1 >= 0 and mapa[pos[0] - 1][pos[1]] == "#":
                pos[0] -= 1
                
                d = "N"
            elif pos[0] + 1 < len(mapa) and mapa[pos[0] + 1][pos[1]] == "#":
                pos[0] += 1
                
                d = "S"
            else:
                assert(False)
        elif d == "S":
            if pos[0] + 1 < len(mapa) and mapa[pos[0] + 1][pos[1]] == "#":
                pos[0] += 1
            elif pos[1] + 1 < len(mapa[pos[0]]) and mapa[pos[0]][pos[1] + 1] == "#":
                pos[1] += 1
                
                d = "E"
            elif pos[1] - 1 >= 0 and mapa[pos[0]][pos[1] - 1] == "#":
                pos[1] -= 1
                
                d = "W"
            else:
                assert(False)
        elif d == "W":
            if pos[1] - 1 >= 0 and mapa[pos[0]][pos[1] - 1] == "#":
                pos[1] -= 1
            elif pos[0] + 1 < len(mapa) and mapa[pos[0] + 1][pos[1]] == "#":
                pos[0] += 1
                
                d = "S"
            elif pos[0] - 1 >= 0 and mapa[pos[0] - 1][pos[1]] == "#":
                pos[0] -= 1
                
                d = "N"
            else:
                assert(False)
        elif d == "N":
            if pos[0] - 1 >= 0 and mapa[pos[0] - 1][pos[1]] == "#":
                pos[0] -= 1
            elif pos[1] - 1 >= 0 and mapa[pos[0]][pos[1] - 1] == "#":
                pos[1] -= 1
                
                d = "W"
            elif pos[1] + 1 < len(mapa[pos[0]]) and mapa[pos[0]][pos[1] + 1] == "#":
                pos[1] += 1
                
                d = "E"
            else:
                assert(False)
        else:
            assert(False)
        
        assert(d == "E" or d == "S" or d == "W" or d == "N")
        
        assert(pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(mapa) and pos[1] < len(mapa[init_pos[0]]))
        
        i += 1
    
    return borders

def paint_curr(mapa, y, x, d):
    j = 1
    
    if d == "E":
        while y + j < len(mapa) and mapa[y + j][x] != "#":
            mapa[y + j][x] = "O"
            
            j += 1
    elif d == "S":
        while x - j >= 0 and mapa[y][x - j] != "#":
            mapa[y][x - j] = "O"
            
            j += 1
    elif d == "W":
        while y - j >= 0 and mapa[y - j][x] != "#":
            mapa[y - j][x] = "O"
            
            j += 1
    elif d == "N":
        while x + j < len(mapa[y]) and mapa[y][x + j] != "#":
            mapa[y][x + j] = "O"
            
            j += 1
    else:
        assert(False)

def paint_all(mapa, borders):
    for i, elem in enumerate(borders):        
        paint_curr(mapa, elem[0], elem[1], elem[2])
        
        paint_curr(mapa, elem[0], elem[1], borders[(i + 1) % len(borders)][2])

def get_total(mapa):
    total = 0

    for i in mapa:
        for j in i:
            if j != ".":
                total += 1

    return total