import functions as fc

workflows = fc.read_file("code.txt")

ratings = fc.get_all_ratings(workflows)

print(fc.get_new_total(ratings))