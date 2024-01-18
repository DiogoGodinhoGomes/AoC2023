from collections import deque

def get_data(filename):
    br, fl, cc, ut, qu = {}, {}, {}, {}, deque()
    
    with open(filename) as file:
        for line in file:
            nl = line.replace(" -> ", ",").replace(" ", "").strip().split(",")
            
            if nl[0][0] == "b":
                br["#br"] = [nl[1:], -1]
            elif nl[0][0] == "%":
                fl[nl[0]] = [nl[1:], -1]
            elif nl[0][0] == "&":
                cc[nl[0]] = [nl[1:], {}]
            else:
                ut["@" + nl[0]] = [[], -1]
    
    for b in br:
        for e in range(len(br[b][0])):
            if "%" + br[b][0][e] in fl:
                br[b][0][e] = "%" + br[b][0][e]
            elif "&" + br[b][0][e] in cc:
                br[b][0][e] = "&" + br[b][0][e]
            elif "#" + br[b][0][e] in br:
                br[b][0][e] = "#" + br[b][0][e]
            else:
                br[b][0][e] = "@" + br[b][0][e]
                
                ut[br[b][0][e]] = [[], -1]
    
    for f in fl:
        for e in range(len(fl[f][0])):
            if "%" + fl[f][0][e] in fl:
                fl[f][0][e] = "%" + fl[f][0][e]
            elif "&" + fl[f][0][e] in cc:
                fl[f][0][e] = "&" + fl[f][0][e]
            elif "#" + fl[f][0][e] in br:
                fl[f][0][e] = "#" + fl[f][0][e]
            else:
                fl[f][0][e] = "@" + fl[f][0][e]
                
                ut[fl[b][0][e]] = [[], -1]
    
    for c in cc:
        for e in range(len(cc[c][0])):
            if "%" + cc[c][0][e] in fl:
                cc[c][0][e] = "%" + cc[c][0][e]
            elif "&" + cc[c][0][e] in cc:
                cc[c][0][e] = "&" + cc[c][0][e]
            elif "#" + cc[c][0][e] in br:
                cc[c][0][e] = "#" + cc[c][0][e]
            else:
                cc[c][0][e] = "@" + cc[c][0][e]
                
                ut[cc[c][0][e]] = [[], -1]
    
    for i, f in enumerate(fl.values()):
        for e in f[0]:
            if e in cc.keys():
                cc[e][1][list(fl.keys())[i]] = -1
    
    for j, c in enumerate(cc.values()):
        for e in c[0]:
            if e in cc.keys():
                cc[e][1][list(cc.keys())[j]] = -1
    
    for k, u in enumerate(ut.values()):
        for e in u[0]:
            if e in cc.keys():
                cc[e][1][list(ut.keys())[k]] = -1
    
    return br, fl, cc, ut, qu

def get_state(dtnr):
    l, s = len(dtnr) - 1, 0
    
    for i, elem in enumerate(dtnr):
        s += int((dtnr[elem] + 1) / 2) * pow(2, l - i)
    
    return s

def press_button(br, fl, cc, ut, qu):
    total, st, tt, tl, th, ps, final = 1, 0, 0, 0, 0, {}, {}
    
    while len(final.keys()) < 4:
        qu.append(("!bt", "#br", -1))
        
        while len(qu) > 0:
            sourc, desti, pulse = qu[0][0], qu[0][1], qu[0][2]
            
            if desti[0] == "#":
                assert(desti in br)
                
                for e in br[desti][0]:
                    qu.append((desti, e, pulse))
                
                br[desti][1] = pulse
            elif desti[0] == "%":
                assert(desti in fl)
                
                if pulse == -1:
                    fl[desti][1] *= -1
                    
                    for e in fl[desti][0]:
                        qu.append((desti, e, fl[desti][1]))
            elif desti[0] == "&":
                assert(desti in cc)
                
                cc[desti][1][sourc] = pulse
                
                if sum(cc[desti][1].values()) == len(cc[desti][1].keys()):
                    output = -1
                else:
                    output = 1
                
                if output == 1 and (desti == "&hn" or desti == "&mp" or desti == "&xf" or desti == "&fz"):
                    final[desti] = st + 1
                
                for e in cc[desti][0]:
                    qu.append((desti, e, output))
            elif desti[0] == "@":
                assert(desti in ut)
                
                ut[desti][1] = pulse
            else:
                assert(False)
            
            if pulse == -1:
                tl += 1
            elif pulse == 1:
                th += 1
            
            tt += 1
            
            qu.popleft()
        
        st += 1

    for s in final:
        total *= final[s]
    
    return total, ps, st, tt, tl, th

def write_periods(filename, ps):
    with open(filename, "w") as file:
        for p in ps:
            for v in ps[p]:
                file.write(str(v) + "\t")
            
            file.write("\n")