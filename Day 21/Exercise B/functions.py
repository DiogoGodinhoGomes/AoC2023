import copy as cp

def get_mapa(filename):
    mp, ops = [], set()

    with open(filename) as file:
        for rw, line in enumerate(file):
            nl = list(line.strip())
            
            mp.append(nl)
            
            if "S" in nl:            
                ops.add((rw, nl.index("S"), 0, 0))
    
    return mp, ops

def get_steps(num, mp, ops):
    for i in range(num):        
        nps = set()
        
        for el in ops:            
            if mp[(el[0] + 1) % len(mp)][el[1] % len(mp[0])] != "#":
                c = 1 if el[0] + 1 >= len(mp) else 0
                
                nps.add(((el[0] + 1) % len(mp), el[1] % len(mp[0]), el[2] + c, el[3]))
            
            if mp[el[0] % len(mp)][(el[1] + 1) % len(mp[0])] != "#":
                c = 1 if el[1] + 1 >= len(mp[0]) else 0
                
                nps.add((el[0] % len(mp), (el[1] + 1) % len(mp[0]), el[2], el[3] + c))
            
            if mp[(el[0] - 1) % len(mp)][el[1] % len(mp[0])] != "#":
                c = 1 if el[0] - 1 < 0 else 0
                
                nps.add(((el[0] - 1) % len(mp), el[1] % len(mp[0]), el[2] - c, el[3]))
            
            if mp[el[0] % len(mp)][(el[1] - 1) % len(mp[0])] != "#":
                c = 1 if el[1] - 1 < 0 else 0
                
                nps.add((el[0] % len(mp), (el[1] - 1) % len(mp[0]), el[2], el[3] - c))
        
        ops = cp.deepcopy(nps)
    
    return ops

def get_diag_square(ops):
    tsm, cps, iy, ix, ay, ax = {}, {}, 0, 0, 0, 0

    for e in ops:
        iy, ix, ay, ax = min(iy, e[2]), min(ix, e[3]), max(ay, e[2]), max(ax, e[3])
        
        if (e[2], e[3]) not in cps:
            cps[(e[2], e[3])] = 1
        else:
            cps[(e[2], e[3])] += 1

    for e in cps:
        if cps[e] not in tsm:
            tsm[cps[e]] = 1
        else:
            tsm[cps[e]] += 1
    
    return tsm, cps, iy, ix, ay, ax

def print_diag_square(filename, n, cps, iy, ix, ay, ax):
    with open(filename, "a") as file:
        file.write(str(n) + ":\n")
        
        for r in range(iy, ay + 1):
            for c in range(ix, ax + 1):
                if (r, c) in cps:
                    file.write(str(cps[(r, c)]) + "\t")
                else:
                    file.write("0\t")
            
            file.write("\n")
        
        file.write("\n")