import time as tm
import numpy as np

dtnr = { "X": 0, "L": 1, "R": 2}

sequence = []

code_list = []

with open("code.txt") as code:
    for i, line in enumerate(code):
        if i == 0:
            sequence = line.strip()
        elif len(line.strip()) > 0:
            code_list.append(line.strip().replace("=", "").replace("(", "").replace(",", "").replace(")","").split())

simplified_code_list = []

for line in code_list:
    L = list(np.array(code_list)[:,0]).index(line[1])
    R = list(np.array(code_list)[:,0]).index(line[2])
    
    simplified_code_list.append([L, R])

steps = 0

current_location = list(np.array(code_list)[:,0]).index("AAA")

destination = list(np.array(code_list)[:,0]).index("ZZZ")

start_time = tm.time()

while current_location != destination:
    left_or_right = dtnr[sequence[steps % len(sequence)]] - 1
    
    current_location = simplified_code_list[current_location][left_or_right]
    
    steps += 1

print(steps, current_location, destination, tm.time() - start_time)