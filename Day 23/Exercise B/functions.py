import copy as cp
import time as tm

def get_mapa(filename):
    mp, st = [], set()

    with open(filename) as file:
        for l, line in enumerate(file):
            mp.append(list(line.replace("v",".").replace(">",".").strip()))

    sp, fp = (0, mp[0].index(".")), (len(mp) - 1, mp[len(mp) - 1].index("."))

    for r in mp:
        for c in r:
            st.add(c)

    assert(len(st) == 2)
    
    return mp, sp, fp

def get_paths(mp, sp, fp, st):
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
                    pt[i].append((-1, -1))
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
        
        print(i, len(pt), tm.time() - st)

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

def get_nodes(mp, sp, fp):
    i, pt = 0, [[cp.deepcopy(sp)]]

    nl, vs, nd = [sp], [], [{}]

    while i < len(pt):
        if len(pt[i]) > 1 and pt[i][-1] in vs:
            pt[i].append((-1, -1))
        
        while pt[i][-1] != (-1, -1):
            p = pt[i][-1]
            
            assert(mp[p[0]][p[1]] != "#")
            
            if mp[p[0]][p[1]] == ".":
                np = []
                
                if p not in vs:
                    vs.append(p)
                
                t = (p[0] - 1, p[1])
                
                if p[0] - 1 >= 0 and mp[p[0] - 1][p[1]] != "#" and t not in pt[i]:
                    np.append(t)
                
                t = (p[0], p[1] - 1)
                
                if p[1] - 1 >= 0 and mp[p[0]][p[1] - 1] != "#" and t not in pt[i]:
                    np.append(t)
                
                t = (p[0] + 1, p[1])
                
                if p[0] + 1 < len(mp) and mp[p[0] + 1][p[1]] != "#" and t not in pt[i]:
                    np.append(t)
                
                t = (p[0], p[1] + 1)
                
                if p[1] + 1 < len(mp[p[0]]) and mp[p[0]][p[1] + 1] != "#" and t not in pt[i]:
                    np.append(t)
                
                if len(np) == 0 and p != fp:
                    pt[i].append((-1, -1))
                elif len(np) == 1:
                    pt[i].append(cp.deepcopy(np[0]))
                else:
                    l, s = len(pt[i]) - 1, pt[i][0]
                    
                    if p not in nl:
                        nl.append(p)
                        
                        nd.append({})
                    
                    if s in nd[nl.index(p)]:
                        assert(nd[nl.index(p)][s] == l)
                    
                    nd[nl.index(p)][s] = l
                    
                    if p in nd[nl.index(s)]:
                        assert(nd[nl.index(s)][p] == l)
                    
                    nd[nl.index(s)][p] = l
                    
                    pt[i].append((-1, -1))
                    
                    for e in np:
                        if e not in vs:
                            tp = [p, cp.deepcopy(e)]
                            
                            pt.append(tp)
            else:
                assert(False)
            
            # print_paths_nodes(mp, pt, nl, vs, nd)
        
        if pt[i][-1] == (-1, -1):
            pt.pop(i)
        else:
            i += 1
    
    return nl, nd

def print_paths_nodes(mp, pt, nl, vs, nd):
    nm = cp.deepcopy(mp)
    
    for e in vs:
        nm[e[0]][e[1]] = "V"
    
    for e in nl:
        nm[e[0]][e[1]] = "N"
    
    for k, r in enumerate(nm):
        nm[k] = "".join(r) + "\t" + "".join(mp[k])
    
    for r in nm:
        print(r)
    
    print()
    
    for j, e in enumerate(nl):
        print(e, nd[j])
    
    print()
    
    for j, e in enumerate(pt):
        print(j, e)
    
    print("\n")

def get_longest_path(nl, nd):
    i, pt, ls = 0, [[nl[0]]], []

    while i < len(pt):    
        while pt[i][-1] != (-1, -1) and pt[i][-1] != nl[-1]:
            index = nl.index(pt[i][-1])
            
            for j in range(len(nd[index]) - 1, -1, -1):
                if j == 0:
                    if list(nd[index].keys())[j] not in pt[i]:
                        pt[i].append(list(nd[index].keys())[j])
                    else:
                        pt[i].append((-1, -1))
                else:
                    tp = cp.deepcopy(pt[i])
                    
                    if list(nd[index].keys())[j] not in pt[i]:
                        tp.append(cp.deepcopy(list(nd[index].keys())[j]))
                    else:
                        tp.append((-1, -1))
                    
                    pt.append(tp)
        
        if pt[i][-1] == (-1, -1):
            pt.pop(i)
        else:
            i += 1
        
        print(len(pt))

    for p in pt:
        total = 0
        
        for i in range(len(p) - 1):
            total += nd[nl.index(p[i + 1])][p[i]]
        
        ls.append(total)

    return max(ls)

def get_possible_paths(nl, nd):
    i, maxl, paths = 0, 0, []

    paths.append([nl[0]])

    while i < len(paths):
        while paths[i][-1] != nl[-1]:
            cont, index = False, nl.index(paths[i][-1])
            
            for e in nd[index]:
                if not cont:
                    if e not in paths[i]:
                        paths[i].append(e)
                        
                        cont, maxl = True, max(maxl, len(paths[i]))
                elif e not in paths[i][:-1]:
                    temp = cp.deepcopy(paths[i][:-1])
                    
                    temp.append(e)
                    
                    paths.insert(i + 1, cp.deepcopy(temp))
                    
                    maxl = max(maxl, len(paths[i + 1]))
            
            if not cont:
                paths.pop(i)
                
                i -= 1
        
        print(len(paths) - i)
        
        i += 1
    
    return paths

def get_longest_length(nl, nd, paths):
    maxl = 0

    for i, p in enumerate(paths):
        assert(p[0] == nl[0] and p[-1] == nl[-1])
        
        total = 0
        
        for j, e in enumerate(p):
            if j > 0:
                total += nd[nl.index(e)][p[j - 1]]
        
        maxl = max(maxl, total)

    return maxl