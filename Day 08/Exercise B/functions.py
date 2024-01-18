import numpy as np

def get_periods(required_potential_stops, filename):
    dtnr = { "L": 0, "R": 1, "A": 2, "Z": 3}
    
    sequence = []
    
    code_list = []
    
    with open(filename) as code:
        for i, line in enumerate(code):
            if i == 0:
                sequence = line.strip()
            elif len(line.strip()) > 0:
                code_list.append(line.strip().replace("=", "").replace("(", "").replace(",", "").replace(")","").split())
    
    simplified_code_list = []
    
    for line in code_list:
        L = list(np.array(code_list)[:,0]).index(line[1])
        R = list(np.array(code_list)[:,0]).index(line[2])
        
        A = 1 if line[0][2] == "A" else 0
        Z = 1 if line[0][2] == "Z" else 0
        
        simplified_code_list.append([L, R, A, Z])
    
    steps = 0
    
    current_locations = []
    
    for i, elem in enumerate(simplified_code_list):
        if elem[dtnr["A"]] == 1:
            Z = 1 if elem[3] == 1 else 0
            
            current_locations.append([i, Z])
    
    potential_stops = []
    
    for i in range(len(current_locations)):
        potential_stops.append([])
    
    min_len = len(potential_stops[0])
    
    for i in potential_stops:
        if len(i) < min_len:
            min_len = len(i)
    
    while min_len < required_potential_stops:
        left_or_right = dtnr[sequence[steps % len(sequence)]]
        
        for i, elem in enumerate(current_locations):
            elem[0] = simplified_code_list[elem[0]][left_or_right]
            elem[1] = simplified_code_list[elem[0]][dtnr["Z"]]
            
            if elem[1] == 1:
                potential_stops[i].append(steps)
        
        min_len = len(potential_stops[0])
    
        for i in potential_stops:
            if len(i) < min_len:
                min_len = len(i)
        
        steps += 1
    
    for i, elem in enumerate(potential_stops):
        num = potential_stops[i][0]
        
        potential_stops[i] = np.array(elem)[1:] - np.array(elem)[:-1]
        
        potential_stops[i] = list(potential_stops[i] - potential_stops[i][0])
        
        if potential_stops[i] == [0] * len(potential_stops[i]):
            potential_stops[i] = num + 1
        else:
            assert(False)
    
    return potential_stops

def get_primes(maximum):
    num = 2

    primes = []

    while len(primes) < maximum:
        prime = True
        
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                prime = False
                break
        
        if prime:
            primes.append(num)
        
        num += 1

    return primes

def get_prime_factors(primes, number):
    new_dtnr = {}

    index = 0

    while number > 1:
        assert(index < len(primes))
        
        if number % primes[index] == 0:
            number /= primes[index]
            
            if primes[index] in new_dtnr.keys():
                new_dtnr[primes[index]] += 1
            else:
                new_dtnr[primes[index]] = 1
        else:
            index += 1

    return new_dtnr