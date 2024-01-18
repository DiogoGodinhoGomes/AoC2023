import copy as cp
import time as tm
import functions as fc

st, ovl, num = tm.time(), {}, 5000

i_mp, i_ops = fc.get_mapa("code.txt")

for n in range(8000):
    ovl[n + 1] = []

with open("periods.txt", "a") as file:
    for e in ovl:
        file.write(str(e) + "\t")
    
    file.write("\n")

for n in range(num, num + 1):
    ops = fc.get_steps(n, cp.deepcopy(i_mp), cp.deepcopy(i_ops))
    
    tsm, cps, iy, ix, ay, ax = fc.get_diag_square(ops)
    
    for e in ovl:
        if e not in tsm:
            ovl[e].append(0)
        else:
            ovl[e].append(tsm[e])
    
    fc.print_diag_square("results.txt", n, cps, iy, ix, ay, ax)
    
    with open("periods.txt", "a") as file:
        for e in ovl:
            file.write(str(ovl[e][-1]) + "\t")
        
        file.write("\n")
    
    print(n, tm.time() - st)