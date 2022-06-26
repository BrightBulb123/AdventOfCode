import timeit

print(timeit.timeit("""
from collections import Counter
file_name = "Day7/Day7Input.txt"


with open(file_name) as file:
    all_positions = tuple(map(int, file.readline().strip().split(",")))

max_pos = max(all_positions) + 1

counts_per_pos = Counter(all_positions)

costs = {
    k: sum(abs(k - kk) * counts_per_pos[kk]
           for kk in counts_per_pos if k != kk)
    for k in range(max_pos//2)
}

min_cost_pos = min(costs, key=costs.get)

#print(f"Minimum Cost is {costs[min_cost_pos]} to position {min_cost_pos}")

# print(counts_per_pos)
# print(costs)

#print("Step 2")

new_costs = {}

pascal = [0, 1]

for k in range(2, max_pos):
    pascal.append(pascal[k-1]+k)

for k in range(1, max_pos//2):
    new_costs[k] = 0

    for kk in counts_per_pos:
        if k == kk:
            continue

        new_costs[k] += pascal[abs(k-kk)] * counts_per_pos[kk]

new_min_cost_pos = min(new_costs, key=new_costs.get)

#print(f"New Minimum Cost is {new_costs[new_min_cost_pos]} to position {new_min_cost_pos}")
""", number=100))
