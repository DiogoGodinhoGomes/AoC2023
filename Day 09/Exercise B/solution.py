import numpy as np
from collections import deque

sequences = []

with open("code.txt") as code:
    for line in code:
        sequences.append(deque(list(map(int, line.strip().split()))))

total = 0

for i, sequence in enumerate(sequences):
    temp_seq = [deque(sequence)]
    
    stop = False
    
    while not stop:        
        temp_seq.append(deque(np.array(list(temp_seq[-1])[1:]) - np.array(list(temp_seq[-1])[:-1])))
        
        if list(temp_seq[-1]) == [0] * len(temp_seq[-1]):
            stop = True
        
    for i in range(len(temp_seq) - 2, -1, -1):
        temp_seq[i].appendleft(temp_seq[i][0] - temp_seq[i + 1][0])
    
    total += temp_seq[0][0]

print(total)