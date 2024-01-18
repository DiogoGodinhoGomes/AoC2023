import functions as fc

ranges, maps = fc.get_seeds_maps("code.txt")

seed_ranges = fc.sort_ranges(ranges)

fc.sort_maps(maps)

better_maps = fc.get_better_maps(maps)

for maps in better_maps:    
    s = 0
    
    while s < len(seed_ranges):
        if seed_ranges[s][0] >= maps[-1][0]:
            interval = len(maps) - 1
        else:
            interval = 0
            
            while seed_ranges[s][0] >= maps[interval + 1][0]:
                interval += 1
        
        if interval == len(maps) - 1:
            seed_ranges[s] = [seed_ranges[s][0] + maps[interval][1], seed_ranges[s][1]]
        elif sum(seed_ranges[s]) <= maps[interval + 1][0]:
            seed_ranges[s] = [seed_ranges[s][0] + maps[interval][1], seed_ranges[s][1]]
        else:
            rest = sum(seed_ranges[s]) - maps[interval + 1][0]
            
            seed_ranges[s] = [seed_ranges[s][0] + maps[interval][1], seed_ranges[s][1] - rest]
            
            seed_ranges.append([maps[interval + 1][0], rest])
        
        s += 1

minimum = int(1e20)

for i in seed_ranges:
    minimum = min(minimum, i[0])

print(minimum)