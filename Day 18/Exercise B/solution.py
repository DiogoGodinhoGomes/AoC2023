import copy as cp
import functions as fc

instr = fc.read_instr("code.txt")

fc.convert_instr(True, instr)

crns, h, w, vp, hp = fc.get_corners(instr)

ba, aa, pba, paa, total, lims = 0, 0, 0, 0, 0, []

for k in range(len(crns)):
    pba, paa = cp.deepcopy(ba), cp.deepcopy(aa)
    
    ba, aa, a, l, t, d, r = 0, 0, [], [], [], [], []
    
    for e in crns[k][1]:
        l.append(1 if e in lims else 0)
    
    assert(len(l) % 2 == 0)
    
    for n in range(int(len(l) / 2)):
        t.append(l[2 * n] + l[2 * n + 1] - 1)
    
    for i, e in enumerate(t):
        if e == -1:
            j = 0
            
            while j < len(lims) and crns[k][1][2 * i] >= lims[j]:
                j += 1
            
            if j % 2 == 0:
                lims.insert(j, cp.deepcopy(crns[k][1][2 * i]))
                lims.insert(j + 1, cp.deepcopy(crns[k][1][2 * i + 1]))
            else:
                a.append(crns[k][1][2 * i])
                a.append(crns[k][1][2 * i + 1])
        elif e == 0:
            if crns[k][1][2 * i] in lims:
                index = lims.index(crns[k][1][2 * i])
                
                if crns[k][1][2 * i + 1] < crns[k][1][2 * i] and index % 2 == 0:
                    lims[index] = cp.deepcopy(crns[k][1][2 * i + 1])
                elif crns[k][1][2 * i + 1] > crns[k][1][2 * i] and index % 2 == 1:
                    lims[index] = cp.deepcopy(crns[k][1][2 * i + 1])
                else:
                    r.append([crns[k][1][2 * i], crns[k][1][2 * i + 1]])
            else:
                index = lims.index(crns[k][1][2 * i + 1])
                
                if crns[k][1][2 * i + 1] > crns[k][1][2 * i] and index % 2 == 0:
                    lims[index] = cp.deepcopy(crns[k][1][2 * i])
                elif crns[k][1][2 * i + 1] < crns[k][1][2 * i] and index % 2 == 1:
                    lims[index] = cp.deepcopy(crns[k][1][2 * i])
                else:
                    r.append([crns[k][1][2 * i + 1], crns[k][1][2 * i]])
        elif e == 1:
            if lims.index(crns[k][1][2 * i]) % 2 == 1:
                lims.remove(crns[k][1][2 * i])
                lims.remove(crns[k][1][2 * i + 1])
            else:
                d.append(crns[k][1][2 * i])
                d.append(crns[k][1][2 * i + 1])
        else:
            assert(False)
    
    for i in range(int(len(lims) / 2)):
        ba += lims[2 * i + 1] - lims[2 * i] + 1
    
    for e in d:
        lims.remove(e)
    
    for e in r:
        index = lims.index(e[0])
        
        lims[index] = e[1]
    
    for e in a:
        j = 0
        
        while j < len(lims) and e >= lims[j]:
            j += 1
        
        lims.insert(j, cp.deepcopy(e))
    
    for i in range(int(len(lims) / 2)):
        aa += lims[2 * i + 1] - lims[2 * i] + 1
    
    # print(crns[k][0], "\t\t", ba, " \t", aa)
    
    if k < len(crns) - 1:
        # print("pba =", pba)
        # print("paa =", paa)
        # print("ba =", ba)
        # print("aa =", aa)
        # print("diff =", crns[k + 1][0] - crns[k][0], "\n")
        
        if aa == ba:
            total += (crns[k + 1][0] - crns[k][0]) * ba
            
            # print("\t\t\t\t\t\t\t", (crns[k + 1][0] - crns[k][0]), "x", ba, "\n")
        else:
            diff = crns[k + 1][0] - crns[k][0]
            
            if diff > 1:
                total += ba + (diff - 1) * aa
                
                # print("\t\t\t\t\t\t\t", 1, "x", ba, "\n")
                # print("\t\t\t\t\t\t\t", diff - 1, "x", aa, "\n")
            else:
                total += diff * ba
                
                # print("\t\t\t\t\t\t\t", diff, "x", ba, "\n")

total += ba

print("\n" + str(total))