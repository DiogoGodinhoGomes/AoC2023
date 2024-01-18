import functions as fc

room, pos = fc.get_room("code.txt")

paths = fc.get_paths(room, pos)

print(fc.get_total(pos))