import copy as cp

def get_mapa(filename):
    mp, ops = [], set()

    with open(filename) as file:
        for rw, line in enumerate(file):
            nl = list(line.strip())
            
            mp.append(nl)
            
            if "S" in nl:            
                ops.add((rw, nl.index("S")))
    
    return mp, ops

def get_steps(st, mp, ops):
    for i in range(st):
        nps = set()
        
        for el in ops:
            if el[0] + 1 < len(mp) and mp[el[0] + 1][el[1]] != "#":
                nps.add((el[0] + 1, el[1]))
            
            if el[1] + 1 < len(mp[el[0]]) and mp[el[0]][el[1] + 1] != "#":
                nps.add((el[0], el[1] + 1))
            
            if el[0] - 1 >= 0 and mp[el[0] - 1][el[1]] != "#":
                nps.add((el[0] - 1, el[1]))
            
            if el[1] - 1 >= 0 and mp[el[0]][el[1] - 1] != "#":
                nps.add((el[0], el[1] - 1))
        
        ops = cp.deepcopy(nps)
    
    return len(ops)