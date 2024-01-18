import functions as fc

stones = fc.get_stones("code.txt")

total = fc.get_collisions(stones, 200000000000000, 400000000000000)

print(total)