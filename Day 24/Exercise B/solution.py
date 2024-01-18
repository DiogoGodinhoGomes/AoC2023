import functions as fc

s = fc.get_stones("code.txt")

x = fc.get_result(s, 6)

print(sum(x[:3]))