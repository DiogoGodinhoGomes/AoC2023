import functions as fc

drct = { "PH": 1, "PV": 2, "NH": -1, "NV": -2 }

maximum, i, index, filename = 0, 0, 0, "code.txt"

room, pos = fc.get_room(filename)

for x in range(2 * len(room[0])):
    if int(x / len(room[0])) == 0:
        paths = [ [ 0, x % len(room[0]), drct["PV"] ] ]
    else:
        paths = [ [ len(room) - 1, x % len(room[0]), drct["NV"] ] ]
    
    room, pos = fc.get_room(filename)
    
    fc.get_paths(room, pos, paths, drct)
    
    curr = fc.get_total(pos)
    
    if curr > maximum:
        maximum = curr
        
        index = i
    
    i += 1

for y in range(2 * len(room)):
    if int(y / len(room)) == 0:
        paths = [ [ y % len(room), 0, drct["PH"] ] ]
    else:
        paths = [ [ y % len(room), len(room[y % len(room)]) - 1, drct["NH"] ] ]
    
    room, pos = fc.get_room(filename)
    
    fc.get_paths(room, pos, paths, drct)
    
    curr = fc.get_total(pos)
    
    if curr > maximum:
        maximum = curr
        
        index = i
    
    i += 1

print(maximum)