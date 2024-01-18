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
            continue
        elif state == 1:
            winning_numbers.append(int(i))
        elif state == 2:
            numbers_you_have.append(int(i))
    
    hits = 0
    
    for w in winning_numbers:
        if w in numbers_you_have:
            hits += 1
    
    return hits

with open("code.txt") as code:
    hits = []
    
    for line in code:
        hits.append(extract_card(line))
    
    total_cards = [1] * len(hits)
    
    for i, h in enumerate(hits):
        for n in range(1, h + 1):
            if i + n < len(hits):
                total_cards[i + n] += total_cards[i]
    
    print(sum(total_cards))