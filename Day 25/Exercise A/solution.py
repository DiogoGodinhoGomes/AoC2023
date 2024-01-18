import time as tm
import functions as fc

st = tm.time()

dtnr = fc.get_dtnr("code.txt")

final, fmaxi = fc.get_critical_links(fc.get_link_traffic(st, dtnr))

total = fc.get_total(dtnr, final)

print(total, tm.time() - st)