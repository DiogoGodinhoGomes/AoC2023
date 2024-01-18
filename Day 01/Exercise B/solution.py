dictionary = {
    'zero'  : 'ze0ro',
    'one'   : 'on1e',
    'two'   : 'tw2o',
    'three' : 'th3ree',
    'four'  : 'fo4ur',
    'five'  : 'fi5ve',
    'six'   : 'si6x',
    'seven' : 'se7ven',
    'eight' : 'ei8ght',
    'nine'  : 'ni9ne' }

sum = 0

with open("code.txt") as code:
    for line in code:     
        new_line = line
        
        for i, key in enumerate(dictionary.keys()):
            new_line = new_line.replace(key, dictionary[key])
        
        result = ''.join(character for character in new_line if character.isdigit())
        
        if len(result) > 0:
            a = int(result[0] + result[-1])
            
            sum += a

print(sum)