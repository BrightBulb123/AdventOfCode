import timeit

print(timeit.timeit("""
file_name = "Day7/Day7Input.txt"

with open(file_name) as file:
    horizontal_positions = tuple(map(int, file.readline().strip().split(",")))

position_map = {
    pos: horizontal_positions.count(pos) for pos in set(horizontal_positions)
}

feul_spends = []

for new_pos in range(max(position_map.keys()) // 2):
    feul_spends.append(
        sum(
            abs(new_pos - current_pos) * n
            for current_pos, n in position_map.items()
        )
    )

#print(f"Min Cost Step 1: {min(feul_spends)}")

new_feul_spends = []

for new_pos in range(max(position_map.keys()) // 2):
    new_feul_spends.append(
        sum(
            ((abs(new_pos - current_pos) * (1 + abs(new_pos - current_pos))) // 2)
            * n
            for current_pos, n in position_map.items()
        )
    )
#print(f"Min Cost Step 2: {min(new_feul_spends)}")
""", number=100))
