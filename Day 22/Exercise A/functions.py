# import time as tm

import numpy as np
import random as rd
import matplotlib.pyplot as plt

'''
new = []

for e in sc:
    new.append([[e[0][0], e[0][1], e[2]], e[1]])

for i in range(len(sc)):
    fc.plot_blocks([ax + 1, ay + 1, min(az, 20) + 1], new[:(i + 1)])
    
    print("\n", sc[len(new[:(i + 1)]) - 1], "\n")
    
    tm.sleep(2)
'''

colors = []

def plot_blocks(axes, sc):
    fig = plt.figure()
    
    ax = fig.add_subplot(111, projection = "3d")
    
    for v, e in enumerate(sc):
        data = np.zeros(axes, dtype = bool)
        
        data[e[0][0], e[0][1], e[0][2]] = True
        
        for i in range(e[1][0]):
            data[e[0][0] + (i + 1), e[0][1], e[0][2]] = True
        
        for j in range(e[1][1]):
            data[e[0][0], e[0][1] + (j + 1), e[0][2]] = True
        
        for k in range(e[1][2]):
            data[e[0][0], e[0][1], e[0][2] + (k + 1)] = True
        
        if v >= len(colors):
            colors.append([rd.random(), rd.random(), rd.random(), 0.75])
        
        ax.voxels(data, facecolors = colors[v], edgecolors = "black")
    
    ax.set_aspect("equal")
    
    plt.show()

def visualize(sc, mp, ix, ax, iy, ay, iz, az):
    for e in sc:
        print(e)
    
    print("x: [" + str(ix) + ", " + str(ax) + "]", end = "\t|\t")
    print("y: [" + str(iy) + ", " + str(ay) + "]", end = "\t|\t")
    print("z: [" + str(iz) + ", " + str(az) + "]")
    
    for r in mp:
        for c in r:
            print(c, end = "\t")
        
        print()

def get_block_dims(sc):
    td = {}

    for e in sc:
        t = 0
        
        for i in e[1]:
            if i > 0:
                t += 1
        
        if t not in td:
            td[t] = 1
        else:
            td[t] += 1

    for e in td:
        print(e, td[e])

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
    
    return sc, mp, ax, ay, az

def visualize_slice(i, sc, num):
    j = -num
    
    print("------------------------------\n\nBlock (" + str(i) + "):")
    
    while j < num + 1 and i + j < len(sc):
        if sc[i + j][1][0] + sc[i + j][1][1] + sc[i + j][1][2] == 0:
            d = "C"
        elif sc[i + j][1][0] > 0:
            d = "V"
        elif sc[i + j][1][1] > 0:
            d = "H"
        elif sc[i + j][1][2] > 0:
            d = "T"
            
        if i + j >= 0:
            print("X" if j == 0 else " ", sc[i + j], d)
        
        j += 1
    
    print()

def visualize_map(mp):
    print("Height Map:")
    
    for r in mp:
        for c in r:
            print(c[0], end = "\t")
        
        print()
    
    print("\nID Map:")
    
    for r in mp:
        for c in r:
            print(c[1], end = "\t")
        
        print()
    
    print()

def get_fall(sc, mp):
    rmv = []
    
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
        
        '''
        visualize_slice(i, sc, 1)
        
        visualize_map(mp)
        '''
    
    for i in range(len(sc)):
        if len(sc[i][3]) == 1 and list(sc[i][3])[0] not in rmv:
            rmv.append(list(sc[i][3])[0])
    
    return rmv

def get_safe_blocks(sc):
    sf = []
    
    for i, e in enumerate(sc):
        false = 0
        
        for b in e[4]:
                if len(sc[b][3]) < 2:
                    false += 1
        
        if false == 0 and i not in sf:
            sf.append(i)
    
    return sf

def write_results(filename, sc):
    with open(filename, "w") as file:
        for b in sc:
            for e in b:
                if not isinstance(e, int):
                    for i, c in enumerate(e):
                        file.write(str(c) + (";" if i < len(e) - 1 else ""))
                else:
                    file.write(str(e))
                
                file.write("|")
            
            file.write("\n")