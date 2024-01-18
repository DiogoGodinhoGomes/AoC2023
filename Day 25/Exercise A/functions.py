import copy as cp
import time as tm

def get_dtnr(filename):
    dtnr = {}

    with open(filename) as file:
        for line in file:
            nl = line.strip().replace(":", "").replace(" ", ",").split(",")
            
            if nl[0] not in dtnr:
                dtnr[nl[0]] = []
            
            for i in range(1, len(nl)):
                if nl[i] not in dtnr[nl[0]]:
                    dtnr[nl[0]].append(nl[i])
                
                if nl[i] not in dtnr:
                    dtnr[nl[i]] = [nl[0]]
                else:
                    dtnr[nl[i]].append(nl[0])
    
    return dtnr

def get_link_traffic(st, dtnr):
    nd = {}

    for p in range(len(dtnr)):
        print(p + 1, tm.time() - st)
        
        f = list(dtnr.keys())[p]
        
        i, n, u, v, cnts = 1, 1000, set(), set(), {}
        
        v.add(f)
        
        for e in dtnr:
            cnts[e] = [n, []]
        
        cnts[f] = [0, []]
        
        while i < len(dtnr):
            m = n + 1
            
            for e in dtnr[f]:
                if e not in v:
                    u.add(e)
                    
                    if cnts[f][0] + 1 < cnts[e][0]:
                        nl = cp.deepcopy(cnts[f][1])
                        
                        nl.append(f)
                        
                        cnts[e] = [cnts[f][0] + 1, cp.deepcopy(nl)]
            
            for e in u:
                if cnts[e][0] < m:
                    m, f = cnts[e][0], cp.deepcopy(e)
            
            u.remove(f)
            
            v.add(f)
            
            i += 1
        
        for e in cnts:
            cnts[e][1].append(e)
        
        for e in cnts:
            for i in range(len(cnts[e][1]) - 1):
                t = tuple(sorted([cnts[e][1][i], cnts[e][1][i + 1]]))
                
                if t not in nd:
                    nd[t] = 1
                else:
                    nd[t] += 1
    
    return nd

def get_critical_links(nd):
    final, fmaxi = [], []

    while len(final) < 3:
        obj, maxi = 0, 0
        
        for i, e in enumerate(nd):
            if nd[e] > maxi and e not in final:
                maxi = nd[e]
                
                obj = e
        
        final.append(cp.deepcopy(obj))
        
        fmaxi.append(cp.deepcopy(maxi))

    return final, fmaxi

def get_group_sizes(dtnr):
    f, l = "", []

    for i in range(2):
        u, v = [], []
        
        if f == "":
            u.append(list(dtnr.keys())[0])
        else:
            u.append(f)
        
        while len(u) > 0:
            for e in dtnr[u[0]]:
                if e not in v:
                    u.append(e)
            
            if u[0] not in v:
                v.append(u[0])
            
            u.pop(0)
        
        for e in dtnr:
            if e not in v:
                f = e
                
                break
        
        l.append(len(v))

    return l

def get_total(dtnr, final = []):
    for e in final:
        dtnr[e[0]].remove(e[1])
        dtnr[e[1]].remove(e[0])

    total, l = 0, get_group_sizes(dtnr)

    if l[0] + l[1] == len(dtnr):
        total = l[0] * l[1]
    elif l[0] == len(dtnr) and l[1] == len(dtnr):
        total = 0
    else:
        assert(False)

    print()
    
    return total