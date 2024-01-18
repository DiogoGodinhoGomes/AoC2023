def extract_card(line):
    state = 0
    
    winning_numbers = []
    numbers_you_have = []
    
    new_line = line.replace(":", " :").split()
    
    for i in new_line:
        if i == "Card":
            continue
        elif i == ":":
            state = 1
        elif i == "|":
            state = 2
        elif state == 0:
            game_id = int(i)
        elif state == 1:
            winning_numbers.append(int(i))
        elif state == 2:
            numbers_you_have.append(int(i))
    
    return game_id, winning_numbers, numbers_you_have

def check_card(winning_numbers, numbers_you_have):
    hits = 0
    
    for w in winning_numbers:
        if w in numbers_you_have:
            hits += 1
    
    return pow(2, hits - 1) if hits > 0 else 0

with open("code.txt") as code:
    points = 0
    
    for line in code:
        game_id, winning_numbers, numbers_you_have = extract_card(line)
        
        points += check_card(winning_numbers, numbers_you_have)
    
    print(points)