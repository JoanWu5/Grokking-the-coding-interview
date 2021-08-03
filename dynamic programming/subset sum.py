# Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

# Example: 
# Input: {1, 2, 3, 7}, S=6
# Output: True
# The given set has a subset whose sum is '6': {1, 2, 3}

# O(N * S) space: O(N * S)
def can_subset_sum(num, s):
    if sum(num) < s:
        return False
    
    n = len(num)
    dp = [[False for _ in range(s + 1)]for _ in range(n)]

    for i in range(n):
        dp[i][0] = True
    
    for j in range(1, s + 1):
        dp[0][j] = j == num[0]

    for i in range(1, n):
        for j in range(1, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]
    
    return dp[n - 1][s]

print(can_subset_sum([1, 2, 3, 7], 6))
print(can_subset_sum([1, 2, 7, 1, 5], 10))
print(can_subset_sum([1, 3, 4, 8], 6))

# O(N * S) space: O(S)
def can_subset_sum_2(num, s):
    if sum(num) < s:
        return False
    
    n = len(num)
    dp = [False for _ in range(s + 1)]

    dp[0] = True

    for i in range(n):
        for j in range(s, -1, -1):
            if not dp[j] and j >= num[i]:
                dp[j] = dp[j - num[i]]
    
    return dp[s]


print(can_subset_sum_2([1, 2, 3, 7], 6))
print(can_subset_sum_2([1, 2, 7, 1, 5], 10))
print(can_subset_sum_2([1, 3, 4, 8], 6))
