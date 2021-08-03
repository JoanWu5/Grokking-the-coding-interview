# Given two integer arrays to represent weights and profits of ‘N’ items, 
# we need to find a subset of these items which will give us maximum profit 
# such that their cumulative weight is not more than a given number ‘C’. 
# Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

# brute force
# O(2^N) space: O(N)
def knapsack_1(profits, weights, capacity):
    return knapsack_recursive_1(profits, weights, capacity, 0)

def knapsack_recursive_1(profits, weights, capacity, current_index):
    if capacity <= 0 or current_index >= len(profits):
        return 0
    
    profit1, profit2 = 0, 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knapsack_recursive_1(profits, weights, capacity - weights[current_index], current_index + 1)
    
    profit2 = knapsack_recursive_1(profits, weights, capacity, current_index + 1)
    return max(profit1, profit2)

print(knapsack_1([4, 5, 3, 7], [2, 3, 1, 4], 5))

# top-down dp
# O(N * C) space: O(N * C)
def knapsack_2(profits, weights, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profits))]
    return knapsack_recursive_2(dp, profits, weights, capacity, 0)

def knapsack_recursive_2(dp, profits, weights, capacity, current_index):
    if capacity <= 0 or current_index >= len(profits):
        return 0
    
    if dp[current_index][capacity] != 0:
        return dp[current_index][capacity]

    profit1, profit2 = 0, 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knapsack_recursive_2(dp, profits, weights, capacity - weights[current_index], current_index + 1)
    
    profit2 = knapsack_recursive_2(dp, profits, weights, capacity, current_index + 1)
    dp[current_index][capacity] = max(profit1, profit2)
    return dp[current_index][capacity]

print(knapsack_2([4, 5, 3, 7], [2, 3, 1, 4], 5))


# bottom-up dp
# O(N * C) space: O(N * C)
def knapsack_3(profits, weights, capacity):
    if capacity <= 0 or len(profits) == 0 or len(profits) != len(weights):
        return 0


    n = len(profits)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    
    for i in range(1, n):
        for j in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            if weights[i] <= j:
                profit1 = dp[i - 1][j - weights[i]] + profits[i]
            profit2 = dp[i - 1][j]
            dp[i][j] = max(profit1, profit2)

    print(print_selected_elements(dp, profits, weights, capacity))
    return dp[n - 1][capacity]

def print_selected_elements(dp, profits, weights, capacity):
    n = len(profits)
    result = []
    total_profit = dp[n - 1][capacity]
    for i in range(n - 1, -1, -1):
        if total_profit != dp[i - 1][capacity]:
            result.append(weights[i])
            capacity -= weights[i]
            total_profit -= profits[i]
    
    if total_profit > 0:
        result.append(weights[0])

    return result

print(knapsack_3([4, 5, 3, 7], [2, 3, 1, 4], 5))

# improve bottom-up solution
def knapsack_3_1(profits, weights, capacity):
    if capacity <= 0 or len(profits) == 0 or len(profits) != len(weights):
        return 0

    n = len(profits)
    dp = [0 for _ in range(capacity + 1)]

    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[c] = profits[0]
    
    for i in range(1, n):
        for j in range(capacity, -1, -1):
            profit1 = 0
            if weights[i] <= j:
                profit1 = dp[j - weights[i]] + profits[i]
            dp[j] = max(profit1, dp[j])

    return dp[capacity]

print(knapsack_3_1([4, 5, 3, 7], [2, 3, 1, 4], 5))