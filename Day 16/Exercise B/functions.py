def get_room(filename):
    room, pos = [], []
    
    with open(filename) as file:
        for line in file:
            room.append(list(line.strip()))
            
            pos.append([0] * len(list(line.strip())))
    
    return room, pos

def get_paths(room, pos, paths, drct):
    i, mmry = 0, set()

    while i < len(paths):
        while paths[i][0] >= 0 and paths[i][1] >= 0 and paths[i][0] < len(room) and paths[i][1] < len(room[paths[i][0]]) and tuple(paths[i]) not in mmry:
            mmry.add(tuple(paths[i]))
            
            pos[paths[i][0]][paths[i][1]] = 1
            
            if room[paths[i][0]][paths[i][1]] == "." or (room[paths[i][0]][paths[i][1]] == "-" and abs(paths[i][2]) == 1) or (room[paths[i][0]][paths[i][1]] == "|" and abs(paths[i][2]) == 2):
                if abs(paths[i][2]) == 1:
                    paths[i][1] += int( paths[i][2] / abs(paths[i][2]) )
                elif abs(paths[i][2]) == 2:
                    paths[i][0] += int( paths[i][2] / abs(paths[i][2]) )
            elif room[paths[i][0]][paths[i][1]] == "\\":
                if abs(paths[i][2]) == 1:
                    paths[i][2] = int(paths[i][2] * 2)
                    
                    paths[i][0] += int( paths[i][2] / abs(paths[i][2]) )
                elif abs(paths[i][2]) == 2:
                    paths[i][2] = int(paths[i][2] / 2)
                    
                    paths[i][1] += int( paths[i][2] / abs(paths[i][2]) )
            elif room[paths[i][0]][paths[i][1]] == "/":
                if abs(paths[i][2]) == 1:
                    paths[i][2] = int(paths[i][2] * (-2))
                    
                    paths[i][0] += int( paths[i][2] / abs(paths[i][2]) )
                elif abs(paths[i][2]) == 2:
                    paths[i][2] = int(paths[i][2] / (-2))
                    
                    paths[i][1] += int( paths[i][2] / abs(paths[i][2]) )
            elif room[paths[i][0]][paths[i][1]] == "-" and abs(paths[i][2]) == 2:
                paths[i][2] = drct["PH"]
                
                paths.append([abs(paths[i][0]), paths[i][1] - 1, drct["NH"]])
                
                paths[i][1] += 1
            elif room[paths[i][0]][paths[i][1]] == "|" and abs(paths[i][2]) == 1:
                paths[i][2] = drct["PV"]
                
                paths.append([paths[i][0] - 1, abs(paths[i][1]), drct["NV"]])
                
                paths[i][0] += 1
        
        i += 1
    
    return paths

def get_total(pos):
    total = 0

    for i in pos:
        for j in i:
            total += j

    return total