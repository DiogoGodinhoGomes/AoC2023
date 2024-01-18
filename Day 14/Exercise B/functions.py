import copy as cp

def get_plat(filename):
    plat = []
    
    with open(filename) as file:
        for line in file:
            plat.append(list(line.strip()))
    
    return plat

def write_result(tag, result):
    with open(tag + "result" + ".txt", "w") as file:
        for line in result:
            file.write(str(line) + "\n")

def get_load(plat):
    total = 0
    
    for row in range(len(plat)):
        current = 0
        
        for elem in plat[row]:
            if elem == "O":
                current += 1
        
        total += (len(plat) - row) * current
    
    return total

def slide_north(plat):
    for col in range(len(plat[0])):
        last_empty_row = 0
        
        for row in range(len(plat)):
            if plat[row][col] == "O":
                plat[row][col] = "."
                
                plat[last_empty_row][col] = "O"
                
                last_empty_row += 1
            elif plat[row][col] == "#" and row + 1 < len(plat):
                last_empty_row = row + 1

def slide_west(plat):
    for row in range(len(plat)):
        last_empty_col = 0
        
        for col in range(len(plat[row])):
            if plat[row][col] == "O":
                plat[row][col] = "."
                
                plat[row][last_empty_col] = "O"
                
                last_empty_col += 1
            elif plat[row][col] == "#" and col + 1 < len(plat[row]):
                last_empty_col = col + 1

def slide_south(plat):
    for col in range(len(plat[0])):
        last_empty_row = len(plat) - 1
        
        for row in range(len(plat) - 1, -1, -1):
            if plat[row][col] == "O":
                plat[row][col] = "."
                
                plat[last_empty_row][col] = "O"
                
                last_empty_row -= 1
            elif plat[row][col] == "#" and row > 0:
                last_empty_row = row - 1

def slide_east(plat):
    for row in range(len(plat)):
        last_empty_col = len(plat[row]) - 1
        
        for col in range(len(plat[row]) - 1, -1, -1):
            if plat[row][col] == "O":
                plat[row][col] = "."
                
                plat[row][last_empty_col] = "O"
                
                last_empty_col -= 1
            elif plat[row][col] == "#" and col > 0:
                last_empty_col = col - 1

def spin_cycle(plat, n):
    lst, dtnr, i, l = [], {}, 0, 0
    
    while i < n:
        slide_north(plat)
        slide_west(plat)
        slide_south(plat)
        slide_east(plat)
        
        load = get_load(plat)
        lst.append(load)
        
        if load in dtnr.keys():
            dtnr[load] += 1
        else:
            dtnr[load] = 1
        
        if len(dtnr.keys()) > l:
            i, l = 0, len(dtnr.keys())
        else:
            i += 1
    
    return lst, dtnr

def find_period(lst, num):
    dlens, new_dtnr, stop = [], {}, False
    p, l, stable, i = 0, 0, 0, len(lst) - 1

    while i >= 0 and not stop:
        if lst[i] in new_dtnr.keys():
            new_dtnr[lst[i]] += 1
            
            stable += 1
        else:
            new_dtnr[lst[i]] = 1
            
            stable = 0
            
            l += 1
        
        dlens.append(len(new_dtnr.keys()))
        
        if stable == num:
            stop = True
            
            p = dlens.index(l) + 1
        
        i -= 1

    cycles = int((len(lst) - i) / p) if p > 0 else 1

    flag = True

    for i in range(cycles - 1):
        if i == 0:
            flag *= (lst[-p:] == lst[-2 * p:-p])
        else:
            flag *= (lst[-(i + 1) * p:-i * p] == lst[-(i + 2) * p:-(i + 1) * p])

    if not (flag and cycles > 1):
        p = 0
    
    return p

def get_index_sequence(lst, period):
    i = len(lst) - period - 1

    sequence = cp.deepcopy(lst[-period:])

    sequence.reverse()

    consistent = True

    j = 0

    while consistent and i >= 0:
        if lst[i] != sequence[j % len(sequence)]:
            consistent = False
        else:
            i -= 1
            j += 1
    
    if i > 0:
        i += 1

    return i, lst[i : i + period]