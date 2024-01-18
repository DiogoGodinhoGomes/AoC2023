def get_list(filename):
    lst = []

    with open(filename) as file:
        for line in file:
            lst += line.strip().split(",")
    
    return lst

def get_hash(string):
    curr = 0

    for i in string:
        curr += ord(i)
        
        curr *= 17
        
        curr = curr % pow(2, 8)
    
    return curr

def get_total(lst):
    total = 0

    for i in lst:
        total += get_hash(i)

    return total

def get_boxes(lst):
    boxes = []

    for i in range(pow(2, 8)):
        boxes.append([])

    for case in lst:
        if "=" in case:
            symbol = "="
            
            lense = int(case[-1])
        elif "-" in case:
            symbol = "-"
            
            lense = 0
        else:
            assert(False)
        
        string = case[:case.index(symbol)]
        
        box = get_hash(string)
        
        if symbol == "-":
            i, found = 0, False
            
            while i < len(boxes[box]) and not found:
                if boxes[box][i][0] == string:
                    boxes[box].remove(boxes[box][i])
                    
                    found = True
                
                i += 1
        elif symbol == "=":
            i, found = 0, False
            
            while i < len(boxes[box]) and not found:
                if boxes[box][i][0] == string:
                    assert(lense > 0)
                    
                    boxes[box][i] = [string, lense]
                    
                    found = True
                
                i += 1
            
            if not found:
                boxes[box].append([string, lense])
    
    return boxes

def get_power(boxes):
    total = 0

    for b, box in enumerate(boxes):
        for l, lense in enumerate(box):
            total += (b + 1) * (l + 1) * lense[1]

    return total