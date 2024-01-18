import numpy as np

def get_maps(filename):
    maps = []
    
    with open(filename) as file:
        new_map = []
        
        for line in file:
            if len(line.strip()) > 0:
                new_map.append(list(line.strip().replace(".", "0").replace("#", "1")))
            else:
                maps.append(new_map)
                
                new_map = []
        
        if len(new_map) > 0:
            maps.append(new_map)
    
    return maps

def get_sym_axis(m):
    l = []

    for i in m:
        l.append(int(''.join(i), 2))

    sym = []

    for i in range(1, len(l)):
        is_sym = True
        
        j = 0
        
        while j < i:
            k = 2 * i - 1 - j
            
            if k < len(l):
                if l[j] != l[k]:
                    is_sym = False
            
            j += 1
        
        if is_sym:
            sym.append(i)

    return sym

def get_axes(m):
    axes = []
    
    rows = get_sym_axis(m)
    
    cols = get_sym_axis(np.array(m).transpose().tolist())
    
    for i in rows:
        axes.append(100 * i)
    
    for i in cols:
        axes.append(i)
    
    return axes

def get_axes_total(maps):
    axes = []

    total = 0

    for m in maps:
        axes.append(get_axes(m))
        
        total += sum(axes[-1])
    
    return axes, total

def get_new_axes(maps):
    new_axes = []

    for m in maps:
        temp_axes = set()
        
        for i in range(len(m)):
            for j in range(len(m[i])):
                m[i][j] = '0' if m[i][j] == '1' else '1'
                
                temp = get_axes(m)
                
                for k in temp:
                    temp_axes.add(k)
                
                m[i][j] = '0' if m[i][j] == '1' else '1'
        
        new_axes.append(temp_axes)
    
    return new_axes