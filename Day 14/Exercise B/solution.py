import functions as fc

tag, num, period, value = "", 100, 0, int(1e9)

while period == 0:    
    plat = fc.get_plat(tag + "code.txt")
    
    lst, dtnr = fc.spin_cycle(plat, num)
    
    period = fc.find_period(lst, num)
    
    num *= 10

index, sequence = fc.get_index_sequence(lst, period)

actual_value = (value - index - 1) % len(sequence)

print(index, sequence, value, actual_value, sequence[actual_value])