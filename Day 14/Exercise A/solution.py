plat = []

with open("code.txt") as file:
    for line in file:
        plat.append(list(line.strip()))

for col in range(len(plat[0])):
    last_empty_row = 0
    
    for row in range(len(plat)):        
        if plat[row][col] == "O":
            plat[row][col] = "."
            
            plat[last_empty_row][col] = "O"
            
            last_empty_row += 1
        elif plat[row][col] == "#" and row + 1 < len(plat):
            last_empty_row = row + 1

total = 0

for row in range(len(plat)):
    current = 0
    
    for elem in plat[row]:
        if elem == "O":
            current += 1
    
    total += (len(plat) - row) * current

print(total)