def dfs(x, y, costs, num_of_colors, dp):

    if x >= len(costs) or y >= num_of_colors: return 0
    if (x, y) in dp: return dp[(x, y)]

    min_cost = float('inf')

    for color in range(num_of_colors):
        if color != y:
            min_cost = min(min_cost, costs[x][y] + dfs(x+1, color, costs, num_of_colors, dp))
    dp[(x, y)] = min_cost

    return min_cost


def minimize_costs(costs, num_of_colors):
    min_cost = float('inf')
    dp = {}
    for x in range(num_of_colors):
        min_cost = min(min_cost, dfs(0, x, costs, num_of_colors, dp))
    
    return min_cost


# print(minimize_costs([
#     [6, 2, 6],
#     [1, 7, 9],
# ], 3))

# print(minimize_costs([
#     [6, 2, 6],
#     [1, 7, 9],
#     [4, 2, 4],
#     [5, 3, 3],
#     [9, 1, 1],
# ], 3))

assert minimize_costs([
    [6, 2, 6],
    [1, 7, 9],
], 3) == 3

assert minimize_costs([
    [6, 2, 6],
    [1, 7, 9],
    [4, 2, 4],
    [5, 3, 3],
    [9, 1, 1],
], 3) == 9