import functions as fc

min_s, max_s = 4, 10

data = fc.get_data("code.txt")

heat_loss, sequence = fc.get_dijkstra_with_restrictions(data, min_s, max_s)

print("\n" + str(heat_loss))