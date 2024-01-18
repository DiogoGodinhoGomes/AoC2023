import time as tm
import functions as fc

st, tag, number, total = tm.time(), "", 5, 0

springs = fc.get_springs(tag + "code.txt", number)

total = fc.write_finals(tag, number, springs, st)

print(total)