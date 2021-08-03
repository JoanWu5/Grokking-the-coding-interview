# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

# Example:
# Input: {1, 1, 2, 3}, S=4
# Output: 3
# The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
# Note that we have two similar sets {1, 3}, because we have two '1' in our input.

# top-down dp
# O(N * S) space: O(N * S)
def count_of_subset_sum(nums, s):
    dp = [[-1 for _ in range(s + 1)] for _ in range(len(nums))]
    return count_of_subset_sum_recursive(dp, nums, 0, s)

def count_of_subset_sum_recursive(dp, nums, current_index, s):
    if s == 0:
        return 1

    if current_index >= len(nums):
        return 0
    
    if dp[current_index][s] == -1:
        sum1 = 0
        if s - nums[current_index] >= 0:
            sum1 = count_of_subset_sum_recursive(dp, nums, current_index + 1, s - nums[current_index])
    
        sum2 = count_of_subset_sum_recursive(dp, nums, current_index + 1, s)
        dp[current_index][s] = sum1 + sum2

    return dp[current_index][s]


print(count_of_subset_sum([1, 1, 2, 3], 4)) 
print(count_of_subset_sum([1, 2, 7, 1, 5], 9)) 

# bottom- up dp
# O(N * S) space: O(N * S)
def count_of_subset_sum_2(nums, s):
    dp = [[-1 for _ in range(s + 1)] for _ in range(len(nums))]
    
    for i in range(len(nums)):
        dp[i][0] = 1
    
    for j in range(1, s + 1):
        if nums[0] == j:
            dp[0][j] = 1
        else:
            dp[0][j] = 0
    
    for i in range(1, len(nums)):
        for j in range(1, s + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i]:
                dp[i][j] += dp[i - 1][j - nums[i]]
    
    return dp[len(nums) - 1][s]


print(count_of_subset_sum_2([1, 1, 2, 3], 4)) 
print(count_of_subset_sum_2([1, 2, 7, 1, 5], 9)) 
