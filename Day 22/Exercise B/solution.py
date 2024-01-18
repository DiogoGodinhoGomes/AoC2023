import functions as fc

sc, mp = fc.get_scmp("code.txt")

fall, rmv = fc.get_fall(sc, mp)

total = fc.get_total(sc, mp, rmv)

print(total)