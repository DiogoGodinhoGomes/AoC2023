import time as tm
from collections import deque

def get_springs(filename, num):
    springs = []
    
    with open(filename) as file:
        for line in file:
            if num > 0:
                sequence, values = line.split()
                
                for i in range(num - 1):
                    sequence += "?" + line.split()[0]
                    values += "," + line.split()[1]
            elif num == 0:
                sequence = "?" + line.split()[0]
                values = line.split()[1]
            
            springs.append([sequence, list(map(int,values.split(",")))])
    
    return springs

def get_char_counts(string, codes):
    t, h, d, q = 0, 0, 0, 0
    
    for char in string:
        t += 1
        
        if char == "#":
            h += 1
        elif char == ".":
            d += 1
        elif char == "?":
            q += 1
    
    b = sum(codes)
    
    assert(t == h + d + q)
    
    return t, h, d, q, b

def is_cons(sequence, comparison):
    results, is_hash, final, length, l = [], True, True, 0, 0
    
    if len(sequence) > 0 and len(comparison) > 0:
        for i in sequence:
            if i == "#":
                if is_hash == False:
                    is_hash = True
                
                length += 1
            elif i == ".":
                if is_hash == True:
                    if length > 0:
                        results.append(length)
                    
                    is_hash = False
                    
                    length = 0
        
        if sequence[-1] == "#":
            results.append(length)
        
        if len(results) > 0:
            if sequence[-1] == ".":
                final = results[0] == comparison[0]
                
                l += 1
            elif sequence[-1] == "#":
                final = results[0] <= comparison[0]
    
    return final, l

def get_final_springs(springs):
    t, h, d, q, b = get_char_counts(springs[0], springs[1])
    
    total, old_pos, new_pos = 0, [[0, deque([]), 0, 0]], []
    
    old_cts, new_cts = [1], []
    
    for c, char in enumerate(springs[0]):
        if char == "?":
            cases = [".", "#"]
        else:
            cases = [char]
        
        for case in cases:
            for j in range(len(old_pos) - 1, -1, -1):
                now = deque([])
                
                for k in old_pos[j][1]:
                    now.append(k)
                
                i, temp_cts = 0, 0 + old_cts[j]
                
                temp_pos = [0 + old_pos[j][0], now, 0 + old_pos[j][2], 0 + old_pos[j][3]]
                
                if case == "#":
                    temp_pos[1].append(case)
                elif len(temp_pos[1]) > 0 and temp_pos[1][-1] == "#":
                    temp_pos[1].append(case)
                
                temp_pos[2] += 1
                
                if case == "#":
                    temp_pos[3] += 1
                
                flag, l = is_cons(temp_pos[1], springs[1][temp_pos[0]:])
                
                total = sum(springs[1][temp_pos[0] : temp_pos[0] + l])
                
                temp_pos[0] += l
                
                while total > 0 and i <= total and len(temp_pos[1]) > 0:
                    if temp_pos[1][0] == "#":
                        i += 1
                    
                    if i <= total:
                        temp_pos[1].popleft()
                
                t_n, h_n, d_n, q_n, b_n = get_char_counts(springs[0][temp_pos[2]:], springs[1][temp_pos[0]:])
                
                if flag and (temp_pos[3] + h_n > b or temp_pos[3] + h_n + q_n < b):
                    flag = False
                
                if flag:
                    if temp_pos not in new_pos:
                        new_pos.append(temp_pos)
                        
                        new_cts.append(temp_cts)
                    else:
                        new_cts[new_pos.index(temp_pos)] += temp_cts
        
        old_pos, old_cts, new_pos, new_cts = new_pos, new_cts, [], []
    
    for j in range(len(old_pos) - 1, -1, -1):
        now = deque([])
        
        for k in old_pos[j][1]:
            now.append(k)
        
        i, temp_cts = 0, 0 + old_cts[j]
        
        temp_pos = [0 + old_pos[j][0], now, 0 + old_pos[j][2], 0 + old_pos[j][3]]
        
        temp_pos[1].append(".")
        
        flag, l = is_cons(temp_pos[1], springs[1][temp_pos[0]:])
        
        assert(flag)
        
        total = sum(springs[1][temp_pos[0] : temp_pos[0] + l])
        
        temp_pos[0] += l
        
        while total > 0 and i <= total and len(temp_pos[1]) > 0:
            if temp_pos[1][0] == "#":
                i += 1
            
            if i <= total:
                temp_pos[1].popleft()
        
        t_n, h_n, d_n, q_n, b_n = get_char_counts(springs[0][temp_pos[2]:], springs[1][temp_pos[0]:])
        
        if len(temp_pos[1]) > 0:
            assert(temp_pos[1][-1] == ".")
            
            temp_pos[1].pop()
        
        assert(temp_pos[0] == len(springs[1]) and len(temp_pos[1]) == 0 and temp_pos[2] == t and temp_pos[3] == b)
        
        if temp_pos not in new_pos:
            new_pos.append(temp_pos)
            
            new_cts.append(temp_cts)
        else:
            new_cts[new_pos.index(temp_pos)] += temp_cts
    
    return sum(new_cts)

def write_finals(tag, number, springs, st):
    total = 0
    
    with open("result.txt", "w") as result:
        for i in range(len(springs)):
            num = get_final_springs(springs[i])
            
            total += num
            
            result.write(str(i + 1) + "\t" + str(num) + "\n")
        
        result.write("\nFinal: " + str(total) + "\n")
        
        result.write("\nRun Time: " + str(round(tm.time() - st, 2)) + " s")
    
    return total