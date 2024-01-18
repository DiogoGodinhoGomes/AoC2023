def reset_dict(dtnr):
    for i in dtnr:
        dtnr[i] = 0
    
    return dtnr

def get_total_points(hand, cv, ct, mt):
    j = 0
    
    for i in hand:
        if i == "J":
            j += 1
        else:
            ct[i] += 1
    
    assert(len(hand) == sum(ct.values()) + j)
    
    for i in list(ct.values())[:-1]:
        if i > 0:
            mt[i] += 1
    
    highest = 1
    
    for i in mt:
        if mt[i] > 0:
            highest = i
    
    if j > 0 and j < len(hand):
        mt[highest] -= 1
        mt[highest + j] += 1
    elif j == len(hand):
        mt[j] += 1
    
    total = 0
    
    for i in mt:
        total += i * mt[i]
    
    assert(len(hand) == total)
    
    ht = 0
    
    if mt[5] == 1:
        ht = 6
    elif mt[4] == 1:
        ht = 5
    elif mt[3] == 1 and mt[2] == 1:
        ht = 4
    elif mt[3] == 1:
        ht = 3
    elif mt[2] == 2:
        ht = 2
    elif mt[2] == 1:
        ht = 1
    elif mt[1] == 5:
        ht = 0
    else:
        assert(False)
    
    tp = ht * int(1e6)
    
    for i in range(len(hand) - 1, -1, -1):
        tp += cv[hand[len(hand) - 1 - i]] * pow(len(cv), i)
    
    reset_dict(ct)
    reset_dict(mt)
    
    return tp

card_values = { "A": 12, "K": 11, "Q": 10, "T": 9, "9": 8, "8": 7, "7": 6,
               "6": 5, "5": 4, "4": 3, "3": 2, "2": 1, "J": 0 }

card_types = { "A": 0, "K": 0, "Q": 0, "T": 0, "9": 0, "8": 0,"7": 0,
               "6": 0, "5": 0, "4": 0, "3": 0, "2": 0, "J": 0 }

match_types = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 }

hand_list = []

with open("code.txt") as code:
    for line in code:
        hand_list.append(line.split())

for i in hand_list:
    i.append(get_total_points(i[0], card_values, card_types, match_types))

hand_list = sorted(hand_list, key = lambda x: x[2])

result = 0

for i, elem in enumerate(hand_list):
    result += (i + 1) * int(elem[1])

print(result)