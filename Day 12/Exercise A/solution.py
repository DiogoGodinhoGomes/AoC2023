import functions as fc

springs = fc.get_springs("code.txt")

final_springs = fc.get_final_springs(springs)

print(fc.get_total(final_springs))