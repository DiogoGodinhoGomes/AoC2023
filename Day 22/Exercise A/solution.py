import functions as fc

sc, mp, ax, ay, az = fc.get_scmp("code.txt")

rmv = fc.get_fall(sc, mp)

print(len(sc) - len(rmv), "\n")