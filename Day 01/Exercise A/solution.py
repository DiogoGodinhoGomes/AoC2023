sum = 0

with open("code.txt") as code:
    for line in code:
        result = ''.join(character for character in line if character.isdigit())
        
        a = int(result[0] + result[-1])
        
        sum += a

print(sum)