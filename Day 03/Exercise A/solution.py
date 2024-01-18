with open("code.txt") as code:
    full_code = []
    actv_pstn = []
    
    for line in code:
        full_code.append(list(line.strip()))
        actv_pstn.append([0] * len(list(line.strip())))
    
    for i in range(len(full_code)):
        for j in range(len(full_code[i])):
            if full_code[i][j] != '.' and not full_code[i][j].isdigit():
                for row in [-1, 0, 1]:
                    for col in [-1, 0, 1]:
                        if i + row >= 0 and j + col >= 0 and i + row < len(full_code) and j + col < len(full_code[i]):
                            actv_pstn[i + row][j + col] = 1
    
    all_nums = []
    
    for i in range(len(full_code)):
        j = 0
        
        num_val = False
        new_num = ""
        numbers = []
        
        while j < len(full_code[i]):
            if full_code[i][j].isdigit():
                new_num += full_code[i][j]
                
                if num_val == False and actv_pstn[i][j] > 0:
                    num_val = True
            else:                
                if num_val and new_num != "":
                    numbers.append(int(new_num))
                
                num_val = False
                new_num = ""
            
            j += 1
        
        if num_val and new_num != "":
            numbers.append(int(new_num))
        
        num_val = False
        new_num = ""
        
        all_nums.append(numbers)
    
    print(sum(sum(all_nums, [])))