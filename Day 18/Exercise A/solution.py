import functions as fc

instr = fc.read_instr("excode.txt")

mapa = fc.get_mapa(instr)

init_pos, init_d = fc.get_initial(mapa)

borders = fc.get_borders(mapa, init_pos, init_d)

fc.paint_all(mapa, borders)

for r in mapa:
    for e in r:
        print(e, end = "\t")
    
    print()

print(fc.get_total(mapa))