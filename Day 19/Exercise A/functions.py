def read_file(filename):
    workflows, ratings = {}, []
    
    with open(filename) as file:
        for line in file:
            if line[0] == "{":
                new_line = list(line.replace("{", "").replace("}", "").replace("=", "").strip().split(","))
                
                new_dtnr = { "f": "", "c": "in" }
                
                for i in new_line:
                    new_dtnr[i[0]] = int(i[1:])
                
                ratings.append(new_dtnr)
            elif line != "\n":
                new_line = list(line.replace("{", ",").replace("}", "").strip().split(","))
                
                new_list = []
                
                for i in new_line[1:]:
                    if ":" in i:
                        pos = i.index(":")
                        
                        new_list.append([ i[0], i[1], int(i[2:pos]), i[pos + 1:]])
                    else:
                        new_list.append([i])
                
                workflows[new_line[0]] = new_list
    
    return workflows, ratings

def process_parts(workflows, ratings):
    for obj in ratings:
        i = 0
        
        while len(obj["f"]) == 0:
            wkf = workflows[obj["c"]][i]
            
            if len(wkf) > 1:
                if wkf[1] == ">":
                    if obj[wkf[0]] > wkf[2]:
                        if wkf[3] == "A" or wkf[3] == "R":
                            obj["f"] = wkf[3]
                        else:
                            obj["c"] = wkf[3]
                            
                            i = 0
                    else:
                        i += 1
                elif wkf[1] == "<":
                    if obj[wkf[0]] < wkf[2]:
                        if wkf[3] == "A" or wkf[3] == "R":
                            obj["f"] = wkf[3]
                        else:
                            obj["c"] = wkf[3]
                            
                            i = 0
                    else:
                        i += 1
                else:
                    assert(False)
            else:
                if wkf[0] == "A" or wkf[0] == "R":
                    obj["f"] = wkf[0]
                else:
                    obj["c"] = wkf[0]
                    
                    i = 0