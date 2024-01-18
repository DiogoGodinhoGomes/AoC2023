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
    
    return sorted(seeds), maps

def sort_maps():
    for i in range(len(maps)):
        for j in range(1, len(maps[i])):
            for k in range(1, len(maps[i]) - j + 1):
                if maps[i][k - 1][1] > maps[i][k][1]:
                    temp = maps[i][k - 1]
                    
                    maps[i][k - 1] = maps[i][k]
                    
                    maps[i][k] = temp

def translate(seed, num):
    i = 0

    while i < len(maps[num]) and seed >= maps[num][i][1]:
        i += 1

    result = seed

    if i > 0:
        result += maps[num][i - 1][0] - maps[num][i - 1][1]
    
    if seed >= maps[num][i - 1][1] + maps[num][i - 1][2]:
        result = seed
    
    return result

def end_to_end(seed):
    for i in range(len(maps)):    
        seed = translate(seed, i)
    
    return seed

seeds, maps = get_seeds_maps("code.txt")

sort_maps()

finals = []

for seed in seeds:
    finals.append(end_to_end(seed))

print(min(sorted(finals)))