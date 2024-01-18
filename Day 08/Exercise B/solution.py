import functions as fc

required_potential_stops = 100

periods = fc.get_periods(required_potential_stops, "code.txt")

primes = fc.get_primes(1000)

final_dtnr = {}

for i in periods:
    current_dtnr = fc.get_prime_factors(primes, i)
    
    for i in current_dtnr:
        if i in final_dtnr.keys():
            final_dtnr[i] = max(final_dtnr[i], current_dtnr[i])
        else:
            final_dtnr[i] = current_dtnr[i]

total = 1

for i in final_dtnr:
    total *= i * final_dtnr[i]

print(total)