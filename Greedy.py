def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    ratio = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    ratio.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    total_weight = 0
    for r, w, v in ratio:
        if total_weight + w <= capacity:
            total_value += v
            total_weight += w
        else:
            remaining_capacity = capacity - total_weight
            total_value += r * remaining_capacity
            break
    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
max_value = knapsack_greedy(weights, values, capacity)
print(f"Maximum value in knapsack (greedy approach): {max_value}")
