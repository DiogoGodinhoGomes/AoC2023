import functions as fc

mp, sp, fp = fc.get_mapa("code.txt")

ml, pt = fc.get_paths(mp, sp, fp)

print(ml)