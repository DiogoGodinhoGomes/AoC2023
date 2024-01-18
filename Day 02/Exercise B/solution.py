with open("code.txt") as code:
    total = 0
    
    for line in code:
        if line.find(":") >= 0:
            split_line = line.split()
            
            dtnr = { "red" : 0, "green": 0, "blue": 0 }
            
            for i, text in enumerate(split_line):
                for j, key in enumerate(dtnr.keys()):
                    if text.find(key) >= 0:
                        if int(split_line[i - 1]) > dtnr[key]:
                            dtnr[key] = int(split_line[i - 1])
            
            game_total = 1
            
            for key in dtnr.keys():
                game_total *= dtnr[key]
            
            total += game_total
    
    print(total)