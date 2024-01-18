import copy as cp

def get_springs(filename):
    springs = []
    
    with open(filename) as file:
        for line in file:
            sequence, values = line.split()
            
            springs.append([sequence, list(map(int,values.split(",")))])
    
    return springs

def get_final_springs(springs):
    final_springs = []

    for i, elem in enumerate(springs):
        print((i + 1) * 100 / len(springs), "%")
        
        possibilities = [[]]
        
        for char in elem[0]:
            if char == '.' or char == '#':
                for j in range(len(possibilities)):
                    possibilities[j].append(char)
            elif char == '?':
                possibilities += cp.deepcopy(possibilities)
                
                for j in range(len(possibilities)):
                    if j < int(len(possibilities) / 2):
                        possibilities[j].append('.')
                    else:
                        possibilities[j].append('#')
        
        for p in possibilities:
            final_springs.append([''.join(p), elem[1]])

    return final_springs

def get_total(springs):
    total = 0

    for i, elem in enumerate(springs):
        print((i + 1) * 100 / len(springs), "%")
        
        is_hash = True
        
        results = []
        
        length = 0
        
        for i in elem[0]:
            if i == '#':
                if is_hash == False:
                    is_hash = True
                
                length += 1
            elif i == '.':
                if is_hash == True:
                    if length > 0:
                        results.append(length)
                    
                    is_hash = False
                    
                    length = 0
        
        if elem[0][-1] == '#':
            results.append(length)
        
        if results == elem[1]:
            total += 1

    return total