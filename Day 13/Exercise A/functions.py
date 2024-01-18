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

    assert(len(sym) <= 1)

    return sym[0] if len(sym) == 1 else 0