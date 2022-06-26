from collections import Counter

file_name = "Day7/Day7Input.txt"

with open(file_name) as file:
    all_positions = tuple(map(int, file.readline().strip().split(",")))


max_pos = max(all_positions) + 1
counts_per_pos = Counter(all_positions)

costs = {
    k: sum(abs(k - kk) * counts_per_pos[kk]
           for kk in counts_per_pos if k != kk)
    for k in range(max_pos // 2)
}

min_cost_pos = min(costs, key=costs.get)

print(f"Minimum Cost is {costs[min_cost_pos]} to position {min_cost_pos}")
