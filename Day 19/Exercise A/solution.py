import functions as fc

workflows, ratings = fc.read_file("code.txt")

fc.process_parts(workflows, ratings)

total = 0

for r in ratings:
    if r["f"] == "A":
        for v in list(r.values())[2:]:
            total += v

print(total)