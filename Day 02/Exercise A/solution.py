dtnr = { "red" : 12, "green": 13, "blue": 14 }

with open("code.txt") as code:
    total = 0
    
    for line in code:
        if line.find(":") >= 0:
            split_line = line.split()
            
            possible_game = True
            
            for i, text in enumerate(split_line):
                for key in dtnr.keys():
                    if text.find(key) >= 0:
                        possible_game *= (int(split_line[i - 1]) <= dtnr[key])
            
            if possible_game:
                total += int(split_line[1].replace(":",""))
    
    print(total)