# import copy as cp
from collections import deque

def print_data(tg, tt, tl, th, br, fl, cc, ut, qu):
    print("----------" + tg + "----------\n")
    
    assert(tt == tl + th)
    
    print("Total:", tt, "\nLow:", tl, "\nHigh:", th, "\n")
    
    print("Broadcasts:")
    
    for b in br:
        print("\t> ", b, br[b])
    
    print("\nFlip-Flops:")
    
    for f in fl:
        print("\t> ", f, fl[f])
    
    print("\nConjunctions:")
    
    for c in cc:
        print("\t> ", c, cc[c])
    
    print("\nUntypeds:")
    
    for u in ut:
        print("\t> ", u, ut[u])
    
    print("\nQueue:")
    
    for q in qu:
        print("\t> ", q)
    
    print("\n----------" + tg + "----------\n")

def get_data(filename):
    br, fl, cc, ut, qu = {}, {}, {}, {}, deque()
    
    with open(filename) as file:
        for line in file:
            n_line = line.replace(" -> ", ",").replace(" ", "").strip().split(",")
            
            if n_line[0][0] == "b":
                br["#br"] = [n_line[1:], -1]
            elif n_line[0][0] == "%":
                fl[n_line[0]] = [n_line[1:], -1]
            elif n_line[0][0] == "&":
                cc[n_line[0]] = [n_line[1:], {}]
            else:
                ut["@" + n_line[0]] = [[], -1]
    
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

def press_button(num, br, fl, cc, ut, qu):
    tt, tl, th = 0, 0, 0
    
    '''
    br_i = cp.deepcopy(br)
    fl_i = cp.deepcopy(fl)
    cc_i = cp.deepcopy(cc)
    ut_i = cp.deepcopy(ut)
    qu_i = cp.deepcopy(qu)

    print_data("INITIAL", tt, tl, th, br, fl, cc, ut, qu)
    '''
    
    for i in range(num):
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
                
                output = -1 if sum(cc[desti][1].values()) == len(cc[desti][1].keys()) else 1
                
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
    
    '''
    print_data("-FINAL-", tt, tl, th, br, fl, cc, ut, qu)

    print("BR == BR_I:\t", br == br_i)
    print("FL == FL_I:\t", fl == fl_i)
    print("CC == CC_I:\t", cc == cc_i)
    print("UT == UT_I:\t", ut == ut_i)
    print("QU == QU_I:\t", qu == qu_i)
    '''
    
    return tl * th