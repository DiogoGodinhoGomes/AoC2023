import numpy as np

def get_scmp(filename):
    sc, mp, osc, ts, ix, ax, iy, ay, iz, az = [], [], [], [], 0, 0, 0, 0, 0, 0
    
    with open(filename) as file:
        for l, line in enumerate(file):
            nl = list(line.strip().split("~"))
            
            for e in range(len(nl)):
                nl[e] = list(map(int, nl[e].split(",")))
            
            ix = min(ix, nl[0][0], nl[1][0])
            ax = max(ax, nl[0][0], nl[1][0])
            
            iy = min(iy, nl[0][1], nl[1][1])
            ay = max(ay, nl[0][1], nl[1][1])
            
            iz = min(iz, nl[0][2], nl[1][2])
            az = max(az, nl[0][2], nl[1][2])
            
            ts.append([l, min(nl[0][2], nl[1][2])])
            
            osc.append([[min(nl[0][0], nl[1][0]),
                         min(nl[0][1], nl[1][1]),
                         min(nl[0][2], nl[1][2])],
                        [abs(nl[0][0] - nl[1][0]),
                         abs(nl[0][1] - nl[1][1]),
                         abs(nl[0][2] - nl[1][2])]])
            
            assert(osc[l][1][0] * osc[l][1][1] == 0 and
                   (osc[l][1][0] * osc[l][1][2] == 0 or
                    osc[l][1][1] * osc[l][1][2] == 0))
    
    for i in range(ay - iy + 1):
        nr = []
        
        for j in range(ax - ix + 1):
            nr.append([0, -1])
        
        mp.append(nr)
    
    ts = np.array(ts)[np.array(ts)[:, 1].argsort()].tolist()
    
    for e in ts:
        sc.append([osc[e[0]][0], osc[e[0]][1], 0, set(), set()])
    
    assert(ix == 0 and iy == 0 and iz == 0)
    
    return sc, mp

def get_fall(sc, mp):
    fall, rmv = 0, []
    
    for i in range(len(sc)):
        h, st = 0, set()
        
        if sc[i][1][0] > 0:
            for p in range(sc[i][1][0] + 1):
                h = max(h, mp[sc[i][0][0] + p][sc[i][0][1]][0])
            
            for p in range(sc[i][1][0] + 1):
                if mp[sc[i][0][0] + p][sc[i][0][1]][1] >= 0 and mp[sc[i][0][0] + p][sc[i][0][1]][0] == h:
                    st.add(mp[sc[i][0][0] + p][sc[i][0][1]][1])
        elif sc[i][1][1] > 0:
            for p in range(sc[i][1][1] + 1):
                h = max(h, mp[sc[i][0][0]][sc[i][0][1] + p][0])
            
            for p in range(sc[i][1][1] + 1):
                if mp[sc[i][0][0]][sc[i][0][1] + p][1] >= 0 and mp[sc[i][0][0]][sc[i][0][1] + p][0] == h:
                    st.add(mp[sc[i][0][0]][sc[i][0][1] + p][1])
        else:
            h = max(h, mp[sc[i][0][0]][sc[i][0][1]][0])
            
            if mp[sc[i][0][0]][sc[i][0][1]][1] >= 0 and mp[sc[i][0][0]][sc[i][0][1]][0] == h:
                st.add(mp[sc[i][0][0]][sc[i][0][1]][1])
        
        for v in st:
            sc[i][3].add(v)
            
            sc[v][4].add(i)
        
        h += sc[i][1][2] + 1
        
        if sc[i][1][0] > 0:
            for p in range(sc[i][1][0] + 1):
                mp[sc[i][0][0] + p][sc[i][0][1]] = [h, i]
            
            sc[i][2] = h
        elif sc[i][1][1] > 0:
            for p in range(sc[i][1][1] + 1):
                mp[sc[i][0][0]][sc[i][0][1] + p] = [h, i]
            
            sc[i][2] = h
        else:
            mp[sc[i][0][0]][sc[i][0][1]] = [h, i]
            
            sc[i][2] = h - sc[i][1][2]
        
        if sc[i][2] != sc[i][0][2]:
            fall += 1
        
    for i in range(len(sc)):
        if len(sc[i][3]) == 1 and list(sc[i][3])[0] not in rmv:
            rmv.append(list(sc[i][3])[0])
    
    return fall, rmv

def get_total(sc, mp, rmv):
    total = 0
    
    for e in sc:
        if e[0][2] > e[2]:
            e[0][2] = e[2]

    for i in range(len(sc)):
        if i in rmv:
            for a in range(len(mp)):
                for b in range(len(mp[a])):
                    mp[a][b] = [0, -1]
            
            n_sc = []
            
            for e in sc[:i] + sc[i + 1:]:
                n_sc.append([e[0], e[1], e[2], set(), set()])
            
            i_fall, i_rmv = get_fall(n_sc, mp)
            
            total += i_fall

    return total