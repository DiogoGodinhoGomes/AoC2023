import copy as cp
import numpy as np

def read_instr(filename):
    instr = []

    with open(filename) as file:
        for line in file:
            nl = line.replace("#", "").replace("(", "").replace(")", "")
            
            instr.append(nl.strip().split(" "))
    
    return instr

def convert_instr(color, instr):
    dtnr = { 0: "R", 1: "D", 2: "L", 3: "U"}
    
    for i in range(len(instr)):
        if color:
            instr[i][0] = dtnr[int(instr[i][2][-1])]
            
            instr[i][1] = int(instr[i][2][:-1], 16)
        else:
            instr[i][1] = int(instr[i][1])
        
        instr[i].pop()

def get_corners(instr):
    corners, new_corners, curr, vp, hp = [], [], [0, 0], 0, 0

    corners.append(cp.deepcopy(curr))

    for i in instr:
        if i[0] == "R":
            curr[1] += i[1]
            
            hp += i[1]
        elif i[0] == "D":
            curr[0] += i[1]
            
            vp += i[1]
        elif i[0] == "L":
            curr[1] -= i[1]
            
            hp += i[1]
        elif i[0] == "U":
            curr[0] -= i[1]
            
            vp += i[1]
        else:
            assert(False)
        
        corners.append(cp.deepcopy(curr))
    
    assert(corners[0] == corners[-1])

    corners.pop()

    min_y, min_x = min(np.array(corners)[:,0]), min(np.array(corners)[:,1])
    
    corners = np.array(corners) - [min_y, min_x]
    
    corners = corners[corners[:, 1].argsort()]

    corners = corners[corners[:, 0].argsort()].tolist()
    
    max_y, max_x = max(np.array(corners)[:,0]), max(np.array(corners)[:,1])
    
    i = 0
    
    while i < len(corners):
        nr = [corners[i][0], [corners[i][1]]]
        
        j = i + 1
        
        while j < len(corners) and corners[j][0] == corners[i][0]:
            nr[1].append(corners[j][1])
            
            j += 1
        
        new_corners.append(cp.deepcopy(nr))
        
        i = j
    
    for i in range(len(new_corners)):
        new_corners[i] = [new_corners[i][0], sorted(new_corners[i][1])]
    
    return new_corners, max_y + 1, max_x + 1, vp, hp