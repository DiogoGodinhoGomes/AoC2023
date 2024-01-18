import numpy as np

sequences = []

with open("code.txt") as code:
    for line in code:
        sequences.append(list(map(int, line.strip().split())))

total = 0

for i, sequence in enumerate(sequences):
    temp_seq = [sequence]
    
    stop = False
    
    while not stop:
        temp_seq.append(list(np.array(temp_seq[-1][1:]) - np.array(temp_seq[-1][:-1])))
        
        if temp_seq[-1] == [0] * len(temp_seq[-1]):
            stop = True
        
    for i in range(len(temp_seq) - 2, -1, -1):
        temp_seq[i].append(temp_seq[i][-1] + temp_seq[i + 1][-1])
    
    total += temp_seq[0][-1]

print(total)