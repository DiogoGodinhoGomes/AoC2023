full_code = []
actv_pstn = []

with open("code.txt") as code:
    for line in code:
        full_code.append(list(line.strip()))
        actv_pstn.append([''] * len(list(line.strip())))
    
for i in range(len(full_code)):
    for j in range(len(full_code[i])):
        if full_code[i][j] == '*':
            actv_pstn[i][j] = []

for i in range(len(full_code)):
    j = 0
    
    new_num = ""
    
    while j < len(full_code[i]):
        if full_code[i][j].isdigit():
            new_num += full_code[i][j]
        else:                
            if new_num != "":
                num_len = len(new_num)
                
                for row in [-1, 0, 1]:
                    for col in range(-(num_len + 1), 1):
                        if i + row >= 0 and j + col >= 0 and i + row < len(full_code) and j + col < len(full_code[i]):
                            if actv_pstn[i + row][j + col] != '':
                                actv_pstn[i + row][j + col].append(int(new_num))
            
            new_num = ""
        
        j += 1
    
    if new_num != "":
        num_len = len(new_num)
        
        for row in [-1, 0, 1]:
            for col in range(-(num_len + 1), 1):
                if i + row >= 0 and j + col >= 0 and i + row < len(full_code) and j + col < len(full_code[i]):
                    if actv_pstn[i + row][j + col] != '':
                        actv_pstn[i + row][j + col].append(int(new_num))
    
    new_num = ""

total = 0

for i in range(len(actv_pstn)):
    for j in range(len(actv_pstn[i])):
        if len(actv_pstn[i][j]) == 2:
            total += actv_pstn[i][j][0] * actv_pstn[i][j][1]

print(total)