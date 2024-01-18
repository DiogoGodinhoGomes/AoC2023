def get_list(filename):
    lst = []

    with open(filename) as file:
        for line in file:
            lst += line.strip().split(",")
    
    return lst

def get_hash(string):
    curr = 0

    for i in string:
        curr += ord(i)
        
        curr *= 17
        
        curr = curr % pow(2, 8)
    
    return curr

lst = get_list("code.txt")

total = 0

for i in lst:
    total += get_hash(i)

print(total)