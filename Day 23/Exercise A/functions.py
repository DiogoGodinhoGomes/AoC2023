import copy as cp

def get_mapa(filename):
    mp, st = [], set()

    with open(filename) as file:
        for l, line in enumerate(file):
            mp.append(list(line.strip()))

    sp, fp = (0, mp[0].index(".")), (len(mp) - 1, mp[len(mp) - 1].index("."))

    for r in mp:
        for c in r:
            st.add(c)

    assert(len(st) == 4)
    
    return mp, sp, fp

def get_paths(mp, sp, fp):
    i, pt, ls = 0, [[cp.deepcopy(sp)]], []

    while i < len(pt):
        while pt[i][-1] != (-1, -1) and pt[i][-1] != fp:
            p = pt[i][-1]
            
            assert(mp[p[0]][p[1]] != "#")
            
            if mp[p[0]][p[1]] == ".":
                np = []
                
                if p[0] - 1 >= 0 and mp[p[0] - 1][p[1]] != "#" and (p[0] - 1, p[1]) not in pt[i]:
                    np.append((p[0] - 1, p[1]))
                
                if p[1] - 1 >= 0 and mp[p[0]][p[1] - 1] != "#" and (p[0], p[1] - 1) not in pt[i]:
                    np.append((p[0], p[1] - 1))
                
                if p[0] + 1 < len(mp) and mp[p[0] + 1][p[1]] != "#" and (p[0] + 1, p[1]) not in pt[i]:
                    np.append((p[0] + 1, p[1]))
                
                if p[1] + 1 < len(mp[p[0]]) and mp[p[0]][p[1] + 1] != "#" and (p[0], p[1] + 1) not in pt[i]:
                    np.append((p[0], p[1] + 1))
                
                if len(np) == 0:
                    p = (-1, -1)
                else:
                    for j in range(len(np) - 1, -1, -1):
                        if j == 0:                        
                            pt[i].append(cp.deepcopy(np[j]))
                        else:
                            tp = cp.deepcopy(pt[i])
                            
                            tp.append(cp.deepcopy(np[j]))
                            
                            pt.append(tp)
            elif mp[p[0]][p[1]] == "v":
                if p[0] + 1 < len(mp) and mp[p[0] + 1][p[1]] != "#" and (p[0] + 1, p[1]) not in pt[i]:
                    pt[i].append((p[0] + 1, p[1]))
                else:
                    pt[i].append((-1, -1))
            elif mp[p[0]][p[1]] == ">":
                if p[1] + 1 < len(mp[p[0]]) and mp[p[0]][p[1] + 1] != "#" and (p[0], p[1] + 1) not in pt[i]:
                    pt[i].append((p[0], p[1] + 1))
                else:
                    pt[i].append((-1, -1))
            else:
                assert(False)
        
        if pt[i][-1] == (-1, -1):
            pt.pop(i)
        else:
            i += 1

    for i in pt:
        ls.append(len(i) - 1)
    
    return max(ls), pt

def print_paths(mp, pt):
    for j, p in enumerate(pt):
        print(j, p[0], p[-1], len(p) - 1)
        
        nm = cp.deepcopy(mp)
        
        for e in p:
            nm[e[0]][e[1]] = "O"
        
        for k, r in enumerate(nm):
            nm[k] = "".join(r) + "\t" + "".join(mp[k])
        
        for r in nm:
            print(r)
        
        print()