# You are given a set of positive numbers and a target sum ‘S’. 
# Each number should be assigned either a ‘+’ or ‘-’ sign. 
# We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.

# Example:
# Input: {1, 1, 2, 3}, S=1
# Output: 3
# Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

# top-down dp
# O(N * S) space: O(N * S)
def target_sum(nums, s):
    total_sum = sum(nums)
    if total_sum < s or (s + total_sum) % 2 != 0:
        return 0

    target_sum = (s + total_sum) // 2
    dp = [[-1 for _ in range(target_sum + 1)] for _ in range(len(nums))]

    return target_sum_recursive(dp, nums, target_sum, 0)

def target_sum_recursive(dp, nums, s, current_index):
    if s == 0:
        return 1
    
    if current_index >= len(nums):
        return 0
    
    if dp[current_index][s] == -1:
        sum1 = 0
        if s >= nums[current_index]:
            sum1 = target_sum_recursive(dp, nums, s - nums[current_index], current_index + 1)
        sum2 = target_sum_recursive(dp, nums, s, current_index + 1)
        
        dp[current_index][s] = sum1 + sum2
    
    return dp[current_index][s]

print(target_sum([1, 1, 2, 3], 1))
print(target_sum([1, 2, 7, 1], 9))

# bottom-up
# O(N * S) space: O(N * S)
def target_sum_2(nums, s):
    total_sum = sum(nums)
    if total_sum < s or (s + total_sum) % 2 != 0:
        return 0

    target_sum = (s + total_sum) // 2

    dp = [[0 for _ in range(target_sum + 1)] for _ in range(len(nums))]
    
    for i in range(len(nums)):
        dp[i][0] = 1

    for j in range(1, target_sum + 1):
        dp[0][j] = 1 if nums[0] == j else 0
        
    for i in range(1, len(nums)):
        for j in range(1, target_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i]:
                dp[i][j] += dp[i - 1][j - nums[i]]

    return dp[len(nums) - 1][target_sum]

print(target_sum_2([1, 1, 2, 3], 1))
print(target_sum_2([1, 2, 7, 1], 9))          

# bottom-up optimize space complexity
# O(N * S) space: O(S)
def target_sum_3(nums, s):
    total_sum = sum(nums)
    if total_sum < s or (s + total_sum) % 2 != 0:
        return 0

    target_sum = (s + total_sum) // 2

    dp = [0 for _ in range(target_sum + 1)]
    
    dp[0] = 1

    for j in range(1, target_sum + 1):
        dp[j] = 1 if nums[0] == j else 0
        
    for i in range(1, len(nums)):
        for j in range(target_sum, -1, -1):
            if j >= nums[i]:
                dp[j] += dp[j - nums[i]]

    return dp[target_sum]

print(target_sum_3([1, 1, 2, 3], 1))
print(target_sum_3([1, 2, 7, 1], 9)) 
