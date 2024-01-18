import copy as cp

def read_file(filename):
    workflows = {}
    
    with open(filename) as file:
        for line in file:
            if line[0] != "{" and line[0] != "\n":
                new_line = list(line.replace("{", ",").replace("}", "").strip().split(","))
                
                new_list = []
                
                for i in new_line[1:]:
                    if ":" in i:
                        pos = i.index(":")
                        
                        new_list.append([ i[0], i[1], int(i[2:pos]), i[pos + 1:]])
                    else:
                        new_list.append([i])
                
                workflows[new_line[0]] = new_list
    
    return workflows

def get_old_total(ratings):
    total = 0

    for r in ratings:
        if r["f"] == "A":
            for v in list(r.values())[2:]:
                total += v

    return total

def get_all_ratings(workflows):
    ratings = [{ "f": "", "c": "in", "i": 0, "x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}]

    index = 0

    while index < len(ratings):
        while len(ratings[index]["f"]) == 0:
            wkf = workflows[ratings[index]["c"]][ratings[index]["i"]]
            
            if len(wkf) > 1:
                if wkf[1] == ">":
                    if ratings[index][wkf[0]][0] > wkf[2]:
                        if wkf[3] == "A" or wkf[3] == "R":
                            ratings[index]["f"] = wkf[3]
                        else:
                            ratings[index]["c"] = wkf[3]
                            
                            ratings[index]["i"] = 0
                    elif ratings[index][wkf[0]][1] < wkf[2]:
                        ratings[index]["i"] += 1
                    else:
                        temp = cp.deepcopy(ratings[index])
                        
                        temp[wkf[0]][1] = wkf[2]
                        
                        temp["i"] += 1
                        
                        ratings.insert(index + 1, temp)
                        
                        ratings[index][wkf[0]][0] = wkf[2] + 1
                        
                        if wkf[3] == "A" or wkf[3] == "R":
                            ratings[index]["f"] = wkf[3]
                        else:
                            ratings[index]["c"] = wkf[3]
                            
                            ratings[index]["i"] = 0
                elif wkf[1] == "<":
                    if ratings[index][wkf[0]][1] < wkf[2]:
                        if wkf[3] == "A" or wkf[3] == "R":
                            ratings[index]["f"] = wkf[3]
                        else:
                            ratings[index]["c"] = wkf[3]
                            
                            ratings[index]["i"] = 0
                    elif ratings[index][wkf[0]][0] > wkf[2]:
                        ratings[index]["i"] += 1
                    else:
                        temp = cp.deepcopy(ratings[index])
                        
                        temp[wkf[0]][0] = wkf[2]
                        
                        temp["i"] += 1
                        
                        ratings.insert(index + 1, temp)
                        
                        ratings[index][wkf[0]][1] = wkf[2] - 1
                        
                        if wkf[3] == "A" or wkf[3] == "R":
                            ratings[index]["f"] = wkf[3]
                        else:
                            ratings[index]["c"] = wkf[3]
                            
                            ratings[index]["i"] = 0
                else:
                    assert(False)
            else:
                if wkf[0] == "A" or wkf[0] == "R":
                    ratings[index]["f"] = wkf[0]
                else:
                    ratings[index]["c"] = wkf[0]
                    
                    ratings[index]["i"] = 0
        
        assert(ratings[index]["x"][1] >= ratings[index]["x"][0])
        assert(ratings[index]["m"][1] >= ratings[index]["m"][0])
        assert(ratings[index]["a"][1] >= ratings[index]["a"][0])
        assert(ratings[index]["s"][1] >= ratings[index]["s"][0])
        
        assert(ratings[index]["f"] == "A" or ratings[index]["f"] == "R")
        
        ratings[index]["t"] = 1
        
        ratings[index]["t"] *= ratings[index]["x"][1] + 1 - ratings[index]["x"][0]
        ratings[index]["t"] *= ratings[index]["m"][1] + 1 - ratings[index]["m"][0]
        ratings[index]["t"] *= ratings[index]["a"][1] + 1 - ratings[index]["a"][0]
        ratings[index]["t"] *= ratings[index]["s"][1] + 1 - ratings[index]["s"][0]
        
        assert(ratings[index]["t"] > 0)
        
        index += 1
    
    return ratings

def get_new_total(ratings):
    total = 0

    for i in ratings:
        if i["f"] == "A":
            total += i["t"]

    return total