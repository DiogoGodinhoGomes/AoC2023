import copy as cp

def get_data(filename):
    data = []
    
    with open(filename) as file:
        for line in file:
            new_line = []
            
            for c in line.strip():
                new_line.append(int(c))
            
            data.append(new_line)
    
    return data

def get_dijkstra_with_restrictions(data, min_s, max_s):
    queue, visited, found = [(0, 0, 0, "E"), (0, 0, 0, "S")], set(), False

    while len(queue) > 0 and not found:
        hl, y, x, dr = queue[0]
        
        queue.pop(0)
        
        print((len(data) - y) + (len(data[y]) - x))
        
        if (y, x, dr[-1]) not in visited:
            visited.add((y, x, dr[-1]))
            
            if dr[-1] == "S" or dr[-1] == "N":
                nhl = cp.deepcopy(hl)
                
                for i in range(1, max_s + 1):
                    if x + i < len(data[y]):
                        nhl += data[y][x + i]
                        
                        if i >= min_s:
                            j = 0
                            
                            while j < len(queue) and queue[j][0] < nhl:
                                j += 1
                            
                            queue.insert(j, (nhl, y, x + i, dr + "E" * i))
                
                nhl = cp.deepcopy(hl)
                
                for i in range(1, max_s + 1):
                    if x - i >= 0:
                        nhl += data[y][x - i]
                        
                        if i >= min_s:
                            j = 0
                            
                            while j < len(queue) and queue[j][0] < nhl:
                                j += 1
                            
                            queue.insert(j, (nhl, y, x - i, dr + "W" * i))
                    
            elif dr[-1] == "E" or dr[-1] == "W":
                nhl = cp.deepcopy(hl)
                
                for i in range(1, max_s + 1):
                    if y + i < len(data):
                        nhl += data[y + i][x]
                        
                        if i >= min_s:
                            j = 0
                            
                            while j < len(queue) and queue[j][0] < nhl:
                                j += 1
                            
                            queue.insert(j, (nhl, y + i, x, dr + "S" * i))
                
                nhl = cp.deepcopy(hl)
                
                for i in range(1, max_s + 1):
                    if y - i >= 0:
                        nhl += data[y - i][x]
                        
                        if i >= min_s:
                            j = 0
                            
                            while j < len(queue) and queue[j][0] < nhl:
                                j += 1
                            
                            queue.insert(j, (nhl, y - i, x, dr + "N" * i))
            else:
                assert(False)
        
        if y == len(data) - 1 and x == len(data[y]) - 1:
            found = True

    return hl, dr[1:]