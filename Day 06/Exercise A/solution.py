def get_parameters(filename):
    parameters = {}
    
    with open(filename) as code:
        for i, line in enumerate(code):
            for j, elem in enumerate(list(map(int, line.replace(":","").split()[1:]))):
                if i == 0:
                    parameters[elem] = 0
                else:
                    parameters[list(parameters.keys())[j]] = elem
    
    return parameters

def get_results(parameters):
    results = []

    for key in parameters.keys():
        possibilities = 0
        
        limit = int((key + 1) / 2)
        
        if key % 2 == 0:
            limit += 1
        
        for speed in range(limit):
            time = key - speed
            
            distance = speed * time
            
            if distance > parameters[key]:
                possibilities += 1
        
        if key % 2 == 0:
            possibilities = (possibilities - 1) * 2 + 1
        else:
            possibilities *= 2
        
        results.append(possibilities)
    
    return results

def get_product(results):
    total = 1

    for i in results:
        total *= i

    return total

print(get_product(get_results(get_parameters("code.txt"))))