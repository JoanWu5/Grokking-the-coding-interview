# Given a set of positive numbers, 
# find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

# Example:
# Input: {1, 2, 3, 4}
# Output: True
# Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

# top-down dp
# O(N * S) where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.
def can_partition(num):
    sum_num = sum(num)
    if sum_num % 2 != 0:
        return False
    
    dp = [[-1 for _ in range(int(sum_num/2) + 1)] for _ in range(len(num))]
    return True if can_partition_recursive(dp, num, int(sum_num/2), 0) == 1 else False

def can_partition_recursive(dp, num, sum_num, current_index):
    if sum_num == 0:
        return 1
    
    n = len(num)
    if n == 0 or current_index >= n:
        return 0
    
    if dp[current_index][sum_num] == -1:
        if num[current_index] <= sum_num:
            if can_partition_recursive(dp, num, sum_num - num[current_index], current_index + 1):
                dp[current_index][sum_num] = 1
                return 1
        
        dp[current_index][sum_num] = can_partition_recursive(dp, num, sum_num, current_index + 1)

    return dp[current_index][sum_num]

print(can_partition([1, 2, 3, 4]))
print(can_partition([1, 1, 3, 4, 7]))
print(can_partition([2, 3, 4, 6]))

# bottom-up
# O(N * S) space: O(N * S)
def can_partition_2(num):
    sum_num = sum(num)
    if sum_num % 2 != 0:
        return False
    sum_num = int(sum_num/2)
    n = len(num)
    dp = [[False for _ in range(sum_num + 1)] for _ in range(n)]
    
    for i in range(n):
        dp[i][0] = True
    
    for j in range(1, sum_num + 1):
        dp[0][j] = num[0] == j
    
    for i in range(1, n):
        for j in range(1, sum_num + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]
    
    return dp[n - 1][sum_num]

print(can_partition_2([1, 2, 3, 4]))
print(can_partition_2([1, 1, 3, 4, 7]))
print(can_partition_2([2, 3, 4, 6]))