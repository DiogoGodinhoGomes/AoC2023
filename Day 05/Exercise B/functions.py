def get_seeds_maps(filename):
    seeds = []
    maps = []
    
    with open(filename) as code:
        i = 0
        
        bundle = []
        
        for line in code:
            if len(line) > 0:
                if ":" in line:
                    if i == 0:
                        seeds = list(map(int, line.replace(":", "").split()[1:]))
                    
                    if len(bundle) > 0:
                        maps.append(bundle)
                    
                    bundle = []
                    
                    i += 1
                elif i > 0 and len(line.split()) > 0:
                    bundle.append(list(map(int, line.split())))
        
        if len(bundle) > 0:
            maps.append(bundle)
    
    return seeds, maps

def sort_ranges(ranges):
    seed_ranges = []

    for i in range(int(len(ranges)/ 2)):
        seed_ranges.append([ranges[2 * i], ranges[2 * i + 1]])

    for i in range(1, len(seed_ranges)):
        for j in range(1, len(seed_ranges) - i + 1):
            if seed_ranges[j - 1][0] > seed_ranges[j][0]:
                temp = seed_ranges[j - 1]
                
                seed_ranges[j - 1] = seed_ranges[j]
                
                seed_ranges[j] = temp
    
    return seed_ranges

def sort_maps(maps):
    for i in range(len(maps)):
        for j in range(1, len(maps[i])):
            for k in range(1, len(maps[i]) - j + 1):
                if maps[i][k - 1][1] > maps[i][k][1]:
                    temp = maps[i][k - 1]
                    
                    maps[i][k - 1] = maps[i][k]
                    
                    maps[i][k] = temp

def translate(seed, current_map):
    i = 0
    result = seed

    while i < len(current_map) and seed >= current_map[i][1]:
        i += 1

    if i > 0:
        result += current_map[i - 1][0] - current_map[i - 1][1]
    
    if seed >= current_map[i - 1][1] + current_map[i - 1][2]:
        result = seed
    
    return i, result

def write_maps(maps):
    with open("maps.txt", mode = 'w') as output:
        for i in range(len(maps)):
            for j in range(len(maps[i])):
                output.write(str(maps[i][j]))
                output.write('\n')
            output.write('\n')

def get_better_maps(maps):
    better_maps = []

    for elem in maps:
        i = 0
        
        new_elem = []
        
        while i < len(elem) and i <= elem[i][1]:
            if i == 0 and elem[i][1] != 0:
                new_elem.append([0, 0])
            
            if i < len(elem) - 1:
                new_elem.append([elem[i][1], elem[i][0] - elem[i][1]])
                
                rest = elem[i + 1][1] - sum(elem[i][1:])
                
                assert(rest >= 0)
                
                if rest > 0:
                    new_elem.append([sum(elem[i][1:]), 0])
            else:
                new_elem.append([elem[i][1], elem[i][0] - elem[i][1]])
                new_elem.append([sum(elem[i][1:]), 0])
            
            i += 1
        
        better_maps.append(new_elem)
        
    assert(len(maps) == len(better_maps))
    
    return better_maps