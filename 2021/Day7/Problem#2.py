from collections import Counter

file_name = "Day7/Day7Input.txt"

with open(file_name) as file:
    all_positions = tuple(map(int, file.readline().strip().split(",")))


max_pos = max(all_positions) + 1
counts_per_pos = Counter(all_positions)
gauss = [0, 1]

for k in range(2, max_pos):
    gauss.append(gauss[k - 1] + k)

new_costs = {
    k: sum(
        gauss[abs(k - kk)] * counts_per_pos[kk]
        for kk in counts_per_pos
        if k != kk
    )
    for k in range(1, max_pos // 2)
}

new_min_cost_pos = min(new_costs, key=new_costs.get)

print(f"New Minimum Cost is {new_costs[new_min_cost_pos]} to position {new_min_cost_pos}")
